'''Learning about CSV parsing'''

import csv
import os

os.chdir('/Users/phil/dev/python/python101/')

def csv_reader(file_obj):
    '''Read CSV file'''
    read = csv.reader(file_obj)
    for row in read:
        print(" ".join(row))

if __name__ == '__main__':
    CSV_PATH = 'files/TB_data_dictionary_2017-08-29.csv'
    with open(CSV_PATH, 'r') as f_obj:
        csv_reader(f_obj)
