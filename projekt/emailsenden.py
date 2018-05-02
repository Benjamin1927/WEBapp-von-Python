from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
import os

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


from_addr=input('Deine Email-Addresse bitte:')
to_addr=input('wer bekommt deine Email:')
password=input('geben Sie bitte ihre Passwort')
smtpaddr=input('smtpaddr bitte')

#需要将msg的主体定义为一个多部分的object
msg = MIMEMultipart()

#常规的形式
msg['From']=_format_addr('von deinem Freund<%s>'%from_addr)
msg['To']=_format_addr('geehrte <%s>'%to_addr)
msg['Subject']=Header('Begrussung von Python','utf-8').encode()

# msg.attach(MIMEText('die Emial wudr von Python beschrieben','plain','utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +'<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
with open('/Users/Benja/Documents/python 程序/ttp.png', 'rb') as f:
    #定义这个Base的类型

    # MIMEBase(),内部的参数分别为内容、类型：可以通过type获得的字符串
    mimeb=MIMEBase('image','png',filename='ttp')

    # 为这个object 添加Header
    mimeb.add_header('Content-Diposition','attachment',filename='Grossemauer.jpg')
    mimeb.add_header('Content-ID','<0>')
    mimeb.add_header('X-Attachment-ID','0')

    #把附件装在到MIMEBase上
    mimeb.set_payload(f.read())

    #需要将这个载体，装有附件的object用Base64编码
    #用的encoders是来自与email中的模块
    encoders.encode_base64(mimeb)
    msg.attach(mimeb)


#smtpaddr的端口需要根据outlook的官网来决定
server=smtplib.SMTP(smtpaddr,587)
server.set_debuglevel(1)
server.starttls()
server.login(from_addr,password)
#这里有个坑，as_string后面有个括号
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
