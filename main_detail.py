from url_and_detail import get_all_detail,detail_list,urls_list
from multiprocessing import Pool

db_list = [item['url'] for item in urls_list.find()]
overtiem_list=[item['url'] for item in detail_list.find()]
x = set(db_list)
y = set(overtiem_list)
rest_of_url = x - y
#断点续爬


def main():
    a = [item['url'] for item in urls_list.find()]
    pool=Pool()
    pool.map(get_all_detail,a)

def main_go_on():
    pool = Pool()
    pool.map(get_all_detail, rest_of_url)

if __name__ == '__main__':
    #main()
    main_go_on()

