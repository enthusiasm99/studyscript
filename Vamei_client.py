import http.client

conn = http.client.HTTPConnection("www.example.com")

conn.request("GET", "/")
response = conn.getresponse()

print(response.status, response.reason)

content = response.read()

print(content)