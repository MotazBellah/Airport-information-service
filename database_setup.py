#!/usr/bin/env python3
import psycopg2
import json
from psycopg2.extras import RealDictCursor


def read_file():
    '''Read airports file and get the header'''
    f = open(r"airports.csv", 'r')
    fString = f.read()
    header = fString.split('\n')[0].split(',')
    return header


def connect_database(query):
    '''Connect to postgrelsql DB using psycopg2 DB-API '''
    try:
        pg = psycopg2.connect(dbname="airports")
        c = pg.cursor()
        c.execute(query)
        pg.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pg.close()


def create_table():
    '''Create a table '''
    # Use read file function
    header = read_file()
    # unpack the header into the table values
    createAirportTable = '''CREATE TABLE AIRPORTSDATA(
                         {} integer NOT NULL,
                         {} text,
                         {} text,
                         {} text,
                         {} real,
                         {} real,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text,
                         {} text
                         ) '''.format(*header)
    # connect to the database and run the query
    connect_database(createAirportTable)


def get_data(query, target):
    '''Connect to the database and fetch the data '''
    try:
        pg = psycopg2.connect(dbname="airports")
        # use the advantage of real dictionary cursor
        # to get a query output as json
        c = pg.cursor(cursor_factory=RealDictCursor)
        # Add the last comma to avoid the SQL injection
        c.execute(query, (target,))
        result = c.fetchall()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pg.close()

    return None


def searchIata(iataCode):
    '''Get the itatcode as a string variable and
    using SQL to search it from AIRPORT table'''
    # q = 'SELECT * FROM AIRPORT where iata_code ILIKE %s'
    query = '''SELECT name, iata_code as iata, gps_code, municipality as city,
            iso_country as country, longitude_deg as longitude
            , latitude_deg as latitude
            FROM AIRPORT where iata_code ILIKE %s'''
    return get_data(query, iataCode)


def searchName(name):
    '''Get the name as a string variable and
    using SQL to search it from AIRPORT table'''
    # q = "SELECT * FROM AIRPORT where position(lower(%s) in lower(name)) > 0"
    query = '''SELECT name, iata_code as iata, gps_code, municipality as city,
            iso_country as country, longitude_deg as longitude,
            latitude_deg as latitude
            FROM AIRPORT where position(lower(%s) in lower(name)) > 0'''
    return get_data(query, name)


if __name__ == '__main__':
    create_table()
