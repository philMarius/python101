'''Learning about config files'''

import configparser
import os

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

def get_config(path):
    '''Return config object'''
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    '''Print out setting'''
    config = get_config(path)
    value = config.get(section, setting)

    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )

    print(msg)
    return value

def update_setting(path, section, setting, value):
    '''Update setting'''
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, 'w') as config_file:
        config.write(config_file)

def delete_setting(path, section, setting):
    '''Delete setting'''
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, 'w') as config_file:
        config.write(config_file)

if __name__ == '__main__':
    PATH = 'files/settings.ini'
    FONT = get_setting(PATH, 'Settings', 'font')
    FONT_SIZE = get_setting(PATH, 'Settings', 'font_size')

    update_setting(PATH, 'Settings', 'font_size', '12')

    delete_setting(PATH, 'Settings', 'font_style')
