'''Learning about CSV parsing'''

import csv
import os

os.chdir('/Users/phil/dev/python/python101/')

def csv_reader(file_obj):
    '''Read CSV file'''
    read = csv.reader(file_obj)
    for row in read:
        print(" ".join(row))

def csv_dict_reader(file_obj):
    '''Use DictReader to read CSV'''
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        print(line['first_name'])
        print(line['last_name'])

if __name__ == '__main__':
    CSV_PATH_1 = 'files/TB_data_dictionary_2017-08-29.csv'
    CSV_PATH_2 = 'files/basic_data.csv'
    with open(CSV_PATH_2, 'r') as f_obj:
        csv_dict_reader(f_obj)
