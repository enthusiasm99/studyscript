from bs4 import BeautifulSoup
html_sample = """
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>

<body>
<h1 id ="title">Hello World</h1>
</body>
</html>"""

soup = BeautifulSoup(html_sample, 'html.parser')
header = soup.select('h1')
print(header)
print(header[0])
print(header[0].text)

"""
print(type(soup))
print(soup.text)
"""