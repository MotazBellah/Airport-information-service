import psycopg2
import json
from psycopg2.extras import RealDictCursor

def read_file():
    '''Read airports file and get the header'''
    f = open(r"airports.csv", 'r')
    fString = f.read()
    # print(fString)
    fList = []
    header = fString.split('\n')[0].split(',')
    return header

def create_table():
    header = read_file()
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
    try:
        pg = psycopg2.connect(dbname="airports")
        c = pg.cursor()
        # commit the changes
        c.execute(createAirportTable)
        pg.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pg.close()

if __name__ == '__main__':
    create_table()
