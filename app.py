#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, abort
from database_setup import searchIata, searchName

app = Flask(__name__)


# Use errorhandler in flask to render custom HTML in case of error
@app.errorhandler(404)
def not_found(e):
    '''Return custom HTML page if page not founs '''
    return render_template('404.html')


@app.errorhandler(500)
def not_found(e):
    '''Return custom HTML page if server has error '''
    return render_template('500.html')


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
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
