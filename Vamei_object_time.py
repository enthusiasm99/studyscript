import time

start = time.clock()
for i in range(100000):
    print(i**2)

end = time.clock()

print(end - start)