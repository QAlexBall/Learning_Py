# coding=utf-8
import requests
from requests import exceptions
from bs4 import BeautifulSoup
import time
#
# uselessPageURLs = ["https://channel.jd.com/", "https://www.baiduu.com", "https://m.jd.com/"]
# for url in uselessPageURLs:
#     try:
#         time.sleep(10)
#         r = requests.get(url,
#              headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
#         print(r.text)
#     except exceptions.HTTPError:
#         print("HTTPError!")
#     except exceptions.ConnectionError:
#         print("connectionError")
#
# print("OK")
def doRequestToURL(url):
    try:
        r = requests.get(url,
                   headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'})
        r.encoding = r.apparent_encoding
        goodsText = r.text
    except exceptions.ConnectionError:
        print("can't connect network!")
    except exceptions.SSLError:
        print("================SSLError=========================")
    return goodsText

targetUrl = "https://e.jd.com/ebook.html/"
goodsText = doRequestToURL(targetUrl)
soup = BeautifulSoup(goodsText, 'lxml')
if soup.findAll(name='meta', attrs={"name": "keywords"}):
    good_Id = targetUrl.split('/')[3].split('.')[0]
    print(good_Id)
    good_Name = soup.findAll(name='meta', attrs={"name": "keywords"})[0].attrs['content']
    pduid = 1540968060261294252038
    pduid += 1
    priceUrl = "https://p.3.cn/prices/mgets?pduid=" + str(pduid) + "&skuIds=J_" + str(good_Id)
    priceInfo = doRequestToURL(priceUrl)
    print(priceInfo)
    if priceInfo is not None:
        good_Price = priceInfo.split(":")[1].split(",")[0]