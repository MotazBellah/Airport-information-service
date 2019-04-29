from flask import (Flask, render_template, request,
                   redirect, url_for, jsonify, flash)

from database_setup import SearchIata, SearchName

app = Flask(__name__)

@app.route('/iata/<iataCode>')
def iataSearch(iataCode):
    # return iataCode
    airports = SearchIata(iataCode)
    return jsonify(airports=[i for i in airports])

@app.route('/name/<name>')
def nameSearch(name):
    # return iataCode
    airports = SearchName(name)
    return jsonify(airports=[i for i in airports])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
