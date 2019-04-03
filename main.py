from controllers.liker.liker import Liker
from controllers.vpn.vpn import Vpn
from controllers.webdrivers.webdrivers import Webdrivers
from controllers.post.post import Post
import logging
import os, time, requests, json, random, logging
from os import walk


formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
f_handler = logging.FileHandler('./config/file.log')   
f_handler.setFormatter(formatter)
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
logger.addHandler(f_handler)


wb = Webdrivers()
vpn = Vpn()
liker = Liker()
drivers = Webdrivers()

""" 
    Each VM will handle one post
    That way there is not racing problems 
    And its easier to handle servers
""" 

def like_post(post):
    logger.info('Started like process...')

    driver = wb.tor()
    start_time = time.time() 
    liker.like_post(driver, post)
    elapsed_time = time.time() - start_time

    logger.info("Like process elapsed time: {}s...".format(elapsed_time))
    
def get_posts():
    posts = ['https://fatalmodel.com/125829/marty-passo-fundo/3078003',
            'https://fatalmodel.com/366618/natalia-passo-fundo/3070694',
            'https://fatalmodel.com/431944/morena-rosa-passo-fundo/3082712',
            'https://fatalmodel.com/343219/ariela-passo-fundo-centro-2/3067388',
            'https://fatalmodel.com/177072/chocolate-cruz-alta/3069072',
            'https://fatalmodel.com/122189/vitoria-passo-fundo-centro/3085536']

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
    #https://fatalmodel.com/366618/natalia-passo-fundo/3070694
    posts = list()
    posts.append(Post('https://fatalmodel.com/412752/luana-dias-passo-fundo/3125728', 2, 13))

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
