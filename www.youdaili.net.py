import urllib
import re
import urllib.request
import socket
import time

"""


"""
def get_page():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url='http://www.youdaili.net/Daili/http/36717.html', headers=headers)
    request = urllib.request.urlopen(req)
    html = request.read().decode('utf-8')
    #print(html)
    return html
#get_page()

def alliplist(html):
    """<p>115.220.150.170:808@HTTP#浙江省宁波市 电信</p>"""
    mat = re.compile("<p>(.+?)@HTTP#(.+?)</p>")
    match = mat.findall(html)
    #print(match)
    return match
#alliplist(get_page())


def to_iplist(alliplists):   #将上述列表转换成单独IP+端口列表
    iplist = []
    lengs = len(alliplists)
    for i in range(lengs):
        ilist = list(alliplists[i])
        del ilist[1]
        iplist.append(ilist[0])
    return iplist
#to_iplist([('211.151.144.188:80', 'xxxxx'), ('115.220.150.170:808', 'xxxx')])
#['211.151.144.188:80', '115.220.150.170:808']

def ipcheck(iplist):
    zhaiip = []
    lengss = len(iplist)
    for i in range(lengss):
        strip = str(iplist[i])
        print(strip, " >>>>开始检测是否可用....")

        socket.setdefaulttimeout(5)
        proxy = urllib.request.ProxyHandler({"http":strip}) #strip is '211.151.144.188:80'
        opener = urllib.request.build_opener(proxy)
        opener.addheaders= [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")]
        urllib.request.install_opener(opener)
        try:
            resp = urllib.request.urlopen('http://ip.chinaz.com/getip.aspx').read().decode('utf-8')

            matchs = re.findall(strip[:-5],resp)
            #print(resp)
            if matchs:
                print(resp)
                zhaiip.append(strip)
            else:
                print('htmlpage is wrong,不可用')

        except Exception:
            print('this ip is useless...')
    print(zhaiip)
    return zhaiip
#print(ipcheck('121.40.42.35:9999'))


html = get_page()
matchs = alliplist(html)
youdaili = to_iplist(matchs)

keyongip = ipcheck(youdaili)
with open('youdaili.txt','w') as f:
    f.write(str(keyongip))

