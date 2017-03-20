
import urllib.request
import re


def savefile(data):
    save_path='D:/b.txt'
    f_obj=open(save_path,'ab')
    f_obj.write(data)
    f_obj.close()



from collections import deque

queue=deque()
visited=set()

url='http://www.sdpc.gov.cn/'

queue.append(url)
count=0

while queue:
    url=queue.popleft()
    visited|={url}
    print('已经抓取:'+str(count)+'正在抓取<----'+url)
    count+=1

    try:
        req=urllib.request.Request(url)
        req.add_header('User-Agent',
             'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36)')

        urlop=urllib.request.urlopen(req,timeout=10)
    except:
        continue
    
    if 'html' not in urlop.getheader('content-type'):
        continue

    try:
        data=urlop.read().decode('utf-8','ignore')
        dat=data.encode('gbk','ignore')
        savefile(dat)
    except:
        continue
    linkre=re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http'in x and x not in visited:
            queue.append(x)
            print('加入队列 --->  ' + x)





