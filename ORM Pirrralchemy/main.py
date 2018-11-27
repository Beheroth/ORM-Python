from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MyElement(Base):
    __tablename__ = 'myelement'
    id = Column(Integer, primary_key = True)
    name = Column(String)

class Link(Base):
    __tablename__ = 'link'
    id = Column(Integer, primary_key=True)

    elem1_id = Column(Integer, ForeignKey('myelement.id'))
    elem1 = relationship(MyElement, backref=backref('links', uselist=True))

    elem2_id = Column(Integer, ForeignKey('myelement.id'))
    elem2 = relationship(MyElement, backref=backref('links', uselist=True))


from sqlalchemy import create_engine
engine = create_engine('sqlite:///')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
