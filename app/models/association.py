from sqlalchemy import Column, Integer, String, Boolean, ARRAY, Table, ForeignKey
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

