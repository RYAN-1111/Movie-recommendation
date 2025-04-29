from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example: postgresql://username:password@localhost/dbname
# DATABASE_URL = "postgresql://postgres:user@localhost/ml_predictions"
DATABASE_URL ="postgresql://postgres:user@host.docker.internal/ml_predictions"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
