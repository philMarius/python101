'''Learning the logger'''

import logging.config
import other_mod
import other_mod_2
import os

os.chdir('/Users/phil/dev/python/python101/part_2/')

def first():
    '''Main entry point of app'''
    logging.basicConfig(filename='files/mySnake.log', level=logging.INFO)
    logging.info('Program started')
    result = other_mod.add(7, 8)
    logging.info('Done!')

def second():
    '''Trying out some formatting'''
    logger = logging.getLogger('exampleApp')
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('files/new_snake.log')

    formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info('Program started')
    result = other_mod_2.add(7, 8)
    logger.info('Done!')

def third():
    '''Using the conf file'''
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('exampleApp')

    logger.info('Program started')
    result = other_mod_2.add(7, 8)
    logger.info('Done')

if __name__ == '__main__':
    third()
