from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey, TypeDecorator, Float, DateTime
from sqlalchemy.orm import relationship
from app.db import Base


class Specialty(Base):
    __tablename__ = 'Specialty'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    code = Column(String(255), unique=True)
    description = Column(String(255))
    deleted = Column(Boolean, default=False)

    doctor_ids = relationship("Doctor", back_populates="specialty")
