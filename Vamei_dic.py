example_dic = {"a":1, "b":2}
print(type(example_dic))

for key in example_dic.keys():
    print(example_dic[key])


for v in example_dic.values():
    print(v)

for k, v in example_dic.items():
    print(k, v)