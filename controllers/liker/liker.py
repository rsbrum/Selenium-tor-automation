from selenium.webdriver.common.keys import Keys
import time, logging

logger = logging.getLogger('root')

class Liker:
    """
        Strip post link for its parent profile
        - parse the post string  
    """

    def like_post(self, webdriver, post_link):
        logger.info('Executing like process...')
        try:
            exploded_link = post_link.split("/")
            url_profile = "{}//{}/{}/{}".format(
                exploded_link[0], exploded_link[2], exploded_link[3], exploded_link[4])
            post_id = exploded_link[5]

            logger.debug('Url profile: {}'.format(url_profile))
            logger.debug('Post id: {}'.format(post_id))

            script = "var elmnt = document.getElementById('timeline'); elmnt.scrollIntoView();"

            webdriver.get(url_profile)
            age18 = webdriver.find_element_by_id("agree-18")
            age18.click()
            webdriver.execute_script(script)

            time.sleep(2)

            btn = webdriver.find_element_by_xpath(
                "//button[@data-tab='photos']")
            btn.click()

            time.sleep(2)

            btn = webdriver.find_element_by_css_selector(
                ".btn-like[data-id='{}']".format(post_id))
            btn.click()

            time.sleep(2)

            webdriver.close()

        except Exception as e:
            logger.warning("Failed to like post!")
            logger.exception(e)
            webdriver.close()
            raise Exception(e)
