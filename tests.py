
string = "http//fatalmodel.com/perfilid/nomedoperfil/postid"
post_link = "https://fatalmodel.com/8399/karol-com-local-passo-fundo/2882281"
exploded_link = post_link.split("/")
url_profile = "{}//{}/{}/{}".format(
exploded_link[0], exploded_link[2], exploded_link[3], exploded_link[4])
post_id = exploded_link[5]
res = string.split("/")
print(url_profile)
print(post_id)
"""
from controllers.vpn.vpn import Vpn
from controllers.webdrivers.webdrivers import Webdrivers
from bs4 import BeautifulSoup as bs
import time
import requests
import selenium
from selenium import webdriver as wb
import subprocess, os, time
import tbselenium.common as cm


from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

tbb_dir = "/home/dev/Desktop/tor-browser_en-US"
tor_process = launch_tbb_tor_with_stem(tbb_path=tbb_dir)
with TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM) as driver:
    driver.load_url("https://check.torproject.org")

tor_process.kill()


html_doc = requests.get('https://fatalmodel.com/125829/marty-passo-fundo/3078003').text
soup = bs(html_doc, 'html.parser')
likes = soup.findAll("span", {"class": "like-count"})[0].text
initial_likes = ""   
for l in likes:            
    if l != ')' and l != '(':
        print(l)


import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem
tbb_dir = "/home/dev/Desktop/tor-browser_en-US"
from tbselenium.tbdriver import TorBrowserDriver
with TorBrowserDriver(tbb_dir) as driver:
    driver.get('https://google.com')



import tbselenium.common as cm
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import launch_tbb_tor_with_stem

from tbselenium.tbdriver import TorBrowserDriver
with TorBrowserDriver(tbb_dir) as driver:
    driver.get('https://google.com')

    for server in servers:
        tries = post.get_tries()
        print(tries)
        if tries % 10 == 0 and tries != 0:
            time.sleep(30)

        start_time = time.time()
        time.sleep(1)
        try:
            #start_vpn(server)
            #time.sleep(60)
            like_post(post)
            #vpn.kill()

        except Exception as e:
         #vpn.kill()
         print(e)
    
######################################################################33




    mypath = "/etc/openvpn/ovpn_udp/"
    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break

def is_internet_on():
    try:
        requests.get('https://google.com', timeout=1)
    except: 
        raise Exception("No internet")





























def get_countries_ids():
    try:
        url = 'https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_countries'
        res = requests.get(url)
        res = json.loads(res.text)
        server_ids = []
        for info in res:
            server_ids.append(info['id'])
    except:
       raise Exception('Failed to get countries ids...')

    return server_ids

def get_list_of_servers():
    hostnames = []
    try:
        countries_ids = get_countries_ids()
    except:
        raise Exception("Failed to get countries ids")

    print("Getting hostnames...")
    for id in countries_ids:
        url = 'https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters={"country_id":"' + str(
            id) + '"}'
        try:
            print(id)
            res = requests.get(url)
            res = json.loads(res.text)
            for info in res:
                hostnames.append(info['hostname'])
                res = requests.get(url)
                res = json.loads(res.text)
                for info in res:
                    hostnames.append(info['hostname'])
        except:
            raise Exception("Couldn't get hostnames of " + str(id))

    print("Checking for duplicates...")
    non_duplicated_servers = []
    for x in range(hostnames.__len__()):
        hostname_test = hostnames[x]
        isEqual = False

        for y in range(hostnames.__len__()):
            if hostnames[y] == hostname_test:
                if x == y:
                    break
                else:
                    isEqual = True

        if not isEqual:
            non_duplicated_servers.append(hostnames[x])

    return non_duplicated_servers

def start_vpn(server):
    errors = 0
    try:
        print("Testing server: " + server)
        vpn.start(server)
        time.sleep(2)
        for x in range(3):
            try:
                time.sleep(0.5)
                is_internet_on()
            except:
                print("Server is not responding...")
                errors += 1

            if errors == 3:
                vpn.kill()
                raise Exception("Server didn't respond")

            time.sleep(0.2)
    except Exception as e : 
        vpn.kill()
        raise Exception(e)
    
    print("Server started: " + server)





















from os import walk
mypath = "/etc/openvpn/ovpn_udp/"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
print(f)


cmd = "gnome-terminal -e ' sh -c \"sudo echo $$ >> ./controllers/vpn/scripts/output.txt; ./controllers/vpn/scripts/test.sh br7.nordvpn.com.udp.ovpn; sleep 100\"'"
#cmd = "gnome-terminal -e ' sh -c \"sudo echo $$ >> ./controllers/vpn/scripts/output.txt;cd /etc/openvpn/ovpn_udp/; sudo openvpn br7.nordvpn.com.udp.ovpn; sleep 100\"'"
#cmd = "openvpn br7.nordvpn.com.udp.ovpn; sleep 10"
pid = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
print(pid.pid)

vpn = Vpn()

vpn.start('br5.nordvpn.com')


#webdriver = Webdrivers.firefox('Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1')
webdriver = wb.PhantomJS()
post = 'https://fatalmodel.com/125829/marty-passo-fundo/3054742'
script = "var elmnt = document.getElementById('timeline'); elmnt.scrollIntoView();" 

webdriver.set_page_load_timeout(20)
webdriver.get('https://fatalmodel.com/125829/marty-passo-fundo/')

age18 = webdriver.find_element_by_id("agree-18")
age18.click()

webdriver.execute_script(script)

time.sleep(0.5)

button = webdriver.find_element_by_xpath("//button[@data-tab='photos']")
button.click()

time.sleep(0.5)

post = webdriver.find_element_by_css_selector(".btn-like[data-id='3054742']")

post.click()
time.sleep(0.5)
webdriver.close()


post = 'https://fatalmodel.com/125829/marty-passo-fundo/3048703'
page = requests.get(post)
soup = BeautifulSoup(page.content, 'html.parser')

mydivs = soup.find("div", {"class": "post-3048703"})
count = mydivs.find("span", {"class": "like-count"})
print(count.text)
count = count.text
new_count = ""

for l in count:
    if l != '(' and l != ')':
        new_count += l

print(new_count)

vpn = Vpn()

webdriver = Webdrivers.firefox('Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1')
post = 'https://fatalmodel.com/125829/marty-passo-fundo/3048703'
script = "var elmnt = document.getElementById('timeline'); elmnt.scrollIntoView();" 

webdriver.get('https://fatalmodel.com/125829/marty-passo-fundo/')

age18 = webdriver.find_element_by_id("agree-18")
age18.click()
webdriver.execute_script(script)
time.sleep(1)
button = webdriver.find_element_by_xpath("//button[@data-tab='photos']")
button.click()
post_id="3048703"
time.sleep(1)
post = webdriver.find_element_by_xpath("//button[@data-id='3048703']")
post.click()
time.sleep(1)
webdriver.close()
"""