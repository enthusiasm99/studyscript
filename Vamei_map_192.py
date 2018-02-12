def square_sum(x, y):
    return x**2 + y**2

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

result = map(square_sum, list1, list2)

for item in result:
    print(item, end = ' ')



list = [1, 2, 4, 6]

result2 = map(lambda x:x+3, list)
for item2 in result2:
    print(item2, end = '\\')