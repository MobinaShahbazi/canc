from sqlalchemy.orm import Session
from app import crud, schemas
from fastapi import Depends
from app.dependencies import get_db


def init_db(db: Session) -> None:

    dmn_model_files = [{
        'name': 'ali',
        'lastname': 'alavi',
        'specialization': 'genetic',
        'code': '12345',
        'description': 'description1/description1/description1',
        'address': 'teranpars',
        'phone': '0912'
    },
        {
        'name': 'taghi',
        'lastname': 'taghavi',
        'specialization': 'general',
        'code': '6789',
        'description': 'description2/description2/descriptio2n',
        'address': 'gharb',
        'phone': '0936'
    }
    ]

    for dmn_model_file in dmn_model_files:
        dmn_in = schemas.dmn_models.DMNModelCreate(**dmn_model_file)
        crud.dmn_crud.create(db=db, obj_in=dmn_in)