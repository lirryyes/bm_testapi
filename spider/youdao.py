import requests
from bs4 import BeautifulSoup
import json
import re

class GetData:
    @classmethod
    def getData(cls):
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        url='http://www.cntour.cn/'
        # proxies={
        #     "http":"http://10.1.159.174:8888",
        #     "https":"http://10.10.1.10:1080"
        #     ,
        # }
        #response = requests.get(url, proxies=proxies)
        strhtml=requests.get(url,headers=headers)
        soup=BeautifulSoup(strhtml.text,'lxml')
        data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
        a = []
        b = {}
        for item in data:
            b["code"] = 20000
            result={
                'name':item.get_text(),
                'link':item.get('href')
            }
            a.append(result)
            b["data"] = a
            c = json.dumps(b,ensure_ascii=False)
        print(c)
        return b

    @classmethod
    def getLogin(cls):
        a = ['admin','admin']
        return a

