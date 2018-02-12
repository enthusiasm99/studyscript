import requests
from bs4 import BeautifulSoup

res = requests.get("http://news.sina.com.cn/china/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.select('.news-item'):
    '''原html中  <div class="news-item"> ，
       发现news-item前为‘class’，
       则在上句中用 . 表示
       若前面为 id=   ， 则用#'''
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        time =  news.select('.time')[0].text
        a  = news.select('a')[0]['href']
        print(time, h2, a)
