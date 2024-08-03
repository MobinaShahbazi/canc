from sqlalchemy import select
import haversine as hs
from haversine import Unit
from app.models import Doctor
from app.models.sumit import association_table_D_MC, Medical_Center, association_table_I_MC, Insurer, Specialty


def findOptions(db, loc, province, specialty, patient_insurer, patient_loc):
    options = []
    distances = []
    stmt = select(Doctor.id, Medical_Center.id, Insurer.code, Medical_Center.latitude, Medical_Center.longitude,
                  Medical_Center.province).select_from(Doctor) \
        .join(Specialty, Doctor.specialty_id == Specialty.id) \
        .join(association_table_D_MC).join(Medical_Center) \
        .join(association_table_I_MC).join(Insurer) \
        .filter(Specialty.code == specialty)

    results = db.execute(stmt)
    for row in results:
        lat = row[3]
        lon = row[4]
        distances.append(distance(lat, lon, patient_loc))

    max_val = max(distances)
    min_val = min(distances)

    results = db.execute(stmt)
    for row in results:
        options.append([row[0], row[1], findScore(row[5], row[2], distance(row[3], row[4], patient_loc), province, patient_insurer, max_val, min_val)])

    sorted_options = sorted(options, key=lambda x: x[2], reverse=True)
    seen_first_parts = {}
    output_list = []
    for item in sorted_options:  # remove repetitive doctors
        first_part = item[0]
        if first_part not in seen_first_parts:
            seen_first_parts[first_part] = True
            output_list.append(item)

    for item in output_list:
        print(item)
    db.close()


def distance(lat, lon, patient_loc) -> float:

    latitude = float(lat)
    longetude = float(lon)
    loc1 = (latitude, longetude)
    result = hs.haversine(loc1, patient_loc, unit=Unit.KILOMETERS)
    return result


def findScore(province, insurer, distance, patient_prov, patient_insurer, max_val, min_val):

    if province == patient_prov:
        x1 = 1
    else:
        x1 = 0
    if insurer == patient_insurer:
        x2 = 1
    else:
        x2 = 0

    x3 = (distance - min_val) / (max_val - min_val)
    score = 1*x1 + 1*x2 + 1*x3
    return score

