import urllib2
import re
import urllib
import socket
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
referer='http://www.xicidaili.com'
headers={"User-Agent":user_agent,'Referer':referer}
req = urllib2.Request(url='http://www.xicidaili.com/', headers=headers)
request = urllib2.urlopen(req)
html = request.read().decode('utf-8').encode('utf-8')
#print html

'''
<td>175.155.231.77</td>
    <td>808</td>
    <td>sichuan</td>
    <td class="country">gaoni</td>
    <td>HTTP</td>
  </tr>
  
  <p>220.189.249.80:80@HTTP#zj dx</p>


'''



def ipscrtch(msg):
    matching = re.compile('''<td>(.+?)</td>
    <td>(.+?)</td>
    <td>(.+?)</td>
    <td class="country">(.+?)</td>
    <td>(.+?)</td>''')
    result = matching.findall(msg)
    return result

#print iplist1


def  urllib2proxy(proxyip):
    try:
        proxy = urllib2.ProxyHandler(proxyip) #proxyip is dict
        opener = urllib2.build_opener(proxy)
        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)")]
        urllib2.install_opener(opener)
        response = urllib2.urlopen('http://ip.chinaz.com/getip.aspx').read()
        print 'sucess done'
        return response
    except Exception as e:
        print 'this ip is useless....'


def list2dict(iplist):
    adict = {}
    # ['180.76.137.46', '8080', 'HTTP']
    # {'HTTP': '180.76.137.46:8080'}
    iplist = [s.lower() for s in iplist]
    adict[iplist[2]] = iplist[0] + ":"+iplist[1]
    return adict
#print list2dict(['180.76.137.46', '8080', 'HTTP'])


def listyuanzu(alist):
    list3 = []
    socket.setdefaulttimeout(3)
    count = 0
    f = open('proxy.txt', 'w')
    for each in alist:
        list2 = list(each)
        del list2[2]
        del list2[2]
        ipdict = list2dict(list2)
        try:
            #url = "http://ip.chinaz.com/getip.aspx"
            #proxy_host = list2[2]+"://" + list2[0] + ":" + list2[1]
            #proxyer = {list2[2]: proxy_host}
            #res = urllib.urlopen(url, proxies=proxyer).read()

            res = urllib2proxy(ipdict)
            #print res

            #testiphtml = urllib2proxy(ipdict)
            strlist = list2[0]
            matchs = re.findall(strlist, res)
            if matchs:
                list3.append(list2)
                f.write(str(list2) + '\n')
                count += 1
                print count
                print matchs

        except Exception,e:
            print 'timeout....'
            continue

    f.close()
    print list3
    numb = len(list3)
    print 'it is done'
    print "there are %d" %(numb)

iplist1 = ipscrtch(html)
listyuanzu(iplist1)



