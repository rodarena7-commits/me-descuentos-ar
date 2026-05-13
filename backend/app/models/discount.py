from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, Enum
from sqlalchemy.sql import func
import enum
from app.database import Base


class DiscountType(str, enum.Enum):
    descuento = "descuento"
    reintegro = "reintegro"
    promocion = "promocion"


class SourceType(str, enum.Enum):
    banco = "banco"
    fintech = "fintech"
    prepaga = "prepaga"


class Discount(Base):
    __tablename__ = "discounts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    discount_type = Column(String(20), nullable=False)  # descuento, reintegro, promocion
    percentage = Column(Float, nullable=True)           # % de descuento o reintegro
    max_amount = Column(Float, nullable=True)           # tope en pesos
    min_amount = Column(Float, nullable=True)           # monto mínimo de compra

    source = Column(String(100), nullable=False)        # Galicia, MercadoPago, etc.
    source_type = Column(String(20), nullable=False)    # banco, fintech, prepaga
    logo_url = Column(String(500), nullable=True)
    url = Column(String(500), nullable=True)            # link al banco/plataforma

    category = Column(String(100), nullable=True)       # supermercados, combustible, etc.
    days_of_week = Column(String(50), nullable=True)    # "lunes,martes" o "todos"

    valid_from = Column(DateTime, nullable=True)
    valid_until = Column(DateTime, nullable=True)

    is_limited_stock = Column(Boolean, default=False)   # hasta agotar stock
    is_new = Column(Boolean, default=True)              # nuevo (últimas 24hs)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
