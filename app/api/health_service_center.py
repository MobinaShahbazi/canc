from fastapi import Depends
from sqlalchemy.orm import Session, Query
from app.dependencies import get_db
from datetime import datetime
from app import schemas, crud
from . import APIBaseClass


class HealthCenterDAO(APIBaseClass):

    def __init__(self):
        super().__init__()

        self.router.add_api_route('/MedicalCenter', self.get, methods=['GET'], tags=['Medical Center']) # when a GET request is made to the /workspaces path, the filter() method of the WorkspacesDAO class will be executed.
        self.router.add_api_route('/MedicalCenter/create', self.create, methods=['POST'], tags=['Medical Center'])
        self.router.add_api_route('/MedicalCenter/update', self.update, methods=['POST'], tags=['Medical Center'])
        self.router.add_api_route('/MedicalCenter/delete', self.delete, methods=['DELETE'], tags=['Medical Center'])

    def get(self, id, db: Session = Depends(get_db)):
        result = crud.health_service_center_crud.get(db=db, id=id)
        return result

    def create(self, request_body: schemas.HelthServiceCenterCreate, db: Session = Depends(get_db)):
        result = crud.health_service_center_crud.create(db=db, obj_in=request_body)
        return result

    def update(self, code, request_body: schemas.HelthServiceCenterUpdete, db: Session = Depends(get_db)):
        result = crud.health_service_center_crud.update(db=db, code=code, obj_in=request_body)
        return result

    def delete(self, id, db: Session = Depends(get_db)):
        result = crud.health_service_center_crud.delete_logical(db=db, id=id)
        return result

    def upsert_by_code(self, request_body: schemas.HelthServiceCenterUpdete, db: Session = Depends(get_db)):
        result = crud.health_service_center_crud.upsert_by_code(db=db, obj_in=request_body)
        return result

    def filter(self):
        pass
