import csv 
import sqlite3

def get_totalvalues_data_as_a_list(totalvalues):

    """ 
    Method which will read CSV file 'tot' and parse CSV data into lists by line. The model will then post the data into the us_port model 
    with create object. 
    Author: Shawn M. 
    """

    with open(totalvalues, "r") as values:
        for values in csv.reader(values):
            yield values

    """
    If statement to grab the filepath and all the  data. 
    
    """

if __name__ == '__main__':
    filepath = "../data/TotalValue.csv"
    iterate_data = iter(get_totalvalues_data_as_a_list(filepath))
    data = next(iterate_data)
    data_list = list(data)
    rest_of_data = iter(get_totalvalues_data_as_a_list(filepath))
        #print(data)
        #print(next(iterate_data)) 

    with sqlite3.connect("../../db.sqlite3") as db:
        cursor = db.cursor()
       
        for row in iterate_data:
            #data = row[0:]
            
            #total_value = row[1:]
            usport = row[0]
            year2003 = row[1]
            year2004 = row[2]
            year2005 = row[3]
            year2007 = row[4]
            year2008 = row[5]
            year2009 = row[6]
            year2010 = row[7]
            year2011 = row[8]
            year2012 = row[9]
            year2013 = row[10]

            print(usport, 
                year2003,
                year2004,
                year2005,
                year2007,
                year2008,
                year2009,
                year2010,
                year2011,
                year2012,
                year2013)

        
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2003,  year2003, usport))


            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2004,  year2004, usport))

    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2005,  year2005, usport))

    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2007,  year2007, usport))
    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2008,  year2008, usport))
    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2009,  year2009, usport))
    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2010,  year2010, usport))
    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2011,  year2011, usport))
    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2012,  year2012, usport))

    
            cursor.execute("""
                  INSERT INTO trader_trade_year(id, year, total_value, usport)
                  VALUES(null, {}, '{}','{}')""".format(2013,  year2013, usport))
