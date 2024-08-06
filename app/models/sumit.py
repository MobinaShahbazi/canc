import json
import datetime

from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey, TypeDecorator, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db import Base

association_table_D_MC = Table(
    "association_table_D_MC",
    Base.metadata,
    Column("Medical_Center_id", ForeignKey("Medical_Center.id")),
    Column("Doctor_id", ForeignKey("Doctor.id")),
)

association_table_I_MC = Table(
    "association_table_I_MC",
    Base.metadata,
    Column("Medical_Center_id", ForeignKey("Medical_Center.id")),
    Column("Insurer_id", ForeignKey("Insurer.id")),
)

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

class Specialty(Base):
    __tablename__ = 'Specialty'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    code = Column(String(255), unique=True)
    description = Column(String(255))
    deleted = Column(Boolean, default=False)

    doctor_ids = relationship("Doctor", back_populates="specialty")

class Insurer(Base):
    __tablename__ = 'Insurer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    code = Column(String(255), unique=True)

    medical_centers = relationship("Medical_Center", secondary=association_table_I_MC, back_populates="insurers")

class Medical_Center(Base):
    __tablename__ = 'Medical_Center'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    province = Column(String(255))
    city = Column(String(255))
    address = Column(String(255))
    latitude = Column(String(255))
    longitude = Column(String(255))
    phone = Column(String(255))
    specialties = Column(ARRAY(String(255)))
    services = Column(ARRAY(String(255)))
    createTime = Column(DateTime, default=datetime.datetime.utcnow)
    lastModified = Column(DateTime, default=datetime.datetime.utcnow)
    enabled = Column(Boolean, default=True)
    deleted = Column(Boolean, default=False)

    # doctor_id = Column(Integer, ForeignKey('Doctor.id'))
    doctor_id = Column(Integer)  # shall be removed
    doctors = relationship("Doctor", secondary=association_table_D_MC, back_populates="workplaces")
    insurers = relationship("Insurer", secondary=association_table_I_MC, back_populates="medical_centers")










