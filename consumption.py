from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Consumption(Base):
    __tablename__ = 'consumptions'

    id = Column(Integer, primary_key=True, nullable=False)
    data = Column(Date)
    classe = Column(String(50))
    ramo = Column(String(50))
    submercado = Column(String(50))
    uf = Column(String(50))
    consumo = Column(Float)
    covid = Column(String(50))


