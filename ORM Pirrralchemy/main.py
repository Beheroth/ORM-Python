from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import urllib.parse


Base = declarative_base()

class MyElement(Base):
    __tablename__ = 'MyElement'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<MyElement(name='%s')>" % self.name



class Link(Base):
    __tablename__ = 'Link'
    id = Column(Integer, primary_key=True)

    elem1_id = Column(Integer, ForeignKey('MyElement.id'))
    elem1 = relationship("MyElement", foreign_keys=[elem1_id])

    elem2_id = Column(Integer, ForeignKey('MyElement.id'))
    elem2 = relationship("MyElement", foreign_keys=[elem2_id])

    result_id = Column(Integer, ForeignKey('MyElement.id'))
    result = relationship("MyElement", foreign_keys=[result_id])




class DBManager():
    server = "LAPTOP-40BAE1KO\SQLEXPRESS"
    database = "Pirrralchemy"
    params = urllib.parse.quote_plus("DRIVER={};"
                                     "SERVER={};"
                                     "DATABASE={};"
                                     "Trusted_Connection=yes".format("SQL Server Native Client 11.0", server, database))

    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        Base.metadata.create_all(self.engine)

    def querying(self):
        print("MyElement")
        for instance in self.session.query(MyElement).order_by(MyElement.id):
            print("  " + instance.name)

        print("Link")
        for instance in self.session.query(Link).order_by(Link.id):
            print("  " + instance.elem1, instance.elem2, instance.result)

    def populate(self):
        water = MyElement(name='water')
        earth = MyElement(name='earth')
        mud = MyElement(name='mud')

        self.session.add(water)
        self.session.add(earth)
        self.session.add(mud)

        monlien = Link(elem1_id=water, elem2_id=earth, result_id=mud)



dbm = DBManager()
dbm.querying()



