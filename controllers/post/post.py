from bs4 import BeautifulSoup as bs
import requests
import logging

"""
    verify in the class if the n of likes has increased
"""
class Post:
    """
        when a like is given, it must be verified and
        then it should update de given likes 
    """
    logger = logging.getLogger('root')

    def __init__(self, link, id, target_likes):
        self.logger.info('Creating post object')
        self.link =  link
        self.id = id
        self.target_likes = target_likes
        self.initial_likes = self.get_likes()
        self.current_likes = self.get_likes()
        self.given_likes = 0 
        self.tries = 0
        self.logger.info('Created post with id {}...'.format(self.id))

    def print_info(self):
        print("Post link: ", self.link)
        print("Initial likes: ", self.initial_likes)
        print("Target likes: ", self.target_likes)
        print("Current likes: ", self.current_likes)
        print("Given likes: ", self.given_likes)
        print("Tries: ", self.tries)

    def is_job_done(self):
        if self.given_likes - 1 == self.target_likes:
            self.logger.info('Post {} job done...'.format(self.id))
            return True
        else:
            return False
         
    def get_likes(self):
        self.logger.info('Scrapping post likes...')
        html_doc = requests.get(self.link).text
        soup = bs(html_doc, 'html.parser')
        likes = soup.findAll("span", {"class": "like-count"})[0].text
        likes_res = ""                                                    
        for l in likes:
            if l != ')' and l != '(':
                likes_res += l

        return likes_res
   
    def update(self):
        self.logger.info('Updating post {} information...'.format(self.id))
        likes = self.get_likes()
        
        if likes > self.current_likes:
            self.given_likes += 1
        else:
            self.logger.warning('Like didnt take effect...')   

        self.tries += 1 
        self.current_likes = self.get_likes()

    def get_post_id(self):
        self.logger.info('Getting post id...')
        return self.id

    def get_post_link(self):
        self.logger.info('Getting post link...')
        return self.link
