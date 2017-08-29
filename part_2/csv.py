'''Learning about CSV parsing'''

import csv
import os

os.chdir('/Users/phil/dev/python/python101/')

def csv_reader(file_obj):
    '''Read CSV file'''
    reader = csv.reader(file_obj)
