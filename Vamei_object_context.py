f = open("abc.text","w")
print(f.closed)
f.write("Hello world")
f.close()
print(f.closed)


with open("abc.text", "w") as g:
    g.write("22222")

'''print(g.readlines())'''
print(g.closed)

class Vow:
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.text = "I say:" + self.text
        return  self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text = self.text + "!"

with Vow("I'm fine") as myVow:
    print(myVow.text)

print(myVow.text)