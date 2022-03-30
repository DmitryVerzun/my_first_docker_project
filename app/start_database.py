from sqlalchemy import create_engine, Integer, Column, DateTime, String, ForeignKey, Table, update, delete
from sqlalchemy.orm import declarative_base, relationship, backref, sessionmaker

#not seen for some reason
#db_string = DATABASE_URL
dbase = declarative_base()

db_string = "postgresql://chibi:chibi_rules!@dbase:5432/hero_database_dev"
engine = create_engine(db_string)

confrontation = Table("confrontation", dbase.metadata,
    Column("hero_1_id", Integer, ForeignKey("hero.id"), primary_key=True),
    Column("hero_2_id", Integer, ForeignKey("hero.id"), primary_key=True),
    Column("hero_1_moto_id", Integer, ForeignKey("slogan.id")),
    Column("hero_2_moto_id", Integer, ForeignKey("slogan.id")),
    Column("winner", Integer)
)


class Hero(dbase):
    __tablename__ = "hero"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    side = Column(String(50))
    name = Column(String(30))
    birthday = Column(DateTime(timezone=True))
    race = Column(String(30))
    power = Column(Integer)

    slogans = relationship("Slogan", cascade="all, delete")
    #backstory = relationship("BackStory", cascade="all, delete")

#many-to-one with hero
class Slogan(dbase):
    __tablename__ = "slogan"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    moto = Column(String(100))

    #this is probably not very good
    moto_id = Column(Integer)

    hero_id = Column(Integer, ForeignKey("hero.id"))
    hero = relationship("Hero", foreign_keys=[hero_id])

#one-to-one with hero
class BackStory(dbase):
    __tablename__ = "backstory"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    story = Column(String(200))

    hero_id = Column(Integer, ForeignKey("hero.id"))
    hero = relationship("Hero", backref=backref("hero", uselist=False))

dbase.metadata.create_all(engine)
session_maker = sessionmaker(bind=engine)
session = session_maker()

#if __name__ == "__main__":
#    name = "hero_database_dev"
#    user = "chibi"
#    password = "chibi_rules!"
#    host = "postgres"  #?
#    port = "5432"
#    db_string = f"postgres://{name}:{user}@{password}:{host}/{port}"
#    db_string = DATABASE_URL
#    engine = create_engine(db_string)
#    Base = declarative_base()
#    Base.metadata.create_all(engine)