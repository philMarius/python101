'''Learning about config files'''

import configparser

def create_config(path):
    '''Create config file'''
    config = configparser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'font', 'Courier')
    config.set('Settings', 'font_size', '10')
    config.set('Settings', 'font_style', 'Normal')
    config.set('Settings', 'font_info', 'You are using %(font)s at %(font_size)s pt')

    with open(path, 'w') as config_file:
        config.write(config_file)

if __name__ == '__main__':
    PATH = 'files/settings.ini'
    create_config(PATH)
