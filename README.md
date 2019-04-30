## Airport-information-service

web service that provides information about airports based on http://ourairports.com/data/

## Code style

This project is written in python 3 and follow PEP-8 Guidelines.

## Database Installation

First download airports.csv from http://ourairports.com/data/ or use the file in the repo.
Use docker, vagrant (VM server) or a real server to run the following commands:

1. Run `psql`  on terminal to start coding in SQL.

2. Run `CREATE DATABASE AIRPORTS` to create airports DB.

3. Exit the SQL environment by ctrl + d.

4. Run `python database_setup.py` to create AIRPORTSDATA table.

5. Run `psql airports` command to update the database.

6. Run `\COPY AIRPORTSDATA from airports.csv DELIMITER ',' CSV HEADER`, to copy the data from airports file to AIRPORTSDATA table.

7. Run `CREATE TABLE AIRPORT AS SELECT * FROM AIRPORTSDATA WHERE iata_code IS NOT NULL` to get the only the airports that have an IATA code.

8. Exit the SQL environment by ctrl + d.

## Run

Run `python app.py` to start the application

## Endpoint URLs

### IATA search

`http://localhost:8000/iata/<iataCode>/JSON`, where `<iataCode>` is a string variable
for example http://localhost:8000/iata/sfx/JSON

### Name search

`http://localhost:8000/name/<name>/JSON`, where `<name>` is a string variable
for example http://localhost:8000/name/berlin/JSON
