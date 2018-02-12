i    = 0
sum  = 500000
yh   = [0.01,0.02, 0.03, 0.035]
while sum > 0 :
    if i < 4:
        rate = yh[i]
    else:
        rate = 0.05
    sum = sum *( 1 + rate ) - 30000
    print("第", i+1 ,"年还剩" , int(sum) ,"元")
    i = i + 1
print("第", i,   "年终于还清了")


for item in iter([1,2]):
    print(item)

example_iter = iter([1, 2])
for item in example_iter:
    print(item)


import time
print(time.__name__)