from flask import (Flask, render_template, request,
                   redirect, url_for, jsonify, flash)

from database_setup import SearchIata

app = Flask(__name__)

@app.route('/<iataCode>')
def iataSearch(iataCode):
    # return iataCode
    x = SearchIata(iataCode)
    return jsonify(x=[i for i in x])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
