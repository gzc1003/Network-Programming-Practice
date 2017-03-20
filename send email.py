from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
from email import encoders

from_addr=input('From:')
password=input('Password:')
smtp_server=input('SMTP server:')
to_addr=input('To:')
#to_addr1=input('To')

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


msg=MIMEMultipart()
msg['From']=_format_addr('人工智能<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']= 'Greeting from the Samaritan'

msg.attach(MIMEText('<html><body><h1>Samaritan says hello!</h1>'+
    '<p><img src="cid:0"></p>'+
    '</body></html>', 'html', 'utf-8'))

with open('D:\hh.png','rb') as f:
    mime=MIMEBase('image', 'png')
    mime.add_header('Content-Disposition', 'attachment',filename='test.png')
    mime.add_header('Content-ID', '<0>')
    #mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server=smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

