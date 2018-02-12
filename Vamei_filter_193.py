def large100(a):
    if a > 100:
        return  True
    else:
        return False

for item in filter(large100, [10, 20, 50,101,200,300]):
    print(item, end = ' ')