from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from numpy import genfromtxt
from datetime import datetime
from consumption import Consumption
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import config

Base = declarative_base()

bd = 'consumption'

engine = create_engine('mysql://{}:{}@{}:3306/{}'.format(config.user, config.password, config.url, bd))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

Consumption.__table__.create(engine)

data = pd.read_csv('src\CCEE_BR_Data_original_edited.csv')

for index, row in data.iterrows():
    record = Consumption(**{
        'data' : datetime.strptime(row[0], '%d/%M/%Y').date(),
        'classe' : row[1],
        'ramo' : row[2],
        'submercado' : row[3],
        'uf' : row[4],
        'consumo' : row[5],
        'covid' : row[6]
    })
    session.add(record)

    session.commit()