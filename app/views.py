import csv
import os

from app import app
from flask import render_template
from flask import jsonify
from flask import request
from flask import send_from_directory

from app.api import json_api_v1

app.logger.info('Loading views...')


def get_geo_list():
    geo_list = []

    try:
        with open("data/geo.txt") as f:
            for index, row in enumerate(csv.reader(f, delimiter="\t")):
                if index == 0:  # header
                    continue  # skip header
                geo_list.append(row[0])
    except IOError as e:
        app.logger.error('File access error: %s', (request.path, e))
        print('error: %s' % e.strerror)
        geo_list = ['EU28', 'DE']
    return geo_list


def get_year_list():
    year_list = []

    try:
        with open("data/years.txt") as f:
            reader = csv.reader(f, delimiter=";")  # csv.reader object
            for row in reader:
                year_list.append(int(row[0]))
    except IOError as e:
        app.logger.error('File access error: %s', (request.path, e))
        year_list = [2015, 2014, 2013]

    return year_list


@app.route("/", methods=['GET'])
@app.route("/index", methods=['GET'])
def index():
    # set entries for geo (dropdown menue) and year (radio button)
    geo_list = get_geo_list()
    year_list = get_year_list()  # get_year_list()

    # get data from the query string (e.g. /?geo=EU28&year=2015)
    query_string = request.args.to_dict()
    # query_string = request.args.lists()

    # set standard data
    if not 'geo' in query_string:
        query_string = {'geo': 'EU28', 'year': 2015}

    # get headline
    headline = query_string['geo'] + ', ' + str(query_string['year'])

    return render_template("index.html",
                           headline=headline,
                           geo_list=geo_list,
                           year_list=year_list)


@app.route("/api/v1.0/json", methods=['GET'])
def energy_json():
    # get query string from route: /api/v1.0/json
    query_string = request.args.to_dict()

    # set default values if nothing is specified
    # (/api/v1.0/json?geo=EU28&year=2015)
    if not 'geo' in query_string:
        query_string = {'geo': 'EU28', 'year': 2015}
        print('Set standard data: %s, %s' % (query_string['geo'],
                                             query_string['year']))

    return jsonify(json_api_v1(geo=query_string['geo'],
                               year=int(query_string['year'])))


@app.route("/meta")
def admin():
    headline = 'Site metadata'
    metadata = []
    metadata.append('Settings: %s' % str(app.config['NAME']))
    metadata.append('Debug Mode: %s' % str(app.config['DEBUG']))
    metadata.append('Database: %s' % str(app.config['DATABASE_URI']))
    metadata.append('App Config: %s' % app.config.items())
    return render_template('meta.html', metadata=metadata, headline=headline)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
