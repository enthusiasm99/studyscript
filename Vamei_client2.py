import http.client

conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET", "/vamei")
response = conn.getresponse()
print(response.status, response.reason)

content = str(response.read())
'''content = content.split("\n")'''

print(content)