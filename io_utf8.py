# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")

# f.write(u"Imagine no-English language here")
f.write(u"想像这是没有使用英语")
f.close()

text = io.open("abc.txt", encoding='utf-8').read()
print(text)