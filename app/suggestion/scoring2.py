import numpy as np
from sqlalchemy import select
import haversine as hs
from haversine import Unit
from app.models import Doctor, Medical_Center, Specialty


def findOptions(db, province, city, specialty, patient_insurer, patient_loc):
    options = []
    distances = []
    stmt = select(Medical_Center.province, Medical_Center.city, Medical_Center.address, Medical_Center.latitude, Medical_Center.longitude,
                  ).select_from(Medical_Center)

    results = db.execute(stmt)
    for row in results:
        lat = row[3]
        lon = row[4]
        distances.append(distance(lat, lon, patient_loc))

    max_val = max(distances)
    min_val = min(distances)

    results = db.execute(stmt)
    for row in results:  # additional info will be added to options
        options.append([row[0], row[1], findScore(row[0], row[1], distance(row[3], row[4], patient_loc), province, city, max_val, min_val), row[2]])

    sorted_options = sorted(options, key=lambda x: x[2], reverse=True)
    seen_first_parts = {}
    output_list = []
    for item in sorted_options:  # remove repetitive doctors
        first_part = item[0]
        # if first_part not in seen_first_parts:
        seen_first_parts[first_part] = True
        output_list.append(item)

    for item in output_list:
        print(item)
    db.close()
    return output_list


def distance(lat, lon, patient_loc) -> float:

    latitude = float(lat)
    longitude = float(lon)
    loc1 = (latitude, longitude)
    result = hs.haversine(loc1, patient_loc, unit=Unit.KILOMETERS)
    return result


def findScore(province, city, distance, patient_prov, patient_city, max_val, min_val):

    if province == patient_prov:
        x1 = 1
    else:
        x1 = 0
    if city == patient_city:
        x2 = 1
    else:
        x2 = 0
    # insurer remained

    x3 = (distance - min_val) / (max_val - min_val)

    score = 10*x1 + 1*x2 - 1*x3
    return score

