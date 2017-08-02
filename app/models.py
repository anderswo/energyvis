""" Database models
"""

from sqlalchemy import Column, Integer, Float, String
# to create database models subclass Base from app.database
from app.database import Base

from app import app
app.logger.info('Loading models...')


class NrgSankey(Base):
    __tablename__ = 'nrgsankey'

    id = Column(Integer, primary_key=True)

    annual_data_2015 = Column(Float, unique=False)
    annual_data_2014 = Column(Float, unique=False)
    annual_data_2013 = Column(Float, unique=False)
    annual_data_2012 = Column(Float, unique=False)
    annual_data_2011 = Column(Float, unique=False)
    annual_data_2010 = Column(Float, unique=False)
    annual_data_2009 = Column(Float, unique=False)
    annual_data_2008 = Column(Float, unique=False)
    annual_data_2007 = Column(Float, unique=False)
    annual_data_2006 = Column(Float, unique=False)
    annual_data_2005 = Column(Float, unique=False)
    annual_data_2004 = Column(Float, unique=False)
    annual_data_2003 = Column(Float, unique=False)
    annual_data_2002 = Column(Float, unique=False)
    annual_data_2001 = Column(Float, unique=False)
    annual_data_2000 = Column(Float, unique=False)
    annual_data_1999 = Column(Float, unique=False)
    annual_data_1998 = Column(Float, unique=False)
    annual_data_1997 = Column(Float, unique=False)
    annual_data_1996 = Column(Float, unique=False)
    annual_data_1995 = Column(Float, unique=False)
    annual_data_1994 = Column(Float, unique=False)
    annual_data_1993 = Column(Float, unique=False)
    annual_data_1992 = Column(Float, unique=False)
    annual_data_1991 = Column(Float, unique=False)
    annual_data_1990 = Column(Float, unique=False)

    unit = Column(String(50), unique=False)
    product = Column(String(50), unique=False)
    indicator = Column(String(50), unique=False)
    geo = Column(String(50), unique=False)

    def __init__(self, unit=None, product=None, indicator=None, geo=None,
                 annual_data_2015=None, annual_data_2014=None,
                 annual_data_2013=None, annual_data_2012=None,
                 annual_data_2011=None, annual_data_2010=None,
                 annual_data_2009=None, annual_data_2008=None,
                 annual_data_2007=None, annual_data_2006=None,
                 annual_data_2005=None, annual_data_2004=None,
                 annual_data_2003=None, annual_data_2002=None,
                 annual_data_2001=None, annual_data_2000=None,
                 annual_data_1999=None, annual_data_1998=None,
                 annual_data_1997=None, annual_data_1996=None,
                 annual_data_1995=None, annual_data_1994=None,
                 annual_data_1993=None, annual_data_1992=None,
                 annual_data_1991=None, annual_data_1990=None):
        self.unit = unit
        self.product = product
        self.indicator = indicator
        self.geo = geo
        self.annual_data_2015 = annual_data_2015
        self.annual_data_2014 = annual_data_2014
        self.annual_data_2013 = annual_data_2013
        self.annual_data_2012 = annual_data_2012
        self.annual_data_2011 = annual_data_2011
        self.annual_data_2010 = annual_data_2010
        self.annual_data_2009 = annual_data_2009
        self.annual_data_2008 = annual_data_2008
        self.annual_data_2007 = annual_data_2007
        self.annual_data_2006 = annual_data_2006
        self.annual_data_2005 = annual_data_2005
        self.annual_data_2004 = annual_data_2004
        self.annual_data_2003 = annual_data_2003
        self.annual_data_2002 = annual_data_2002
        self.annual_data_2001 = annual_data_2001
        self.annual_data_2000 = annual_data_2000
        self.annual_data_1999 = annual_data_1999
        self.annual_data_1998 = annual_data_1998
        self.annual_data_1997 = annual_data_1997
        self.annual_data_1996 = annual_data_1996
        self.annual_data_1995 = annual_data_1995
        self.annual_data_1994 = annual_data_1994
        self.annual_data_1993 = annual_data_1993
        self.annual_data_1992 = annual_data_1992
        self.annual_data_1991 = annual_data_1991
        self.annual_data_1990 = annual_data_1990
