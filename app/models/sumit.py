from sqlalchemy import Column, Integer, String, DateTime, Boolean, text
from sqlalchemy import ForeignKeyConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid
from typing import Optional, List
from sqlalchemy import Column, String, UniqueConstraint
from sqlalchemy.dialects.mysql import CHAR

from app.db import Base


class Doctor(Base):
    __tablename__ = 'Doctor'

    id = Column(Integer, primary_key=True)

    # UUID(as_uuid=False), primary_key=True, index=True, default=uuid.uuid4
    name = Column(String(255), default='unnamed workspace')
    lastname = Column(String(255))
    specialization = Column(String(255))
    code = Column(String(255))
    description = Column(String(255), nullable=True)
    address = Column(String(255))
    phone = Column(String(255))

    __table_args__ = (
        UniqueConstraint('code', name='_unique_ws_code'),
    )

    # ws_data_records: Mapped[List['WSData']] = relationship()




