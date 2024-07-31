import pandas as pd

from sqlalchemy.orm import Session
from app import schemas
from fastapi import Depends
from app.dependencies import get_db
from app import crud

def init_db(db: Session) -> None:

    path = r'E:\term6\internship\Projects\temp\spe.xlsx'
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
