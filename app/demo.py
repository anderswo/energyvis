""" Demo views
Views for demonstration purposes
"""

from app import app

from flask import render_template
from flask import jsonify
from flask import Response
from flask import request

from app.api import read_json_data
from app.api import read_csv_data
from app.api import read_csv_data_as_dict
from app.api import read_file

from app.models import NrgSankey


@app.route("/api/demo/json", methods=['GET'])
def json_data():
    return jsonify(read_json_data())


@app.route("/api/demo/csv")
def csv_data():
    return str(read_csv_data())


@app.route("/api/demo/csvdict")
def csv_data_dict():
    return str(read_csv_data_as_dict())


@app.route("/api/demo/file")
def file_data():
    return Response(read_file())


@app.route("/api/demo/db")
def energy_data():
    """Return all energy data"""
    dataset = NrgSankey.query.all()  # returns a list
    return render_template("db.html", data=dataset)


@app.route("/api/demo/db2")
def energy_selection():
    """Energy selection"""
    from app.database import db_session

    # returns an object with .first() and a list with .all()
    dataset = db_session.query(NrgSankey).filter_by(geo='DE',
                                                    product='2000',
                                                    indicator='B_100100'
                                                    ).all()

    db_session.remove()
    return render_template("db.html", data=dataset)


@app.route("/api/demo/json2")
def jsondemo():
    from app.database import db_session

    # returns an object with .first() and a list with .all()
    dataset = db_session.query(NrgSankey).filter_by(geo='DE',
                                                    product='2000',
                                                    indicator='B_100100'
                                                    ).first()

    db_session.remove()
    return jsonify(source='Primary production',
                   target='Production',
                   value=dataset.annual_data_2015)


@app.route("/formdemo", methods=['GET', 'POST'])
def form_demo():
    if request.method == 'POST':
        print('Post Method')
        form_data = request.form['geo_list']
        print(form_data)
        return form_data

    form_data_get = request.form['geo_list']
    print(form_data_get)
    return form_data_get
