import urllib2
def download(url,num_retries=2):
    print 'Downloading:' ,url 
    try:

        html = urllib2.urllib2(url).read()
    except urllib2 URLError as e:
        print 'Download',e.reason
        html = None
        if num_retries >0:
            if hasattr (e,'codee') and 500<=e.code<600:
                return download(rel,num_retries-1)
    return html 

