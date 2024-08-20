from typing import Type
from app.crud.base import CRUDBase
from sqlalchemy.orm import Session
from sqlalchemy import update
from .base import ModelType, UpdateSchemaType
from fastapi.encoders import jsonable_encoder
from app import models, schemas


class MedicalCenterCRUD(CRUDBase[models.Medical_Center, schemas.MedicalCenterCreate, schemas.MedicalCenterUpdete]):

    def get_by_code(self, db: Session, code) -> ModelType:
        return db.query(self.model).filter(self.model.code == code).first()




medical_center_crud =MedicalCenterCRUD(models.Medical_Center)

