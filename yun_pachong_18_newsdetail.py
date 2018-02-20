import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

def getCommentCount(newsurl):
    tempid = re.search('.doc-i(.+).shtml', newsurl)
    newsid = tempid.group(1)
    comments = requests.get(commentsURL.format(newsid))
    jd = json.loads(comments.text)
    #print(jd['result']['count']['show'])

def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('.main-title')[0].text
    time = soup.select('.time-source')[0].content[0].strip()
    result['dtime'] = datetime.strptime(time, '%Y年%m月%d日 %H:%M')
    result['source'] = soup.select('.source')[0].text
    result['articel'] = ' '.join([p.text.strip() for p in soup.select('#article p')[:-3]])
    result['editor']  = soup.select('.show_author')[0].text.lstrip('责任编辑：')
    result['comment']  = getCommentCount(newsurl)
    return result

commentsURL ="http://comment5.news.sina.com.cn/page/info?version=1&format=json\
&channel=gn&newsid=comos-{}&group=undefined\
&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3\
&t_size=3&h_size=3&thread=1"

news = "http://news.sina.com.cn/c/nd/2018-01-30/doc-ifyremfz2269397.shtml"
getNewsDetail(news)