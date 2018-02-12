def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000

for i in gen():
    print(i)

def gen():
    i = 0
    while i < 10000:
        i = i + 1
        yield  i

for i in gen():
    print(i)