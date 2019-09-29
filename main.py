import requests
import praw
import configparser
import os




def get_config():
    config = configparser.ConfigParser()
    if os.path.exists('dev_config.ini'):
        config.read('dev_config.ini')
    else:
        config.read('config.ini')

    return config


def auth_reddit():
    config = get_config()['REDDIT']

    reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     user_agent=config['user_agent'])

    return reddit


def get_user_subs():
    if os.path.exists('dev_subs.txt'):
        with open('dev_subs.txt', 'r') as subs_file:
            subs_from_file = subs_file.readlines()
    else:
        with open('subs.txt', 'r') as subs_file:
            subs_from_file = subs_file.readlines()

    subs = []
    for i in subs_from_file:
        subs.append(i.replace('\n', ''))

    return subs


def get_posts():
    reddit = auth_reddit()

    urls = []
    for sub in get_user_subs():
        for post in reddit.subreddit(sub).hot(limit=int(get_config()['PREFS']['img_amount'])):
            if post.is_self == True:
                pass
            elif post.stickied == True:
                pass

            if post.url[-4:] == '.jpg':
                urls.append(post.url)
            else:
                pass




if __name__ == '__main__':
    get_posts()
