from typing import Mapping, Union

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(bind=engine)()
Base = declarative_base()


class Band(Base):
    __tablename__ = 'band'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    musician = Column(Integer, ForeignKey('musician.id'))

    members = relationship("Musician", back_populates="bands", lazy=False)


class Musician(Base):
    __tablename__ = 'musician'

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    last_name = Column(String)
    instrument = Column(String)

    bands = relationship("Band", back_populates="members", lazy=False)

def create_tables() -> None:

    return Base.metadata.create_all(engine)

def get_fixtures() -> Mapping[str, Union[Band, Musician]]:
    create_tables()
    fixtures = {}

    band = Band(name='Band Of Gypsys', genre='Rock')

    fixtures['band'] = band

    musician = Musician(given_name='Jimi',
                        last_name='Hendrix',
                        instrument='Guitar')

    fixtures['musician'] = musician

    return fixtures


def get_fixtures_with_relationship() -> Mapping[str, Union[Band, Musician]]:
    fixtures = {}

    band = Band(name='Band Of Gypsys', genre='Rock')


    musician = Musician(given_name='Jimi',
                        last_name='Hendrix',
                        instrument='Guitar',
                        bands=[band])


    session.add_all([band, musician])
    session.commit()

    fixtures['band'] = session.query(Band).first()
    fixtures['musician'] = session.query(Musician).first()

    return fixtures
