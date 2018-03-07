from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']
item_info = ceshi['item_info3']

#spider 1

# def get_links_from(channel,pages,who_sells=0):
#     list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
#     wb_data = requests.get(list_view)
#     time.sleep(1)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     if soup.find('td','t'):     #如果有td标签和t标签，则继续操作
#         for link in soup.select('td.t a.t'):
#             item_link = link.get('href').split('?')[0]
#             url_list.insert_one({'url':item_link})
#             print(item_link)
#     else:
#         pass



def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist = 'logonew.gif' in soup.find('img').get('src').split('/')
    if not no_longer_exist:
        title = soup.title.text
        try:
            price_now = soup.select('span.price_now > i')[0].text + '元' #if soup.find_all('span.price_now > i') else url +'出错'
        except IndexError:
            pass
        price_ori = soup.select('span.price_now > b.price_ori')[0].text[3:] if soup.find_all('span.price_now > b.price_ori') else '无'
        try:
            area = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')[0].text
        except IndexError:
            pass
        try:
            item_info.insert_one({'title':title,'price_now':price_now,'price_ori':price_ori,'area':area})
        except UnboundLocalError:
            pass

        #print({'title':title,'price_now':price_now,'price_ori':price_ori,'area':area})


count =0
for i in url_list.find({},{"url":1,"_id":0}):
    for value in i.values():
        get_item_info(value)
        count += 1
        print('当前是第%d/共27182条记录' %count)
print('完成')
#print(url_list.find().count())   #打印url_list中记录总数





