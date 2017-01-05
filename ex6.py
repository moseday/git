class Downloader:
    def __init__(self, delay=5,user_agent='wswp', proxies=None, num_retries=1, cache=None):
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.cache = cache


    def __call__(self,url):
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
        else:
            if self.num_retries > 0 and \ 500 <= result['code'] <600:
                result = None
        if result is None:
            self.throttle.wait(url)
            proxies = random.choice(self.proxies) if self.proxies else None
            headers = {'User-agent' : self.user_agent}
            result = self.download(url, headers, proxies, num_retries)
            if self.cache:
                self.cache[url] = result
        return result['html']
    

    def download(self, url, headers, proxies, num_retries, data=None):
        print "Download:", url

        res = requests.get(url, headers, proxies, data)
        html = res.text
        code = res.code
        
        



#bitbucket.org/wswp/code/src/tip/chapter03
        
