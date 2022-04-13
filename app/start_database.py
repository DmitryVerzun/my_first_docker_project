from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
db_string = "postgresql+psycopg2://chibi:chibi_rules!@db:5432/hero_database_dev"
engine = create_engine(db_string)
Base.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)