from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker

engine = create_engine("postgresql://postgres.antrcpgodmulkouibwrj:ryTTynY8PYdTq1OR@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres")

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)

Base = declarative_base()

def get_database():
    db = SessionLocal()
    try : 
        yield db 
    finally : 
        db.close()