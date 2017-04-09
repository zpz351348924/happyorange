# -*- coding: utf-8 -*-
""" ------------------------------------------------- File Name： demo_1.py.py Description : Python爬虫—破解JS加密的Cookie 快代理网站为例：http://www.kuaidaili.com/proxylist/1/ Document: Author : JHao date： 2017/3/23 ------------------------------------------------- Change Activity: 2017/3/23: 破解JS加密的Cookie ------------------------------------------------- """
__author__ = 'JHao'

import re
import PyV8
import requests

TARGET_URL = "http://www.kuaidaili.com/proxylist/1/"

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

# 第一次访问获取动态加密的JS
first_html = getHtml(TARGET_URL)

# first_html = """
# <html><body><script language="javascript"> window.onload=setTimeout("lu(158)", 200); function lu(OE) {var qo, mo="", no="", oo = [0x64,0xaa,0x98,0x3d,0x56,0x64,0x8b,0xb0,0x88,0xe1,0x0d,0xf4,0x99,0x31,0xd8,0xb6,0x5d,0x73,0x98,0xc3,0xc4,0x7a,0x1e,0x38,0x9d,0xe8,0x8d,0xe4,0x0a,0x2e,0x6c,0x45,0x69,0x41,0xe5,0xd0,0xe5,0x11,0x0b,0x35,0x7b,0xe4,0x09,0xb1,0x2b,0x6d,0x82,0x7c,0x25,0xdd,0x70,0x5a,0xc4,0xaa,0xd3,0x74,0x98,0x42,0x3c,0x60,0x2d,0x42,0x66,0xe0,0x0a,0x2e,0x96,0xbb,0xe2,0x1d,0x38,0xdc,0xb1,0xd6,0x0e,0x0d,0x76,0xae,0xc3,0xa9,0x3b,0x62,0x47,0x40,0x15,0x93,0xb7,0xee,0xc3,0x3e,0xfd,0xd3,0x0d,0xf6,0x61,0xdc,0xf1,0x2c,0x54,0x8c,0x90,0xfa,0x24,0x5b,0x83,0x0c,0x75,0xaf,0x18,0x01,0x7e,0x68,0xe0,0x0a,0x72,0x1e,0x88,0x33,0xa7,0xcc,0x31,0x9b,0xf3,0x1a,0xf2,0x9a,0xbf,0x58,0x83,0xe4,0x87,0xed,0x07,0x7e,0xe2,0x00,0xe9,0x92,0xc9,0xe8,0x59,0x7d,0x56,0x8d,0xb5,0xb2,0x6c,0xe0,0x49,0x73,0xfc,0xe7,0x20,0x49,0x34,0x09,0x71,0xeb,0x60,0xfd,0x8e,0xad,0x0f,0xb9,0x2e,0x77,0xdc,0x74,0x9b,0xbf,0x8f,0xa5,0x8d,0xb8,0xb0,0x06,0xac,0xc5,0xe9,0x10,0x12,0x77,0x9b,0xb1,0x19,0x4e,0x64,0x5c,0x00,0x98,0xc6,0xed,0x98,0x0d,0x65,0x11,0x35,0x9e,0xf4,0x30,0x93,0x4b,0x00,0xab,0x20,0x8f,0x29,0x4f,0x27,0x8c,0xc2,0x6a,0x04,0xfb,0x51,0xa3,0x4b,0xef,0x09,0x30,0x28,0x4d,0x25,0x8e,0x76,0x58,0xbf,0x57,0xfb,0x20,0x78,0xd1,0xf7,0x9f,0x77,0x0f,0x3a,0x9f,0x37,0xdb,0xd3,0xfc,0x14,0x39,0x11,0x3b,0x94,0x8c,0xad,0x8e,0x5c,0xd3,0x3b];qo = "qo=251; do{oo[qo]=(-oo[qo])&0xff; oo[qo]=(((oo[qo]>>4)|((oo[qo]<<4)&0xff))-0)&0xff;} while(--qo>=2);"; eval(qo);qo = 250; do { oo[qo] = (oo[qo] - oo[qo - 1]) & 0xff; } while (-- qo >= 3 );qo = 1; for (;;) { if (qo > 250) break; oo[qo] = ((((((oo[qo] + 200) & 0xff) + 121) & 0xff) << 6) & 0xff) | (((((oo[qo] + 200) & 0xff) + 121) & 0xff) >> 2); qo++;}po = ""; for (qo = 1; qo < oo.length - 1; qo++) if (qo % 5) po += String.fromCharCode(oo[qo] ^ OE);eval("qo=eval;qo(po);");} </script> </body></html>
# """

# 提取其中的JS加密函数
js_func = ''.join(re.findall(r'(function .*?)</script>', first_html))

print 'get js func:\n', js_func

# 提取其中执行JS函数的参数
js_arg = ''.join(re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', first_html))

print 'get ja arg:\n', js_arg

# 修改JS函数，使其返回Cookie内容
js_func = js_func.replace('eval("qo=eval;qo(po);")', 'return po')

# 执行JS获取Cookie
cookie_str = executeJS(js_func, js_arg)

# 将Cookie转换为字典格式
cookie = parseCookie(cookie_str)

print cookie

# 带上Cookie再次访问url,获取正确数据
print getHtml(TARGET_URL, cookie)
