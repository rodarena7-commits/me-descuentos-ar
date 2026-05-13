from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DiscountBase(BaseModel):
    title: str
    description: Optional[str] = None
    discount_type: str
    percentage: Optional[float] = None
    max_amount: Optional[float] = None
    min_amount: Optional[float] = None
    source: str
    source_type: str
    logo_url: Optional[str] = None
    url: Optional[str] = None
    category: Optional[str] = None
    days_of_week: Optional[str] = None
    valid_from: Optional[datetime] = None
    valid_until: Optional[datetime] = None
    is_limited_stock: bool = False
    is_new: bool = True
    is_active: bool = True


class DiscountCreate(DiscountBase):
    pass


class DiscountResponse(DiscountBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class DiscountFilter(BaseModel):
    discount_type: Optional[str] = None
    source: Optional[str] = None
    source_type: Optional[str] = None
    category: Optional[str] = None
    is_limited_stock: Optional[bool] = None
    is_new: Optional[bool] = None
    expiring_soon: Optional[bool] = None  # vence en los próximos 3 días
