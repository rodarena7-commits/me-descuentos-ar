from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys
from dotenv import load_dotenv

load_dotenv()

_SQLITE_DEFAULT = "sqlite:///./descuentos.db"

DATABASE_URL = os.getenv("DATABASE_URL", _SQLITE_DEFAULT)

# Render provee postgres:// pero SQLAlchemy 2.x requiere postgresql://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Validar la URL; si es inválida caer a SQLite y loguear el problema
try:
    make_url(DATABASE_URL)
except Exception:
    print(
        f"[DB] DATABASE_URL inválida (primeros 40 chars): {DATABASE_URL[:40]!r} "
        "— usando SQLite local como fallback.",
        file=sys.stderr,
    )
    DATABASE_URL = _SQLITE_DEFAULT

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
