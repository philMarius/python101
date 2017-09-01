'''other_mod_2 for logger.py'''

import logging

MODULE_LOGGER = logging.getLogger('exampleApp.otherMod2')

def add(x, y):
    '''Adding again'''
    logger = logging.getLogger('exampleApp.otherMod2.add')
    logger.info('added %sand %s to get %s' % (x, y, x+y))
    return x+y
