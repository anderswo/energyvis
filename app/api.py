#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Data processing API
"""

import csv
import json

from app.database import db_session
from app.models import NrgSankey

from app import app
app.logger.info('Loading API...')


def get_data():
    """Wrapper function to get data"""
    return json_api_v1()


def load_nodes():
    """Function to load all the nodes
    :returns List of nodes as nested dictionary"""

    nodes = []
    with open("data/nodes_default.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")  # delimiter="\t"

        for index, line in enumerate(csvreader):
            if index == 0:  # header
                # print('Header: %s' % str(line))
                continue  # skip header
            nodes.append({'name': line[0]})

    return nodes


def load_links(geo='EU28', year=2015):
    """Build the links"""
    # year mapping for database query
    # ToDo: load from file: data/years.txt
    db_year = {
        2015: 'annual_data_2015',
        2014: 'annual_data_2014',
        2013: 'annual_data_2013',
        2012: 'annual_data_2012',
        2011: 'annual_data_2011',
        2010: 'annual_data_2010',
        2009: 'annual_data_2009',
        2008: 'annual_data_2008',
        2007: 'annual_data_2007',
        2006: 'annual_data_2006',
        2005: 'annual_data_2005',
        2004: 'annual_data_2004',
        2003: 'annual_data_2003',
        2002: 'annual_data_2002',
        2001: 'annual_data_2001',
        2000: 'annual_data_2000',
        1999: 'annual_data_1999',
        1998: 'annual_data_1998',
        1997: 'annual_data_1997',
        1996: 'annual_data_1996',
        1995: 'annual_data_1995',
        1994: 'annual_data_1994',
        1993: 'annual_data_1993',
        1992: 'annual_data_1992',
        1991: 'annual_data_1991',
        1990: 'annual_data_1990'
    }

    app.logger.info('Getting geo links...')
    nrg_query = db_session.query(NrgSankey)

    links = []
    with open("data/links_default.csv") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter=";")  # delimiter="\t"

        for index, line in enumerate(tsvreader):
            if index == 0:  # header
                # print('Header: %s' % str(line))
                continue  # skip header
            try:
                links.append({'source': line[0],
                              'target': line[1],
                              'value': nrg_query.filter_by(geo=geo,
                                                           product='0',
                                                           indicator=line[2]).first().__dict__[db_year[year]]
                              })
            except Exception as e:
                print('Error: %s' % e)
                app.logger.error('Error: %s' % e)

    return links


def json_api_v1(geo='DE', year=2015):
    """Return the data as json"""

    json_data_template = {
        'nodes': load_nodes(),
        'links': load_links(geo, year)
    }
    return json_data_template


def read_json_data():
    with open('data/example_data_json.json') as f:
        data = json.load(f)
        # print('Data: %s' % data)
        # print('Node: %s' % data['nodes'][1]['name'])
        return data


def read_csv_data():
    with open('data/example_data_DE_2015.csv') as f:
        # reader = csv.DictReader(f)
        reader = csv.reader(f)
        data_list = []
        for row in reader:
            # print(row)
            data_list.append(row)
        return data_list


def read_csv_data_as_dict():
    with open('data/example_data_DE_2015.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)


def read_file():
    with open('data/example_data_DE_2015.csv') as f:
        data_list = []
        for line in f.readlines():
            # print(line, end='', flush=True)
            data_list.append(line)
        return data_list


def read_file2():
    with open('data/example_data_DE_2015.csv') as f:
        data_list = []
        for line in f:
            data_list.append(line.rstrip('\n'))
        return data_list
