import urllib.request
import re
from collections import deque

save_path='D:/test.txt'
obj=open(save_path,'w')
obj.close()

page=deque(['p1/','p2/','p3/'])
while page:

    home_url='http://haitao.smzdm.com/'

    url=home_url+page.popleft()

    req=urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    op=urllib.request.urlopen(req)
    data=op.read().decode()
    itemre=re.compile('href="http://haitao.smzdm.com/p/(\d+)/?"')
    itemtemp=itemre.findall(data)


    i=0
    item=deque()
    while i<len(itemtemp):
        if 'http://haitao.smzdm.com/p/'+itemtemp[i]+'/'not in item:
            item.append('http://haitao.smzdm.com/p/'+itemtemp[i]+'/')
        i+=1
    print(item)


    today_item=deque()
    while item:
        item_url=item.popleft()
        item_req=urllib.request.Request(item_url)
        item_req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        item_op=urllib.request.urlopen(item_req)
        item_data=item_op.read().decode()
        timere=re.compile('<span>[\u65f6][\u95f4].(.+?)</span>')
        time=timere.findall(item_data)

        try:
            if len(time[0])==5:
                today_item.append(item_url)
        except:
            continue
    print(today_item)

    item_link=deque()
    title=deque()
    price=deque()
    description=deque()
    while today_item:
        today_item_url=today_item.popleft()
        print(today_item_url)
        item_link.append(today_item_url)

        today_item_req=urllib.request.Request(today_item_url)
        today_item_req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
        today_item_op=urllib.request.urlopen(today_item_req)
        today_item_data=today_item_op.read().decode()

        title_re=re.compile('<meta property="og:title" content="(.+?)" />')
        title_temp=title_re.findall(today_item_data)
        print(title_temp)
        title.append(title_temp[0])


        price_re=re.compile('<meta property="og:description" content="(.+?)" />')
        price_temp=price_re.findall(today_item_data)
        print(price_temp)
        price.append(price_temp[0])

        description_re=re.compile('<div class="inner-block">\n *?<p>(.+?)</p>')
        description_temp=description_re.findall(today_item_data)
        try:
            print(description_temp)
        except:
            description.append('Error')
            continue
        try:
            description.append(description_temp[0])
        except:
            description.append('null')
            continue



    with open(save_path,'a') as obj:
        i=0
        while i<len(title):
            obj.write('Title:'+title[i]+'\n'+'Link:'+item_link[i]+'\n'+
                      'Price:'+price[i]+'\n'+'Description:'+description[i]+'\n\n')
            i+=1



