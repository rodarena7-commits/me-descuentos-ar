from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import Optional, List
from datetime import datetime, timedelta

from app.database import get_db
from app.models.discount import Discount
from app.schemas.discount import DiscountResponse

router = APIRouter(prefix="/api/discounts", tags=["discounts"])


@router.get("/", response_model=List[DiscountResponse])
def get_discounts(
    discount_type: Optional[str] = Query(None),
    source: Optional[str] = Query(None),
    source_type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    is_limited_stock: Optional[bool] = Query(None),
    is_new: Optional[bool] = Query(None),
    expiring_soon: Optional[bool] = Query(None),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    query = db.query(Discount).filter(Discount.is_active == True)

    if discount_type:
        query = query.filter(Discount.discount_type == discount_type)
    if source:
        query = query.filter(Discount.source.ilike(f"%{source}%"))
    if source_type:
        query = query.filter(Discount.source_type == source_type)
    if category:
        query = query.filter(Discount.category.ilike(f"%{category}%"))
    if is_limited_stock is not None:
        query = query.filter(Discount.is_limited_stock == is_limited_stock)
    if is_new:
        since = datetime.utcnow() - timedelta(hours=24)
        query = query.filter(Discount.created_at >= since)
    if expiring_soon:
        in_3_days = datetime.utcnow() + timedelta(days=3)
        query = query.filter(
            and_(Discount.valid_until != None, Discount.valid_until <= in_3_days)
        )

    return query.order_by(Discount.created_at.desc()).offset(skip).limit(limit).all()


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Discount).filter(Discount.is_active == True).count()
    new_today = db.query(Discount).filter(
        Discount.created_at >= datetime.utcnow() - timedelta(hours=24),
        Discount.is_active == True,
    ).count()
    expiring_soon = db.query(Discount).filter(
        Discount.valid_until <= datetime.utcnow() + timedelta(days=3),
        Discount.valid_until != None,
        Discount.is_active == True,
    ).count()
    limited_stock = db.query(Discount).filter(
        Discount.is_limited_stock == True, Discount.is_active == True
    ).count()

    return {
        "total": total,
        "new_today": new_today,
        "expiring_soon": expiring_soon,
        "limited_stock": limited_stock,
    }


@router.get("/sources")
def get_sources(db: Session = Depends(get_db)):
    sources = db.query(Discount.source, Discount.source_type, Discount.logo_url).filter(
        Discount.is_active == True
    ).distinct().all()
    return [{"source": s[0], "source_type": s[1], "logo_url": s[2]} for s in sources]


@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    cats = db.query(Discount.category).filter(
        Discount.is_active == True, Discount.category != None
    ).distinct().all()
    return [c[0] for c in cats if c[0]]


@router.get("/{discount_id}", response_model=DiscountResponse)
def get_discount(discount_id: int, db: Session = Depends(get_db)):
    return db.query(Discount).filter(Discount.id == discount_id).first()
