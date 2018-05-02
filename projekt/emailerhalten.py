import poplib
from email.parser import Parser #将得到的lines组合成的text分析并且标记，然后可以用于后续的文本分析（该方法返回一个具有各种method的instance）
from email.header import decode_header#解码Header,返回一个list
from email.utils import parseaddr#分析地址

def decode_str(s):#使用decode_header函数分析header，获得内容和编码方式
    value,charset=decode_header(s)[0]
    if charset:
        value=value.decode(charset)
    return value


def guess_charset(msg):
    #尝试获取编码类型
    charset=msg.get_charset()
    print('hier ist charset::',charset)
    if charset is None: #如果找不到的话从msg属性中寻找。
        #content_type 是一个string
        content_type=msg.get('Content-Type','').lower()
        print('hier ist content_type::',content_type)
        pos=content_type.find('charset=')#得到的是该字符串的首字母的index
        if pos>=0:
            #content_type已经是字符串了，8代表charset=，这几个字符的长度
            charset=content_type[pos+8:].strip()#脱去空格\r\n\t等字符
    return charset


def print_info(msg,indent=0):
    if indent==0:
        #所有获取来的信息都是经过编码的，所以都需要decode
        for headers in ['From','To','Subject']:
            value=msg.get(headers,'')
            if headers=='Subject':
                value=decode_str(value)
            else:
                name,addr=parseaddr(value)
                name=decode_str(name)
                value='%s<%s>'%(name,addr)
            print('%s%s:%s'%('  '*indent,headers,value))
    if msg.is_multipart():
        parts=msg.get_payload()
        #get_payload是获得不带有这个层级载体的内容。但是他的每一个元素，仍旧带有载体。
        #因此即便是最后一层了，在下面的else中还是需要再用一次get_payload去获得内容，然后分析
        for n,part in enumerate(parts):
            print('%spart%d' % ('   '*indent, n))
            print('%s-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'%'   '*indent)
            print_info(part,indent+1)
    else:
        content_type=msg.get_content_type()
        if content_type=='text/html' or content_type=='text/plain':
            content=msg.get_payload(decode=False)
            charset=guess_charset(msg)#需要从头文件中获取这些信息

            print('是否需要base64之外的解码方式！？%s'%content)
            if charset:
                content=content.decode(charset)
            print('%sText:%s'%('    '*indent,content+'....'))
        else:
            print('%sAttachment%s'%('   '*indent,content_type))

# emailaddr=input('deine Email Addresser bitte:')
# mailboxpw=input('dein Email password bitte:')
# popaddr=input('POP-Serveraddresse bitte:')

server = poplib.POP3_SSL('smtp-mail.outlook.com')
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user('benjamin_1927@outlook.com')
server.pass_('')

print('Msg: %s size: %s' %server.stat())

resp,mails,octets=server.list()
print('hier ist resp %s' %resp)#一组字符串
print('hier ist mailslist %s'%mails)#主体，邮件的序号和编号（可能是服务器内部是索引吧）
print('hier ist octets%s'%octets)#一组数字

index=len(mails)
resp,lines,octets=server.retr(index)#取回的是最新的一份邮件
#邮件的编码是，最新的编码在最后。

text=b'\r\n'.join(lines)
print('hier ist Text ohne UTF-8\n',text)

text = b'\r\n'.join(lines).decode('utf-8')

print('\nhier ist texte\n',text)
print('hier ist meg\n----------- ', type(text))

msg=Parser().parsestr(text)

print('hier ist meg\n----------- ',type(msg))

server.close()

print_info(msg)
