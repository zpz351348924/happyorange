from channel_url_get import channel_url_list
from url_and_detail import get_all_url,urls_list
from multiprocessing import Pool




def main():
    pool = Pool()
    pool.map(get_all_url,channel_url_list)
    #print(channelurl.split())

if __name__ == '__main__':
    main()
