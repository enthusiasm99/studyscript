import requests
from bs4 import BeautifulSoup
from datetime import datetime

res = requests.get("http://news.sina.com.cn/c/nd/2018-01-30/doc-ifyremfz2269397.shtml")
res.encoding = 'utf-8'
    #print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

editor = soup.select('.show_author')[0].text.lstrip('责任编辑：')
    #lstrip('责任编辑：')  从左边移除'责任编辑：'的内容
print(editor)