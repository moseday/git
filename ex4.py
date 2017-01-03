
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
def link_crawler(seed_url,link_regex):
    crawl_queue = [seed_url]
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                link = urlparse.urljoin(seed_url, link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_links(html):
    
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com','/(index|view)')
