from fastapi import Depends
from sqlalchemy.orm import Session, Query
from app.dependencies import get_db
from datetime import datetime
from app import schemas, crud
from . import APIBaseClass


class DoctorDAO(APIBaseClass):

    def __init__(self):
        super().__init__()

        self.router.add_api_route('/Doctor', self.get, methods=['GET']) # when a GET request is made to the /workspaces path, the filter() method of the WorkspacesDAO class will be executed.
        self.router.add_api_route('/Doctor/create', self.create, methods=['POST'])
        self.router.add_api_route('/Doctor/create_bulk', self.create_bulk, methods=['POST'])
        self.router.add_api_route('/Doctor/update', self.update, methods=['POST'])
        self.router.add_api_route('/Doctor/delete', self.delete, methods=['DELETE']) 

    def get(self, id, db: Session = Depends(get_db)):
        result = crud.doctor_crud.get(db=db, id=id)
        return result

    def create(self, request_body: schemas.DoctorCreate, db: Session = Depends(get_db)):
        result = crud.doctor_crud.create(db=db, obj_in=request_body)
        return result

    def create_bulk(self, request_body: schemas.DoctorCreateBulk, db: Session = Depends(get_db) ):
        result = crud.doctor_crud.create_bulk(db=db, objs_in=request_body)
        return result

    def update(self, code, request_body: schemas.DoctorUpdate, db: Session = Depends(get_db)):
        result = crud.doctor_crud.update(db=db, code=code, obj_in=request_body)
        return result

    def delete(self, id, db: Session = Depends(get_db)):
        result = crud.doctor_crud.delete_logical(db=db, id=id)
        return result

    def upsert_by_code(self, request_body: schemas.DoctorUpdate, db: Session = Depends(get_db)):
        result = crud.doctor_crud.upsert_by_code(db=db, obj_in=request_body)
        return result

    def filter(self):
        pass
