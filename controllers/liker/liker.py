from selenium.webdriver.common.keys import Keys
import time

class Liker:
    """
        Strip post link for its parent profile
        - parse the post string  
    """
    
    def like_post(self, webdriver, post):
        try:            
            post_link = post
            script = "var elmnt = document.getElementById('timeline'); elmnt.scrollIntoView();" 
            #https://fatalmodel.com/125829/marty-passo-fundo/3057913
            #https://fatalmodel.com/364813/luana-suelen/3038001
            #https://fatalmodel.com/116460/tais-ninfetinha-marau/3078419
            #https://fatalmodel.com/34409/laura-c-local-passo-fundo/3083178
            #webdriver.set_page_load_timeout(20)
            webdriver.get('https://fatalmodel.com/412752/luana-dias-passo-fundo')
            age18 = webdriver.find_element_by_id("agree-18")
            age18.click()
            webdriver.execute_script(script)
            time.sleep(2)
            btn = webdriver.find_element_by_xpath("//button[@data-tab='photos']")
            btn.click()
            time.sleep(2)
            btn = webdriver.find_element_by_css_selector(".btn-like[data-id='3125728']")
            btn.click()
            time.sleep(2)   
            webdriver.close()
            
            """
            webdriver.get(post)
            time.sleep(4)
            
            age18 = webdriver.find_element_by_id("agree-18")
            age18.click()

            a = webdriver.find_element_by_class_name("js-post-like")
            a.click()
            
            time.sleep(2)
            webdriver.close()
            """
        except Exception as e:
            webdriver.close()
            raise Exception(e)

