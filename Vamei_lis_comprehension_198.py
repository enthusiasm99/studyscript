list1 = [1, 3, 5, 6, 7]
list2 = [9, 12, 13, 11, 8]

l = [x**2 for(x, y) in zip(list1, list2) if y > 10]

for item in l:
    print(item)


d = {k:v for k,v in enumerate("Vamei") if val not in "Vi"}
print(d)