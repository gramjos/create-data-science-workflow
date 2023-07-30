#!/usr/local/bin/python3.9
# requests lib needs 3.9
"""
        needed pip install lxml 
"""

def parse ( s ) :
    # '1 ETH = 2,431.86 USD'
    m= search(r'1\s([A-Z]{3})\s=\s(([0-9]|,|\.)*)', s )
    # returns a stringified int
    return m.group(2)

def get_link_price(links, content):
    to_Log= list()
    for link in links:
        re = content.find_all(name= 'a', attrs= {'href':[link]})
        print(re[0].text)
        to_Log.append( parse( re[0].text ))
    log_data ( to_Log )

def log_data ( data, warehouse='GetCoinPrice_Log.csv') :
    with open ( warehouse, 'a' ) as log_fd :
        new_data=''
        for i in data: 
            new_data+=( i+'| ' )
        t_stamped=str(datetime.now())
        ret=new_data+t_stamped+'\n'
        log_fd.write(ret)

if __name__ == "__main__":

    import requests 
    from bs4 import BeautifulSoup
    from re import search 
    from datetime import datetime

    # preparing to make url
    which_crypts= ['ethereum','bitcoin', 'litecoin','zcash','monero']

    # piece together the 'a' tag's attribute (href) value 
        # front {which_crypts[i]} back
        # comparison/zcash-price.html
    front,back= "comparison/","-price.html"

    # request object from HTTP request. r holds raw content
    r= requests.get('https://bitinfocharts.com')

    # scraped content reformat
    content= BeautifulSoup(r.content,features="lxml")

    href_link= [ front+i+back for i in which_crypts ]

    get_link_price(href_link, content)


