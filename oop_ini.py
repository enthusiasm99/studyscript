class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('My name is ', self.name)

p = Person('Hardy')
p.say_hi()