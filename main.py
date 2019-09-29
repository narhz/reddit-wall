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


def auth_reddit():
    config = config()

    reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     user_agent=config['user_agent'])

    return reddit
