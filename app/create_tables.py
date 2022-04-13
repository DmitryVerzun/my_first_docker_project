from sqlalchemy import Integer, Column, DateTime, String, ForeignKey, Table, update
from sqlalchemy.orm import relationship, backref

from start_database import Base

#not seen for some reason
#db_string = DATABASE_URL


confrontation = Table("confrontation", Base.metadata,
    Column("hero_1_id", Integer, ForeignKey("hero.id"), primary_key=True),
    Column("hero_2_id", Integer, ForeignKey("hero.id"), primary_key=True),
    Column("hero_1_moto_id", Integer, ForeignKey("slogan.id")),
    Column("hero_2_moto_id", Integer, ForeignKey("slogan.id")),
    Column("winner", Integer), extend_existing=True
)


class Hero(Base):
    __tablename__ = "hero"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    side = Column(String(50))
    name = Column(String(30))
    birthday = Column(DateTime(timezone=True))
    race = Column(String(30))
    power = Column(Integer)

    slogans = relationship("Slogan", back_populates="hero_slog", passive_deletes=True)
    #backstory = relationship("BackStory", cascade="all, delete")

#many-to-one with hero
class Slogan(Base):
    __tablename__ = "slogan"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    moto = Column(String(250))

    #this is probably not very good
    moto_id = Column(Integer)

    hero_id = Column(Integer, ForeignKey("hero.id", ondelete="CASCADE"))
    hero_slog = relationship("Hero", backref=backref("hero_slog"), cascade="all, delete")
 #   hero_slog=relationship ("Hero", back_populates="slogans", cascade="all, delete")
 #   hero = relationship("Hero", back_populates="slogans")

#one-to-one with hero
class BackStory(Base):
    __tablename__ = "backstory"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    story = Column(String(200))

    hero_id = Column(Integer, ForeignKey("hero.id", ondelete="CASCADE"))
    hero = relationship("Hero", backref=backref("hero", uselist=False), cascade="all, delete")