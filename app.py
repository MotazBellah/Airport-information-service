#!/usr/bin/env python3
from flask import (Flask, render_template, request,
                   redirect, url_for, jsonify, flash, abort)

from database_setup import searchIata, searchName

app = Flask(__name__)

@app.route('/iata/<iataCode>')
def iataSearch(iataCode):
    '''search iataCode and return the output in JSON form'''
    airports = searchIata(iataCode)
    if airports is None:
        abort(500)
    return jsonify(airports=[i for i in airports])


@app.route('/name/<name>')
def nameSearch(name):
    '''search name and return the output in JSON form'''
    airports = searchName(name)
    if airports is None:
        abort(500)
    return jsonify(airports=[i for i in airports])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
