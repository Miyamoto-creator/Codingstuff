import regex as re

def domain_name(url):
    x = re.sub("[\/w-]|_",  "", url)
    url += x
    print(url)
    lst_dom = ["https", "http", "www"]
    lst_doms = ["com", "net", "cojp", "org"]
    string = " "
    for i in lst_dom:
        if i in url:
            string = i
            string in range(len(lst_dom))
            print(string)
    if string in url:
        url = url.split(string)
    print(url)
    url = "".join(url)
    stringg = " "
    for j in lst_doms:
        if j in url:
            stringg = (j)
        if stringg in url:
            url = url.split(stringg)
    url = "".join(url)
    print(url)
    return url
domain_name("http://google.com")
