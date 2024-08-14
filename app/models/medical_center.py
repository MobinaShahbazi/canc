import datetime
from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey, TypeDecorator, Float, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.association import association_table_D_MC, association_table_I_MC


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