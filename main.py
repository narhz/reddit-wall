import requests
import praw
import configparser
import os


def config():
    config = configparser.ConfigParser()
    if os.path.exists('dev_config.ini'):
        config.read('dev_config.ini')
    else:
        config.read('config.ini')

    return config['REDDIT']
