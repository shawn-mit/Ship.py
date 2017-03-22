"""
years = next(get_data_list)
print (years)


years_list = list(years)

rest_of_data = iter(get_data_list)
print(rest_of_data)
"""

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
    print(year)
    print(next(iterate_data)) 

    
    for row in iterate_data:
        year = row[0]
        total_ton = row[1]
       

        print(year, total_ton)