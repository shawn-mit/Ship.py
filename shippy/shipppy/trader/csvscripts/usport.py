import csv 
import sqlite3

def get_usport_data_as_a_list(usport):

    """ 
    Method which will read CSV file 'usport' and parse CSV data into lists by line. The model will then post the data into the us_port model 
    with create object. 
    Author: Shawn M. 
    """

    with open(usport, "r") as us_port_data:
        for us_port_data in csv.reader(us_port_data):
            yield us_port_data

if __name__ == '__main__':
    filepath = "../data/usport.csv"
    iterate_data = iter(get_usport_data_as_a_list(filepath))
    print(next(iterate_data))


    with sqlite3.connect("../../db.sqlite3") as db:
        cursor = db.cursor()


        for row in iterate_data:
            city = row[0]
            state = row[1]

            print(city, state)

            cursor.execute("""
                INSERT INTO trader_us_port(id, city, state)
                VALUES (null, '{}', '{}')""".format(city, state))





            =======================================


