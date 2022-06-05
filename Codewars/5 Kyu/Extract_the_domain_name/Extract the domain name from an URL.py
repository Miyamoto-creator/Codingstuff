import logging
import re

#logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def domain_name(url):
    print(url)
    
    before = ["http://", "https://", "www."]
    after = [".com", ".co.jp", ".ru"]
    string = ""
    for i in before:
        if i in url:
            string = (i)
    if string in url:
        url = url.split(string)
    print(url)
    url = "".join(url)
    stringg = ""
    for j in after:
        if j in url:
            stringg = (j)
        if stringg in url:
            url = url.split(stringg)
    url = "".join(url)
    print(url)
    return url
        #url = url.replace(illegals, '')
        #logging.error('url after replace for loop %s', url)
    #x_url = url.split(illegal)
    #g_url = "".join(x_url)
    #h_url = g_url.replace(illegal_two, "")
    
    #logging.error('x_url after split %s', x_url)
    #logging.error('G_url after join %s', g_url)
    #logging.error('H_url after replace %s', h_url)

domain_name("http://google.com")
#domain_name("http://google.co.jp")
#domain_name("www.xakep.ru")
#domain_name("https://youtube.com")

