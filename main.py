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

    return config


def auth_reddit():
    config = config()['REDDIT']

    reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     user_agent=config['user_agent'])

    return reddit


def get_user_subs():
    if os.path.exists('dev_subs.txt'):
        with open('dev_subs.txt', 'r') as subs_file:
            subs_from_file = subs_file.readlines()

        subs = []
        for i in subs_from_file:
            subs.append(i.replace('\n', ''))

    return subs
