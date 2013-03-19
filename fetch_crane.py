import urllib2
from BeautifulSoup import BeautifulSoup
import os.path
from urllib2 import urlopen
import os
import codecs

## definitions
base_url_pre= "http://collections.chadwyck.com/searchFulltext.do?id="
base_url_suff= "&divLevel=0&queryId=&area=eaf2&forward=textsFT&pageSize=&print=No&size=710Kb&warn=Yes"
theurl = 'http://collections.chadwyck.com/contents/volumes/eaf2.jsp'
txdata = None
txheaders =  {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# fake a user agent, some websites (like google) don't like automated exploration
div_class = 'rdrcontent'

def test(book_url):
    return base_url in book_url

def my_get_book_text(id, title, year):
    base_dir = "/Users/joyceliu/Dropbox/info290corpus"
    url = base_url_pre + id + base_url_suff
    print "Getting " + url
    handle = urlopen(url)
    file_name = year + "_" + title + ".txt"
    f = open(base_dir + "/" + file_name, "w")
    f.write(handle.read())
    f.close()    

# main function
try:
    #req = Request(theurl, txdata, txheaders)
    # create a request object

    handle = urlopen(theurl)
    # and open it to return a handle on the url

except IOError, e:
    print 'We failed to open "%s".' % theurl
    if hasattr(e, 'code'):
        print 'We failed with error code - %s.' % e.code
    elif hasattr(e, 'reason'):
        print "The error object has the following 'reason' attribute :"
        print e.reason
        print "This usually means the server doesn't exist,",
        print "is down, or we don't have an internet connection."
    sys.exit()

else:
    main_page = handle.read() 
    soup = BeautifulSoup(main_page)
    links =  soup.findAll('a')
    for link in links:
        try:
            url = link['href']
            if "Z00" in url:
                print link
                inner_text = link.string
                year = "?"
                title = inner_text
                if "(" in year:
                    title = components[0]
                    components = inner_text.split("(")
                    year = components[1][:-1]
                id = url.split("('")[1].split("',")[0]
                print title
                my_get_book_text(id, title, year)
                print "\n\n"
        except Exception, e:
            print e
            pass

    
if cj is None:
    print "We don't have a cookie library available - sorry."
    print "I can't show you any cookies."
else:
    cj.save(COOKIEFILE)                     # save the cookies again

