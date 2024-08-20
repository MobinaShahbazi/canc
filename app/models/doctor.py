import datetime
from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey, TypeDecorator, Float, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.association import association_table_D_MC


class Doctor(Base):
    __tablename__ = 'Doctor'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    lastname = Column(String(255))
    nezamCode = Column(String(255), unique=True)
    gender = Column(String(255))
    rate = Column(Float)
    createTime = Column(DateTime, default=datetime.datetime.utcnow)
    lastModified = Column(DateTime, default=datetime.datetime.utcnow)
    enabled = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)

    specialty_code = Column(String(255), ForeignKey('Specialty.code'))
    specialty = relationship("Specialty", back_populates="doctor_ids")
    workplaces = relationship("Medical_Center", secondary=association_table_D_MC, back_populates="doctors")
