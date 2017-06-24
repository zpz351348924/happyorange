import requests
from bs4 import BeautifulSoup
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ganji = client['ganjispider']
urls_list = ganji['urls_list']
detail_list = ganji['detail_list']


headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    'Cookie':'ganji_login_act=1493868030023; citydomain=bj; ganji_xuuid=3770cdcd-0a32-4a6d-8ddf-c2d3503f6140.1493868030250; ganji_uuid=5062040362043394936492; __utmt=1; __utma=32156897.424260824.1493868030.1493868030.1493868030.1; __utmb=32156897.1.10.1493868030; __utmc=32156897; __utmz=32156897.1493868030.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); webimverran=60; GANJISESSID=ffad2356ae923ea4b86327e2db235719; als=0; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A40830318130%7D; 58uuid=690ebb93-16ab-4d07-a9f7-149cecef48ae; new_session=0; init_refer=http%253A%252F%252Fbj.ganji.com%252Fwu%252F; new_uv=1; lg=1'
}

def get_all_url(urls,page=30):
    for i in range(1,page):
        url = '{}o{}/'.format(urls,i)
        wb_data = requests.get(url,headers=headers)
        time.sleep(1)
        soup = BeautifulSoup(wb_data.text,'lxml')
        links = soup.select('td.t a')
        if len(links) != 0:
            for link in links:
                url = link.get('href').split('?')[0]
                url2={'url':url}
                if 'detail' in url.split('/'):
                    print(url)
                    urls_list.insert_one(url2)
                else:
                    pass
            print('{}done......'.format(i))
        else:
            break

def get_all_detail(url):
    try:
        wb_data = requests.get(url,headers=headers)
        time.sleep(1)
        soup = BeautifulSoup(wb_data.text,'lxml')
        title = soup.select('h1.info_titile')[0].text
        if len(title) != 0:
            price = soup.select('span.price_now i')
            area = soup.select('div.palce_li span i')
            data = {
                'title':title,
                'price':int(price[0].text),
                'area':area[0].text,
                'url':url
            }
            print(data)
            detail_list.insert_one(data)
        else:
            pass
            print('商品已经下架')
    except ValueError as e:
        pass




if __name__ == '__main__':
    url= 'http://zhuanzhuan.ganji.com/detail/859964898620473357z.shtml'
    #get_all_url(url)
    get_all_detail(url)