import os 
from dotenv import load_dotenv 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Get database URL from environment variable
DATABASE_URL = os.getenv("POSTGRES_CONNECTION_STRING", "sqlite:///./sql_app.db")

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    # Required for SQLite
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()