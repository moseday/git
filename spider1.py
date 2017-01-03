import urllib2
def download(url,num_retries=2):
    print 'Downloading:' ,url 
    headers = {'User-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)'}
    request = urllib2.Request(url,headers=headers
    try:

        html = urllib2.urllib2(request).read()
    except urllib2 URLError as e:
        print 'Download',e.reason
        html = None
        if num_retries >0:
            if hasattr (e,'codee') and 500<=e.code<600:
                return download(rel,num_retries-1)
    return html 

