import datetime
from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey, TypeDecorator, Float, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.association import association_table_I_MC


class Insurer(Base):
    __tablename__ = 'Insurer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    code = Column(String(255), unique=True)

    medical_centers = relationship("Medical_Center", secondary=association_table_I_MC, back_populates="insurers")
