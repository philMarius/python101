'''other_mod for logging example'''

import logging

def add(x, y):
    '''Add some numbers together'''
    logging.info('Added %s and %s to get %s' % (x, y, x+y))
    return x+y
