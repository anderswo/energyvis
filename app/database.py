#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Database

Python console database setup
==============================

Create DB
-----------------------------
import app.database as db
db.init_db()


Query
-----------------------------
from app.models import NrgSankey
dataset = NrgSankey.query.all()
for item in dataset: print(item)


Reload
-----------------------------
from importlib import reload
reload(db)

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app import app

engine = create_engine(app.config['DATABASE_URI'],
                       convert_unicode=True, echo=False)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

app.logger.info('Loaded database engine, session and base')


def init_db():
    """Create a new database"""
    # import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise
    # you will have to import them first before calling init_db()
    print('Importing database models...')
    import app.models
    print('Creating new database: %s...' % engine.name)
    Base.metadata.create_all(bind=engine)


def float_check(value):
    """Check if value can be converted into float.
    If not return 0. The energy dataset contains ":" for datapoints where
    no data is present.
    """
    try:
        val = float(value)
        return val
    except ValueError as e:
        return 0


def import_energy_data():
    """Import energy data into database"""
    from app.models import NrgSankey
    import csv

    print('Starting data import...')

    with open("data/nrg_sankey.csv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")  # delimiter="\t"

        for index, line in enumerate(tsvreader):
            if index == 0:  # header
                print('Header: %s' % str(line))
                continue  # skip header

            data = NrgSankey(unit=line[0],
                             product=line[1],
                             indicator=line[2],
                             geo=line[3],
                             annual_data_2015=float_check(line[4]),
                             annual_data_2014=float_check(line[5]),
                             annual_data_2013=float_check(line[6]),
                             annual_data_2012=float_check(line[7]),
                             annual_data_2011=float_check(line[8]),
                             annual_data_2010=float_check(line[9]),
                             annual_data_2009=float_check(line[10]),
                             annual_data_2008=float_check(line[11]),
                             annual_data_2007=float_check(line[12]),
                             annual_data_2006=float_check(line[13]),
                             annual_data_2005=float_check(line[14]),
                             annual_data_2004=float_check(line[15]),
                             annual_data_2003=float_check(line[16]),
                             annual_data_2002=float_check(line[17]),
                             annual_data_2001=float_check(line[18]),
                             annual_data_2000=float_check(line[19]),
                             annual_data_1999=float_check(line[20]),
                             annual_data_1998=float_check(line[21]),
                             annual_data_1997=float_check(line[22]),
                             annual_data_1996=float_check(line[23]),
                             annual_data_1995=float_check(line[24]),
                             annual_data_1994=float_check(line[25]),
                             annual_data_1993=float_check(line[26]),
                             annual_data_1992=float_check(line[27]),
                             annual_data_1991=float_check(line[28]),
                             annual_data_1990=float_check(line[29]))
            db_session.add(data)

    print('Changes...')
    print(db_session.dirty)
    print(db_session.new)
    print(db_session.identity_map)

    print('Committing changes...')
    db_session.commit()
    print('Imported Data into database')
    db_session.remove()  # close session


def print_energy_data():
    from app.models import NrgSankey

    dataset = db_session.query(NrgSankey).all()

    for instance in dataset:
        print(instance.id,
              instance.geo,
              instance.indicator,
              instance.annual_data_2015)

    db_session.remove()


def print_energy_entries():
    from app.models import NrgSankey

    # returns a list
    dataset = db_session.query(NrgSankey).filter_by(geo='DE',
                                                    product='0',
                                                    indicator='B_100100').all()

    for instance in dataset:
        print(instance.id,
              instance.geo,
              instance.indicator,
              instance.annual_data_2015)

    print(type(dataset))
    db_session.remove()


def print_energy_entry():
    from app.models import NrgSankey

    # returns an object
    dataset = db_session.query(NrgSankey).filter_by(geo='DE',
                                                    product='2000',
                                                    indicator='B_100100'
                                                    ).first()
    print('%s %s' % ('Value:', dataset.annual_data_2015))
    print(dataset)

    print(type(dataset))
    db_session.remove()


print('Register database application functions...')
app.logger.info('Register database application functions...')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
    app.logger.debug('teardown_appcontext...')


if __name__ == '__main__':
    import os
    print(os.path.abspath(os.path.dirname(__file__)))
