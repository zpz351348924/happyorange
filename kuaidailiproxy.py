# -*- coding: utf-8 -*-
""" ------------------------------------------------- File Name： demo_1.py.py Description : Python爬虫—破解JS加密的Cookie 快代理网站为例：http://www.kuaidaili.com/proxylist/1/ Document: Author : JHao date： 2017/3/23 ------------------------------------------------- Change Activity: 2017/3/23: 破解JS加密的Cookie ------------------------------------------------- """
__author__ = 'JHao'

import re
import PyV8
import urllib2
import time
import socket
import requests


def getHtml(url, cookie=None):
    header = {
        "Host": "www.kuaidaili.com",
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    html = requests.get(url=url, headers=header, timeout=30, cookies=cookie).content
    return html

def executeJS(js_func_string, arg):
    ctxt = PyV8.JSContext()
    ctxt.enter()
    func = ctxt.eval("({js})".format(js=js_func_string))
    return func(arg)

def parseCookie(string):
    string = string.replace("document.cookie='", "")
    clearance = string.split(';')[0]
    return {clearance.split('=')[0]: clearance.split('=')[1]}

def todict(alist):
    #['115.210.27.16', '9000', 'HTTP']
    adict ={}
    adict['http']=alist[0]+":"+alist[1]
    return adict


def remat(html):
    mat = re.compile('''<td data-title="IP">(.+?)</td>
                <td data-title="PORT">(.+?)</td>
                <td data-title="匿名度">(.+?)</td>
                <td data-title="类型">(.+?)</td>''')
    iplist = re.findall(mat,html)
    iplist2 =[]
    for i in iplist:
        list1 = list(i)
        del list1[2]
        list1dict = todict(list1)
        iplist2.append(list1dict)
    return iplist2
#print remat(html)
def checkip(proxyip):
    try:

        proxy = urllib2.ProxyHandler(proxyip)  # proxyip is dict
        opener = urllib2.build_opener(proxy)
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib2.install_opener(opener)
        response = urllib2.urlopen('http://ip.chinaz.com/getip.aspx').read()
        ip = proxyip
        print response
        return ip
    except Exception as e:
        print 'timeout...'


def saveip(pages=3):
    socket.setdefaulttimeout(3)
    with open('kuaidaili.txt','w') as f:
        for n in range(1,pages):
            TARGET_URL= "http://www.kuaidaili.com/proxylist/"+str(n)+"/"
            first_html = getHtml(TARGET_URL)
            js_func = ''.join(re.findall(r'(function .*?)</script>', first_html))
            js_arg = ''.join(re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', first_html))
            js_func = js_func.replace('eval("qo=eval;qo(po);")', 'return po')
            cookie_str = executeJS(js_func, js_arg)
            cookie = parseCookie(cookie_str)

            html = getHtml(TARGET_URL,cookie)
            iplist = remat(html)
            #print iplist
            for i in iplist:
                #print i
                ip = checkip(i)   # i = {'http': '183.31.216.171:9797'}
                if ip is not None:
                    f.write(str(ip)+"\n")
                    print ip
                time.sleep(3)
            print '%d ye done'%(n)
        print 'Done'

saveip()