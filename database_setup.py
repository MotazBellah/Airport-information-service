#!/usr/bin/env python3
import psycopg2
import json
from psycopg2.extras import RealDictCursor

def read_file():
    '''Read airports file and get the header'''
    f = open(r"airports.csv", 'r')
    fString = f.read()
    fList = []
    header = fString.split('\n')[0].split(',')
    return header

def connect_database(query):
    '''Connect to postgrelsql DB using psycopg2 DB-API '''
    try:
        pg = psycopg2.connect(dbname="airports")
        c = pg.cursor()
            # commit the changes
        c.execute(query)
        pg.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pg.close()


def create_table():
    '''Create a table '''
    header = read_file() # Use read file function
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
                             ) '''.format(*header) # unpack the header into the table values
    connect_database(createAirportTable) # connect to the database and run the query


def searchIata(iataCode):
    '''Get the itatcode as a string variable and using SQL to search it from AIRPORT table'''
    # q = 'SELECT * FROM AIRPORT where iata_code ILIKE %s'
    query = 'SELECT name, iata_code as iata, gps_code, municipality as city, iso_country as country, longitude_deg as longitude, latitude_deg as latitude FROM AIRPORT where iata_code ILIKE %s'
    try:
        pg = psycopg2.connect(dbname="airports")
        c = pg.cursor(cursor_factory=RealDictCursor) # use the advantage of real dictionary cursor to get a query output as json
        c.execute(query, (iataCode,)) # Add the last comma to avoid the SQL injection
        result = c.fetchall()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pg.close()

    return None

def searchName(name):
    '''Get the name as a string variable and using SQL to search it from AIRPORT table'''
    # q = "SELECT * FROM AIRPORT where position(lower(%s) in lower(name)) > 0"
    query = "SELECT name, iata_code as iata, gps_code, municipality as city, iso_country as country, longitude_deg as longitude, latitude_deg as latitude FROM AIRPORT where position(lower(%s) in lower(name)) > 0"
    try:
        pg = psycopg2.connect(dbname="airports")
        c = pg.cursor(cursor_factory=RealDictCursor)
        c.execute(query, (name,))
        result = c.fetchall()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pg.close()

    return None

if __name__ == '__main__':
    create_table()
