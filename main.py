from multiprocessing import Pool
from channel_extraction import channel_list
from page_parsing import get_links_from


def get_all_links_from(channel):
    for num in range(1,101):
        get_links_from(channel,num)


def get_all_item_info(url):

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from,channel_list.split())
