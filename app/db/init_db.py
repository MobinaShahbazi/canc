import pandas as pd
from sqlalchemy.orm import Session
from app import schemas
from app import crud

def init_Speciaity(db: Session) -> None:

    path = r'static\external\spe.xlsx'
    dataframe = pd.read_excel(path)
    dmn_model_files = []

    for i in range(693):  # 693
        code = dataframe.iloc[i, 1]
        title = dataframe.iloc[i, 2]
        description = dataframe.iloc[i, 3]
        record = {
            'code': str(code),
            'title': str(title),
            'description': str(description)
        }
        dmn_model_files.append(record)

    for dmn_model_file in dmn_model_files:
        dmn_in = schemas.specialty.SpecialtyCreate(**dmn_model_file)
        crud.specialty_crud.create(db=db, obj_in=dmn_in)

def init_Insurer(db: Session) -> None:

    path = r'static\external\insurance.xlsx'
    dataframe = pd.read_excel(path)
    dmn_model_files = []

    for i in range(78):  # 693
        code = dataframe.iloc[i, 1]
        name = dataframe.iloc[i, 2]
        record = {
            'code': str(code),
            'name': str(name),
        }
        dmn_model_files.append(record)

    for dmn_model_file in dmn_model_files:
        dmn_in = schemas.insurer.InsurerCreate(**dmn_model_file)
        crud.insurer_crud.create(db=db, obj_in=dmn_in)

def init_Doctor(db: Session) -> None:

    path = r'static\external\doctors_DoctorNext.xlsx'
    dataframe = pd.read_excel(path)
    na_df = dataframe.isna()
    # print(na_df)
    dmn_model_files = []

    for i in range(345):
        name = dataframe.iloc[i, 0]
        lastname = dataframe.iloc[i, 1]
        code = dataframe.iloc[i, 2]
        gender = dataframe.iloc[i, 3]
        if not na_df.iloc[i, 5]:
            rate = dataframe.iloc[i, 5]
        else:
            rate = 2.5
        specialty_id = dataframe.iloc[i, 6]
        record = {
            'name': str(name),
            'lastname': str(lastname),
            'nezamCode': str(code),
            'gender': str(gender),
            'rate': float(rate),
            'specialty_code': str(specialty_id)
        }
        dmn_model_files.append(record)

    for dmn_model_file in dmn_model_files:
        dmn_in = schemas.doctor.DoctorCreate(**dmn_model_file)
        crud.doctor_crud.create(db=db, obj_in=dmn_in)

def init_Medical_Center(db: Session) -> None:
    path = r'static\external\offices_DoctorNext.xlsx'
    dataframe = pd.read_excel(path)
    dmn_model_files = []

    for i in range(282):
        title = dataframe.iloc[i, 3]
        province = dataframe.iloc[i, 4]
        city = dataframe.iloc[i, 5]
        address = dataframe.iloc[i, 6]
        lat = dataframe.iloc[i, 7]
        lon = dataframe.iloc[i, 8]
        phone = dataframe.iloc[i, 9]
        doctor_id = dataframe.iloc[i, 2]  # change!!!!!!!!!!!!!!!!!
        record = {
            'title': str(title),
            'province': str(province),
            'city': str(city),
            'address': str(address),
            'latitude': str(lat),
            'longitude': str(lon),
            'phone': str(phone),
            'specialties': [],
            'services': [],
            'doctor_id': str(doctor_id)
        }
        dmn_model_files.append(record)

    for dmn_model_file in dmn_model_files:
        dmn_in = schemas.medical_center.MedicalCenterCreate(**dmn_model_file)
        crud.medical_center_crud.create(db=db, obj_in=dmn_in)