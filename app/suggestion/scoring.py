from sqlalchemy import select
import haversine as hs
from haversine import Unit
from app.models import Doctor
from app.models.sumit import association_table_D_MC, Medical_Center, association_table_I_MC, Insurer, Specialty


def findOptions(db, loc, province, specialty, patient_insurer, patient_loc):
    options = []
    stmt = select(Doctor.id, Medical_Center.id, Insurer.code, Medical_Center.latitude, Medical_Center.longitude).select_from(Doctor) \
        .join(Specialty, Doctor.specialty_id == Specialty.id)\
        .join(association_table_D_MC).join(Medical_Center)\
        .join(association_table_I_MC).join(Insurer) \
        .filter(Specialty.code == specialty)

    results = db.execute(stmt)

    for row in results:
        if(row[2] == patient_insurer):
            lat = row[3]
            lon = row[4]
            options.append([row[0], row[1], distance(lat, lon, patient_loc)])

    sorted_options = sorted(options, key=lambda x: x[2])
    seen_first_parts = {}
    output_list = []
    for item in sorted_options:       # remove repetitive doctors
        first_part = item[0]
        if first_part not in seen_first_parts:
            seen_first_parts[first_part] = True
            output_list.append(item)

    for item in output_list:
        print(item)

    db.close()
    # print(options)


def distance(lat, lon, patient_loc) -> float:
    latitude = float(lat)
    longetude = float(lon)
    loc1 = (latitude, longetude)

    result = hs.haversine(loc1, patient_loc, unit=Unit.KILOMETERS)

    return result
