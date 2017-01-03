import lxml.html
import urlparse
import requests
import urllib2


def download(url,num_retries=2):
    print 'Downloading:' ,url 
    headers = {'User-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)'}
    proxies = {"http":"http://121.14.6.236:80",}

    response = requests.get(url,headers=headers,proxies=proxies)
    try:
        html = response.text
    except requests.GetError as e:
        print 'Download',e.reason
        html = None
        if num_retries >0:
            if hasattr (e,'codee') and 500<=e.code<600:
                return download(rel,num_retries-1)
    return html



import re
def link_crawler(seed_url,link_regex,scrape_callback=None):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)

    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        links = []
        if scrape_callback:
            links.extend(scrape_callback(url,html) or [])

        for link in get_links(html):
            if re.match(link_regex,link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)


import csv
class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('country.csv', 'w'))
        self.fields = ('area','population','iso','country','capital','continent','tld','currency_code','currency_name','phone','postal_code_format','postal_code_regex','languages','neighbours')
        self.writer.writerow(self.fields)

    def __call__(self,url,html):
        if re.search('/view/', url):
            tree = lxml.html.fromstring(html)
            row = []
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row >td,w2p_fw'.format(field))[0].text_content())
                self.writer.writerow(row)
link_crawler('http://example.webscraping.com','/view/',scrape_callback=ScrapeCallback())

