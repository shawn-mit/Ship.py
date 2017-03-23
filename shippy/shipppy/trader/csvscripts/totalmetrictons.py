import csv 
import sqlite3

def get_totalmetrictons_data_as_a_list(totalmetrictons):

    """ 
    Method which will read CSV file 'tot' and parse CSV data into lists by line. The model will then post the data into the us_port model 
    with create object. 
    Author: Shawn M. 
    """

    with open(totalmetrictons, "r") as metric_tons:
        for metric_tons in csv.reader(metric_tons):
            yield metric_tons

if __name__ == '__main__':
    filepath = "../data/TotalMT.csv"
    iterate_data = iter(get_totalmetrictons_data_as_a_list(filepath))
    year= next(iterate_data)
    year_list = list(year)
    rest_of_data = iter(get_totalmetrictons_data_as_a_list(filepath))
    #print(year)
    #print(next(iterate_data)) 

    with sqlite3.connect("../../db.sqlite3") as db:
        cursor = db.cursor()
    
        for row in iterate_data:
            #year = row[0]
            #total_ton = row[1:]
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
           

            print(usport, year2003)
      
        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2003
            AND  usport = '{}'
                """.format(year2003, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2004
            AND  usport = '{}'
                """.format(year2004, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2005
            AND  usport = '{}'
                """.format(year2005, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2007
            AND  usport = '{}'
                """.format(year2007, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2008
            AND  usport = '{}'
                """.format(year2008, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2009
            AND  usport = '{}'
                """.format(year2009, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2010
            AND  usport = '{}'
                """.format(year2010, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2011
            AND  usport = '{}'
                """.format(year2011, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2012
            AND  usport = '{}'
                """.format(year2012, usport))

        cursor.execute("""
            UPDATE trader_trade_year
            SET  total_ton = '{}'
            WHERE year = 2013
            AND  usport = '{}'
                """.format(year2013, usport))