import requests
from bs4 import BeautifulSoup
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    'Cookie':'ganji_login_act=1493868030023; citydomain=bj; ganji_xuuid=3770cdcd-0a32-4a6d-8ddf-c2d3503f6140.1493868030250; ganji_uuid=5062040362043394936492; __utmt=1; __utma=32156897.424260824.1493868030.1493868030.1493868030.1; __utmb=32156897.1.10.1493868030; __utmc=32156897; __utmz=32156897.1493868030.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webimverran=60; GANJISESSID=ffad2356ae923ea4b86327e2db235719; als=0; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A40830318130%7D; 58uuid=690ebb93-16ab-4d07-a9f7-149cecef48ae; new_session=0; init_refer=http%253A%252F%252Fbj.ganji.com%252Fwu%252F; new_uv=1; lg=1'
}

def get_channel_url(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('dl.fenlei dt a')
    for link in links:
        url = 'http://bj.ganji.com{}'.format(link.get('href'))
        print(url)


if __name__ == '__main__':
    url = 'http://bj.ganji.com/wu/'
    #get_channel_url(url)

channelurl = """
http://bj.ganji.com/jiaju/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/shouji/
http://bj.ganji.com/shoujihaoma/
http://bj.ganji.com/bangong/
http://bj.ganji.com/nongyongpin/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/ershoubijibendiannao/
http://bj.ganji.com/ruanjiantushu/
http://bj.ganji.com/yingyouyunfu/
http://bj.ganji.com/diannao/
http://bj.ganji.com/xianzhilipin/
http://bj.ganji.com/fushixiaobaxuemao/
http://bj.ganji.com/meironghuazhuang/
http://bj.ganji.com/shuma/
http://bj.ganji.com/laonianyongpin/
"""

channel_url_list = channelurl.split()
#print(channel_url_list)