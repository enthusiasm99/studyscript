import re

newsurl = "http://news.sina.com.cn/c/nd/2018-01-30/doc-ifyremfz2269397.shtml"

tempid = re.search('.doc-i(.+).shtml', newsurl)
print(tempid)
print(tempid.group())
print(tempid.group(0))
print(tempid.group(1))

newsid = tempid.group(1)
