from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    username=Config.DB_USER,
    password=Config.DB_PASS,
    database=Config.DB_NAME,
)

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
