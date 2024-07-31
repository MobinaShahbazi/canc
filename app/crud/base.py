from idlelib.query import Query
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
            CRUD object with default methods to Create, Read, Update, Delete (CRUD).
            **Parameters**
            * `model`: A SQLAlchemy model class
            * `schema`: A Pydantic model (schema) class
        """

        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def create_bulk(self, db:Session,*,objs_in: List[CreateSchemaType]) -> List[ModelType]:
        result = []
        obj_in_data = jsonable_encoder(objs_in) # is it dict?
        doc_list = obj_in_data['values']
        for doctor in doc_list:
            db_obj = self.model(**doctor)
            result.append(db_obj)
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        resultDict = {}
        resultDict["values"] = result
        return resultDict

    def update(self, db: Session, *, obj_in: UpdateSchemaType) -> ModelType:

        obj_in_data = jsonable_encoder(obj_in, exclude_none=True)
        db_obj = self.get(db, obj_in_data['id'])

        if db_obj:
            for k, v in obj_in_data.items():
                setattr(db_obj, k, v)
            db.commit()
        else:
            raise HTTPException(status_code=404, detail='Doctor not found.')

        return None

    def delete_logical(self, db: Session, id: Any) -> List[ModelType]:
        db.query(self.model).filter(self.model.id == id).update({'deleted': True})
        db.commit()
        return None

    def filter_by(self, db: Session, skip: int = 0, limit: int = 100, **filters):
        return db.query(self.model).filter_by(**{k: v for k, v in filters.items() if v is not None}).offset(skip).limit(limit).all()


