from typing import Type
from app.crud.base import CRUDBase
from sqlalchemy.orm import Session
from sqlalchemy import update
from .base import ModelType, UpdateSchemaType
from fastapi.encoders import jsonable_encoder
from app import models, schemas


class HeathServiceCenterCRUD(CRUDBase[models.Health_Service_Center, schemas.HelthServiceCenterCreate, schemas.HelthServiceCenterUpdete]):

    def get_by_code(self, db: Session, code) -> ModelType:
        return db.query(self.model).filter(self.model.code == code).first()




health_service_center_crud = HeathServiceCenterCRUD(models.Health_Service_Center)

