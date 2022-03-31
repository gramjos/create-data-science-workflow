#!/usr/local/bin/python3.9
# requests lib needs 3.9
"""
        needed pip install lxml 
"""

def parse ( s ) :
    # '1 ETH = 2,431.86 USD'
    m= search(r'1\s([A-Z]{2,3})\s=\s(([0-9]|,|\.)*)', s )
    # returns a stringified int
    return m.group(2)

def get_link_price(l, content):

    a_tag = 'a'
    cv2= {'href':[]}

    to_Log= list()

    for i in l:
        cv2['href']=i
        re = content.find_all(name= a_tag, attrs= cv2)
        print(re[0].text)
        to_Log.append( parse( re[0].text ))
    log_data ( to_Log )

# Historical Analysis
# raw at GetCoinPrice_Log.csv

def log_data ( data, warehouse='GetCoinPrice_Log.csv') :
    # display the data being logged and its standard
    #p_print(data)   
    #print(data)   data.append( datetime.now() )
    with open ( warehouse, 'a' ) as log_fd :
        for i in data: 
            if type(i) != str :
                time_stamp= i.strftime("%x %X")
                log_fd.write( time_stamp )
                
            else :
                log_fd.write( i+'| ' )
        log_fd.write("\n")

if __name__ == "__main__":

    import requests 
    from bs4 import BeautifulSoup
    from re import search 
    from datetime import datetime

    # preparing to make url
    which_crypts= ['ethereum','bitcoin', 'litecoin','zcash','monero']

    # piece together the 'a' tag's attribute (href) value 
        # comparison/zcash-price.html
    front,back= "comparison/","-price.html"

    # request object from HTTP request. r holds raw content
    r= requests.get('https://bitinfocharts.com')

    content= BeautifulSoup(r.content,features="lxml")

    href_link= [ front+i+back for i in which_crypts ]
    get_link_price(href_link, content)


