#coding=utf-8
import requests
from bs4 import BeautifulSoup

url = "http://news.qq.com/"
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'lxml')
news_titles = soup.select("div.text > em.f14 > a.linkto")
file = open(r'/Python项目/爬取腾讯新闻/news.txt', 'w')
for i in news_titles:
    title = i.get_text()
    link = i.get("href")
    data = {
        '标题':title,
        '链接':link
    }
    file.write(str(data) + '\n')
    print(data)
print("保存成功，已保存为12342.txt")
#print(wbdata)
