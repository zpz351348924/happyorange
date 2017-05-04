import requests
from bs4 import BeautifulSoup
import pymongo
import time

client = pymongo.MongoClient('localhost',27017)
tongcheng58 = client['58tongcheng']
urls_list = tongcheng58['urls_list']
detail_list = tongcheng58['detail_list']

def get_all_links(channel_url,page=31,source=0):
    #http://nj.58.com/xiaomi/pn2/
    for uumb in range(1,page):
        url = '{}pn{}/'.format(channel_url,uumb)
        wb_data = requests.get(url)
        time.sleep(1.1)
        soup= BeautifulSoup(wb_data.text,'lxml')
        links = soup.select('td.t a.t')[6:-2]
        for link in links:
            url2 = link.get('href').split('?')[0]
            urls_list.insert_one({'url':url2})
            print(url2)

def get_detail(url):
    wb_data = requests.get(url)
    time.sleep(1)
    soup= BeautifulSoup(wb_data.text,'lxml')
    title= soup.title.text.strip()
    price = int(soup.select('span.price_now i')[0].text)
    area = soup.select('div.palce_li span i')[0].text
    detail_list.insert_one({'title':title,'price':price,'area':area})
    print(title,price,area)



if __name__ == '__main__':

    #get_all_links('http://nj.58.com/xiaomi/')
    #get_detail('http://zhuanzhuan.58.com/detail/757065680095444994z.shtml')
    out_url_from()
