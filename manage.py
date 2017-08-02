#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module for managing the project"""

import csv
from app.database import init_db, import_energy_data


def create_database():
    """Wrapper function for database creation"""
    print('Creating database...')
    init_db()


def db_imports():
    """Import energy data into database"""
    import_energy_data()


def print_file(filepath):
    with open(filepath) as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")  # reader object
        for index, line in enumerate(tsvreader):
            if index == 0:  # header
                continue  # skip header
            print('%s, %s' % (line[0], line[1]))  # line[1:]


if __name__ == '__main__':
    import os
    from app import app

    print(os.path.abspath(os.path.dirname(__file__)))

    print('Debug Mode: %s' % app.config['DEBUG'])

    # print_file("data/geo.txt")

    init_db()
    import_energy_data()
