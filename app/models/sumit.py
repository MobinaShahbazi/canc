import json

from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey, TypeDecorator
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db import Base

association_table = Table(
    "association_table",
    Base.metadata,
    Column("Health_Service_Center_id", ForeignKey("Health_Service_Center.id")),
    Column("Doctor_id", ForeignKey("Doctor.id")),
)

class Doctor(Base):
    __tablename__ = 'Doctor'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    lastname = Column(String(255))
    code = Column(String(255), unique=True)
    description = Column(String(255))
    specialty_id = Column(Integer, ForeignKey('Specialty.id'))  # ForeignKey relationship to Specialty
    deleted = Column(Boolean, default=False)
    # Relationship with Health_Service_Center through association_table
    workplaces = relationship("Health_Service_Center", secondary=association_table, back_populates="doctors")

class Specialty(Base):
    __tablename__ = 'Specialty'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    code = Column(String(255), unique=True)
    description = Column(String(255))
    deleted = Column(Boolean, default=False)

class Health_Service_Center(Base):
    __tablename__ = 'Health_Service_Center'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    province = Column(String(255))
    district = Column(String(255))
    city = Column(String(255))
    address = Column(String(255))
    latitude = Column(String(255))
    longitude = Column(String(255))
    phone = Column(String(255))
    specialties = Column(ARRAY(String(255)))
    services = Column(ARRAY(String(255)))
    deleted = Column(Boolean, default=False)

    # Relationship with Doctor through association_table
    doctor_id = Column(Integer, ForeignKey('Doctor.id'))
    doctors = relationship("Doctor", secondary=association_table, back_populates="workplaces")









