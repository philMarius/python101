'''Writing out a CSV'''

import csv
import os

os.chdir('/Users/phil/dev/python/python101/')

def csv_writer(data, path):
    '''Write out a CSV'''
    with open(path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def csv_dict_writer(path, fieldnames, data):
    '''Write CSV with DictWriter'''
    with open(path, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    DATA = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")]

    PATH = 'files/output.csv'

    MY_LIST = []
    FIELDNAMES = DATA[0]
    for values in DATA[1:]:
        inner_dict = dict(zip(FIELDNAMES, values))
        MY_LIST.append(inner_dict)
    PATH_DICT_WRITER = 'files/dictwriter_output.csv'

    csv_dict_writer(PATH_DICT_WRITER, FIELDNAMES, MY_LIST)
