from sqlalchemy import Column, Integer, String, DateTime, Boolean, text, ARRAY, Table
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid
from typing import Optional, List
from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR

from app.db import Base

association_table = Table(
    "association_table",
    Base.metadata,
    Column("Health_Service_Center_id", ForeignKey("Health_Service_Center.id")),
    Column("Doctor_id", ForeignKey("Doctor.id")),
)
class Doctor(Base):
    __tablename__ = 'Doctor'
    __table_args__ = (UniqueConstraint('code', name='_unique_D_code'),)

    id: Mapped[str] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    lastname: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))           #should be removed
    phone: Mapped[str] = mapped_column(String(255))             #should be removed
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    specialty_id: Mapped[int] = mapped_column(ForeignKey("Specialty.id"))
    specialty: Mapped["Specialty"] = relationship(back_populates="doctors")

class Specialty(Base):
    __tablename__ = 'Specialty'

    id: Mapped[str] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    doctors: Mapped[List["Doctor"]] = relationship(back_populates="specialty")

class Health_Service_Center(Base):
    __tablename__ = 'Health_Service_Center'

    id: Mapped[str] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))  #enum

    province: Mapped[str] = mapped_column(String(255))
    district: Mapped[str] = mapped_column(String(255))
    city: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))

    phone: Mapped[str] = mapped_column(String(255))
    specialties: Mapped[List[str]] = mapped_column(ARRAY(String(255)))
    services: Mapped[List[str]] = mapped_column(ARRAY(String(255)))
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    doctors: Mapped[List["Doctor"]] = relationship(secondary=association_table)










