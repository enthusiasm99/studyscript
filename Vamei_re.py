import re

m = re.search("[0-9]", "0a1b2c3d4e5f6")
print(m.group(0))

