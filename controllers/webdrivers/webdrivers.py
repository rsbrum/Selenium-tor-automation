import os
import tbselenium.common as cm
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

class Webdrivers:

    def chrome(self):
        return webdriver.Chrome()

    def tor(self):
        tbb_dir = "/home/rnsbrum/Desktop/tor-browser_en-US"
        driver = TorBrowserDriver(tbb_dir) 
        return driver

    @staticmethod
    def firefox(user_agent):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        options = Options()
        #options.headless = True

        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        profile.set_preference("general.useragent.override",user_agent)
        profile.set_preference("places.history.enabled", False)
        profile.set_preference("privacy.clearOnShutdown.offlineApps", True)
        profile.set_preference("privacy.clearOnShutdown.passwords", True)
        profile.set_preference("privacy.clearOnShutdown.siteSettings", True)
        profile.set_preference("privacy.sanitize.sanitizeOnShutdown", True)
        #profile.set_preference('permissions.default.image', 2)
        #profile.set_preference('permissions.default.stylesheet', 2)
        profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        profile.update_preferences()
        
        wb = webdriver.Firefox(options=options, firefox_profile=profile, log_path="")
        return wb

    @staticmethod
    def firefox2():
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.cache.disk.enable", False)
        profile.set_preference("browser.cache.memory.enable", False)
        profile.set_preference("browser.cache.offline.enable", False)
        profile.set_preference("network.http.use-cache", False)
        profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:37.0) Gecko/20100101 Firefox/37.0")
        profile.set_preference("places.history.enabled", False)
        profile.set_preference("privacy.clearOnShutdown.offlineApps", True)
        profile.set_preference("privacy.clearOnShutdown.passwords", True)
        profile.set_preference("privacy.clearOnShutdown.siteSettings", True)
        profile.set_preference("privacy.sanitize.sanitizeOnShutdown", True)
        profile.set_preference('permissions.default.image', 2)
        profile.set_preference('permissions.default.stylesheet', 2)
        profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        profile.update_preferences()

        return webdriver.Firefox(profile)

    @staticmethod
    def IE():
        return webdriver.Ie()

    @staticmethod
    def PhantomJS():
        return webdriver.PhantomJS()