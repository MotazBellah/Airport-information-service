#!/usr/bin/env python3
from flask import Flask, render_template, jsonify, abort, make_response
from database_setup import searchIata, searchName

app = Flask(__name__)


# Use errorhandler in flask to render custom HTML in case of error
@app.errorhandler(404)
def not_found(e):
    '''Return custom JSON if page not founs '''
    return jsonify(code=e.code, message=str(e),
                   reason='Page Not Found, or Server Not Found',
                   action='Please check the URL'), 404


@app.errorhandler(500)
def not_found(e):
    '''Return custom HTML page if server has error '''
    return jsonify(code=e.code, message=str(e),
                   reason='''The server encountered an unexpected condition
                          which prevented it from fulfilling the request,
                          or the server is overloaded''',
                   action='''Please come back later
                          when we fixed that problem.'''), 500


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
