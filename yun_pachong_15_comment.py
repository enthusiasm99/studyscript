import requests
import json

comments = requests.get("http://comment5.news.sina.com.cn/page/info?version=1&format=json\
&channel=gn&newsid=comos-fyremfz2269397&group=undefined\
&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3\
&t_size=3&h_size=3&thread=1")

jd = json.loads(comments.text)

print(jd['result']['count']['show'])
#在chrome中，查看页面的preview,按缩进目录找