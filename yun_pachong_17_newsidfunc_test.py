import re
import requests
import json

commentsURL ="http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gj&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1"
#*************************************************************************************15中此处为gn

def getCommentCount(newsurl):
    tempid = re.search('.doc-i(.+).shtml', newsurl)
    newsid = tempid.group(1)
    comments = requests.get(commentsURL.format(newsid))
    jd = json.loads(comments.text)
    print(jd['result']['count']['show'])

news = "http://news.sina.com.cn/w/zx/2018-02-11/doc-ifyrmfmc1382793.shtml"
getCommentCount(news)



