from controllers.liker.liker import Liker
from controllers.vpn.vpn import Vpn
from controllers.webdrivers.webdrivers import Webdrivers
from controllers.post.post import Post
from config.logger import setup_logger
import os, time, requests, json, random, logging
from os import walk

wb = Webdrivers()
vpn = Vpn()
liker = Liker()
drivers = Webdrivers()
logger = setup_logger()
api_url = 'https://fatal-bot-api.herokuapp.com/'

""" 
    Each VM will handle one post
    That way there is not racing problems 
    And its easier to handle servers
    Validate link
""" 

def like_post(post):
    logger.info('Started like process...')

    driver = wb.tor()
    start_time = time.time() 
    liker.like_post(driver, post)
    elapsed_time = time.time() - start_time

    logger.info("Like process elapsed time: {}s...".format(elapsed_time))
    
def get_posts():
    logger.info('Getting list of posts from database...')
    try:
        posts = requests.get(api_url + 'posts/')
        return posts['posts']
    except:
        logger.warning('Failed to get posts!')


def clean_tmp():
    logger.info('Cleaning temp files...')
    try:
        os.system('cd /tmp; sudo rm -r *')
        logger.info('Temp files cleaned successfully...')
    except OSError as e:
        logger.warn('Failed to clean temporary files')
        logger.debug(e)

def main():

    logger.info('Process started...')
    posts_res = get_posts()
    posts = list()

    for post in posts_res: 
        posts.append(Post(post['id'], post['link'], post['n_likes']))

    while len(posts) != 0:
        for post in posts:
            try:
                post_id = post.get_post_id()
                logger.info('Process is using post id {}'.format(post_id))

                if post.is_job_done():
                    logger.info('Removing post {} from list...'.format(post_id))
                    posts.remove(post)

                    raise Exception("Post {} job is done".format(post_id))

                like_post(post.get_post_link())
                post.update()
                clean_tmp()

            except Exception as e:
                clean_tmp()
                logger.exception(e)

if __name__ == "__main__":
    main()
