import re

m = re.search("output_(\d{4})", "output_19862018.txt")

print(m.group(0))



import re
'''P131'''
m = re.search("output_(?P<year>\d{4})", "output_19862018")
print(m.group("year"))