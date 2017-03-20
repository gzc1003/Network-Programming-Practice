__author__ = 'guozichun'

from urllib import request
import re

home_url='https://s.taobao.com/search?q=%E6%99%BA%E8%83%BD%E5%AE%B6%E5%B1%85&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20151117&ie=utf8'
a=input('Please input the page:')
a=int(a)
for i in range(a):
     if i==0:
          url=home_url
     else:
          url=home_url+'&bcoffset='+str(1-3*(i-1))+'&ntoffset='+str(1-3*(i-1))+'&p4plefttype=3%2C1&p4pleftnum=1%2C3&s='+str(44*i)
          print(url)
     req=request.Request(url)


     op=request.urlopen(req)
     try:
        data=op.read().decode()
     except:
        continue
     script=re.compile(r'"raw_title":"(.*?)".*?"view_price":"(.*?)".*?"nick":"(.*?)"')
     x=script.findall(data)

     print(x)
