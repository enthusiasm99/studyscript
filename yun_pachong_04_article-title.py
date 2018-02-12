import requests
from bs4 import BeautifulSoup
from datetime import datetime

res = requests.get("http://news.sina.com.cn/c/nd/2018-01-30/doc-ifyremfz2269397.shtml")
res.encoding = 'utf-8'
'''print(res.text)'''
soup = BeautifulSoup(res.text, 'html.parser')

'''print(soup.select('.main-title')[0].text)
print(soup.select('.date')[0].text)
print(soup.select('.source')[0].text)'''

title = soup.select('.main-title')[0].text
time = soup.select('.date')[0].text
dt = datetime.strptime(time, '%Y年%m月%d日 %H:%M')
source = soup.select('.source')[0].text


print(source, dt, title)

'''
如果链接网址、时间在一个“  class = "time-source" ”中，则要用到coutents[0].strip方法

1.取时间来源
timesource = soup.select('.time-source')[0].content[0].strip()
    content[0]输出list中的第1个结果：
       2018年2月3日 12:18:23 \t\t
    content[0].strip()输出结果为 str字符串格式：
       2018年2月3日 12:18:23

from datetime import datetime
dt datetime.strptime(timesource, '%Y年%m月%d日 %H:%M:%S')
   STR转TIME strptime  反之则 strftime

2.取网址名称
soup.select('.time-source' span a)[0].text
'''
