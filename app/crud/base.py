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

    def create_bulk(self, db:Session,*,objs_in: List[CreateSchemaType]) -> List[ModelType]:     #??
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

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

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

    def filter(self, db: Session,                     #///////
               model_class_list: list | None = None,
               filter_by_list: list | None = None,
               order_by_list: list | None = None,
               limit: int | None = None,
               offset: int | None = None):

        # taken from https://www.peterspython.com/en/blog/slqalchemy-dynamic-query-building-and-filtering-including-soft-deletes
        # TODO: This is not necessary right now but can be used to filter any entity

        fname = 'db_select'
        dbg_print = False

        if dbg_print:
            print(fname + ": len(model_class_list) = {}".format(len(model_class_list)))

        if filter_by_list == None:
            filter_by_list = []

        if order_by_list == None:
            order_by_list = []

        if not isinstance(model_class_list, list):
            raise Exception('model_class_list not list')
        if not isinstance(filter_by_list, list):
            raise Exception('filter_by_list not list')
        if not isinstance(order_by_list, list):
            raise Exception('order_by_list not list')

        # collector for model_classes
        mcs = []
        # collector for columns
        columns = []
        for model_class_item in model_class_list:
            if isinstance(model_class_item, tuple):
                m, key = model_class_item
                column = getattr(m, key, None)
                columns.append(column)
                mcs.append(m)
            else:
                columns.append(model_class_item)
                mcs.append(model_class_item)
        query = Query(columns)

        if dbg_print:
            print(fname + ": after creating query, query = {}".format(query))

        if dbg_print:
            # filter_by_items
            for filter_by_item in filter_by_list:
                print(fname + ": filter_by_item = {}".format(filter_by_item))
            # order_by_items
            for order_by_item in order_by_list:
                print(fname + ": order_by_item = {}".format(order_by_item))

        for filter_by_item in filter_by_list:
            if dbg_print:
                print(fname + ": processing filter_by_item = {}".format(filter_by_item))
            try:
                model_class, key, op, value = filter_by_item
            except ValueError:
                raise Exception('Invalid filter_by_item: %s' % filter_by_item)

            if dbg_print:
                print(fname + ": processing key, op, value = {}, {}, {}".format(key, op, value))

            column = getattr(model_class, key, None)
            if not column:
                raise Exception('Invalid filter column: %s' % key)

            if op == 'in':
                if isinstance(value, list):
                    filt = column.in_(value)
                else:
                    filt = column.in_(value.split(','))

                if dbg_print:
                    print(fname + ": if, filt = {}".format(filt))
            else:
                try:
                    attr = list(filter(
                        lambda e: hasattr(column, e % op),
                        ['%s', '%s_', '__%s__']
                    ))[0] % op
                except IndexError:
                    raise Exception('Invalid filter operator: %s' % op)

                if dbg_print:
                    print(fname + ": processing filter_cond, attr = {}".format(attr))

                if value == 'null':
                    value = None
                filt = getattr(column, attr)(value)

                if dbg_print:
                    print(fname + ": else, filt = {}".format(filt))

            if dbg_print:
                print(fname + ": adding filt")
            query = query.filter(filt)

        for order_by_item in order_by_list:
            if dbg_print:
                print(fname + ": processing order_by_item = {}".format(order_by_item))

            try:
                model_class, key, op = order_by_item
            except ValueError:
                raise Exception('Invalid order_by_item: %s' % order_by_item)

            if dbg_print:
                print(fname + ": processing model_class = {}, key = {}, op = {}".format(model_class, key, op))

            column = getattr(model_class, key, None)
            column_sorted = getattr(column, op)()
            query = query.order_by(column_sorted)

        if limit:
            if dbg_print:
                print(fname + ": processing limit = {}".format(limit))
            query = query.limit(limit)

        if offset:
            if dbg_print:
                print(fname + ": processing offset = {}".format(offset))
            query = query.offset(offset)

        if dbg_print:
            print(fname + ": after building query, query = {}".format(query))
        return query.with_session(db)