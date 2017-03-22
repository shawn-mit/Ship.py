import csv 
import sqlite3

def get_totalvalue_data_as_a_list(totalvalue):

    """ 
    Method which will read CSV file 'tot' and parse CSV data into lists by line. The model will then post the data into the us_port model 
    with create object. 
    Author: Shawn M. 
    """

    with open(totalvalue, "r") as us_port_data:
        for us_port_data in csv.reader(us_port_data):
            yield us_port_data

if __name__ == '__main__':
    filepath = "../data/usport.csv"
    iterate_data = iter(get_usport_data_as_a_list(filepath))
    next(iterate_data)

    #with sqlite3.connect("../../db.sqlite3") as db:
        #cursor = db.cursor()

        for row in iterate_data:
            total_ton = row[0]
            total_value = row[1]

            print(city, state)

            #cursor.execute("""
               #UPDATE trader_us_port(id, city, state)
                #VALUES (null, '{}', '{}')""".format(city, state))