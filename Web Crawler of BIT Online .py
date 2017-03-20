from urllib import request,parse
from http import cookiejar
import re
url='https://login.bit.edu.cn/cas/login'
req=request.Request(url)


req.add_header('Host','login.bit.edu.cn')
req.add_header('Origin','https://login.bit.edu.cn')
req.add_header('Referer','https://login.bit.edu.cn/cas/login?service=http%3A%2F%2Fonline.bit.edu.cn%2Fccs%2Fehome%2Findex.do')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')

cookie=cookiejar.CookieJar()
handler=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(handler)

op=opener.open(req)
data=op.read().decode()
lt_re=re.compile('name="lt" value="(.*?)"')
x=lt_re.findall(data)
execution_re=re.compile('name="execution" value="(.*?)"')
y=execution_re.findall(data)



login_data=parse.urlencode([
    ('username','2120150113'),
    ('password','8800956guozichun'),
    ('lt',x[0]),
    ('execution',y[0]),
    ('_eventId','submit'),
    ('rmShown','1')])
op=opener.open(req,login_data.encode())
op=opener.open('http://online.bit.edu.cn/ccs/euser/profile.do?content=campus')
data=op.read().decode()

name_re=re.compile('<a class="name"\r\n *href="/ccs/euser/profile.do\?uid=1349214">(.*?)</a>')
name=name_re.findall(data)
print(name)

