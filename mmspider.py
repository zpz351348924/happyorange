import os
import time
import urllib
import urllib.request
import re

#url = "http://jandan.net/ooxx/page-2421#comments"
def open_url(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    res = urllib.request.Request(url = url, headers=headers)
    html = urllib.request.urlopen(res).read()
    #print(html)
    return html

def get_page(url):
    #url = "http://jandan.net/ooxx/page-2421#comments"
    html = open_url(url).decode('utf-8')
    return html


#<a href="http://jandan.net/ooxx/page-2421#comment-3416866">3416866</a></span><p><a href="//wx1.sinaimg.cn/large/005vbOHfgy1feau79zrejj30sg0iz77z.jpg"
#<a href="//wx1.sinaimg.cn/large/005vbOHfgy1feau79zrejj30sg0iz77z.jpg"
def findimg(html):
    ms = re.compile('<a href="//(.+?).jpg"')
    mat = re.findall(ms, html)
    #print(mat)
    return mat
#findimg(html)

def saveimg(matlist):

    number = 1
    for each in matlist:
        imgaddres= "http://" + str(each) + '.jpg'
        #print(imgaddres)
        httml = open_url(imgaddres)
        filename = str(each[-5:]) + '.jpg'
        print(number)
        time.sleep(0.5)
        with open(filename, 'wb') as f:
            number +=1
            f.write(httml)

def xiazai(pages=3):
    url = "http://jandan.net/ooxx/page-2418#comments"
    wenjianjianame = "mm"
    os.makedirs(wenjianjianame)
    os.chdir(wenjianjianame)
    count = 0


    for i in range (pages):


        urlnumb = re.compile("http://jandan.net/ooxx/page-(.+?)#comments")
        msnumb = re.findall(urlnumb, url)
        msnumb = int(str(msnumb[0])) - i
        urls = "http://jandan.net/ooxx/page-"+ str(msnumb)+"#comments"
        mat = findimg(get_page(urls))
        saveimg(mat)
        count+=1
        print('第%d页保存完毕' %(count))

        time.sleep(3)
    print('Done')

xiazai()
