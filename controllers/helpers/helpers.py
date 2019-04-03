    def is_internet_on():
        try:
            requests.get('https://google.com', timeout=1)
            return True
        except requests.ConnectionError as err: 
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
    except Exception as e:
        print(e)

    print("Getting hostnames...")
    for id in countries_ids:
        url = 'https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations&filters={"country_id":"' + str(id) + '"}'
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

    #check for duplicated server names
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
    try:
        print("Testing server: " + server)
        try:
            Vpn.start(server)
            time.sleep(0.3)
            for x in range(3):
                is_internet_on()
                time.sleep(0.2)
        except Exception as e:
            print(e)
    except: 
        Vpn.kill()
        raise Exception("Failed to start server: " + server )
    
    print("Server started: " + server)

def like_posts(posts):
    user_agents = ['Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0','Mozilla/5.0 (X11; U; Linux Core i7-4980HQ; de; rv:32.0; compatible; JobboerseBot; http://www.jobboerse.com/bot.htm) Gecko/20100101 Firefox/38.0','Mozilla/5.0 (Windows NT 5.1; rv:36.0) Gecko/20100101 Firefox/36.0','Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0']
    for post in posts:
        try: 
            x = random.randint(0, 9)
            driver = Webdrivers.firefox(user_agents[x])
            start_time = time.time()
            Liker.like_post(driver, post)
            #Liker.like_post(driver, post['link'])
            #decrement_likes_post(post['id'])

            elapsed_time = time.time() - start_time
            print("Time taken to like post {}: {}".format(post, elapsed_time))
        except Exception as e:
            print(e)
