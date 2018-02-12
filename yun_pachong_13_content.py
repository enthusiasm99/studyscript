import requests
from bs4 import BeautifulSoup
from datetime import datetime

res = requests.get("http://news.sina.com.cn/c/nd/2018-01-30/doc-ifyremfz2269397.shtml")
res.encoding = 'utf-8'
'''print(res.text)'''
soup = BeautifulSoup(res.text, 'html.parser')

article = []
'''print(soup.select('#article p')[:-3])'''
'''[:-n]去掉最后n个P'''
for p in soup.select('#article p')[:-3]:
    article.append(p.text.strip())
'''方法用于移除字符串头尾指定的字符（默认为空格）'''

' '.join(article)
'''article中的段落用空格隔开'''
print(article)


'''
   上面一段语句可以只用一行表示
print(' '.join([p.text.strip() for p in soup.select('#article p')[:-3]]))

'''