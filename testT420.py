# print(type('word'))


# 函数示例
# 温度转换器
def fahrenheit_converter(C):
    fahrenheit = C * 9 / 5 + 32
    return str(fahrenheit) + 'F'


C2F = fahrenheit_converter(35)
print(C2F)


# 重量转换器
def weight_converter(g):
    weight = g / 1000
    return str(weight) + 'KG'


G2KG = weight_converter(2700)
print(G2KG)

# 求直角三角形斜边长
import math


def trangleC_len(A, B):
    trangleC = math.sqrt(A * A + B * B)
    return 'The right triangle third side\'s length is ' + str(trangleC)


C_len = trangleC_len(3, 4)
print(C_len)


# 类属性与实例属性
# 类属性变化，实例属性是否会跟着变化？----打印结果为42，即会跟着变化

class TestA:
    attr = 1


obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)


# 实例属性被赋值，是否会影响到类属性的引用？--------打印结果为1，即不会影响

class TestA:
    attr = 1


obj_a = TestA()
obj_b = TestA()

obj_a.attr = 42
print(obj_b.attr)


####
class TestA:
    attr = 1

    def __init__(self):
        self.attr = 42


obj_a = TestA()
print(obj_a.attr)

obj1 = 1
obj2 = 'string'
obj3 = []
obj4 = {}
print(type(obj1), type(obj2), type(obj3), type(obj4))


class Bird(object):
    def __init__(self, sound):
        self.sound = sound
        print('My sound is ',  sound)

    def jiao(self):
        print(self.sound)

summer = Bird('ji')
summer.jiao()


def outer():
    def inner():
        print("Inside inner")
    return inner

foo = outer()
foo
foo()