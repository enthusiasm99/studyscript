class Bird:
    feather = True
    def chirp(self):
        print("some sound")

class Chicken(Bird):
    fly = True
    def __init__(self, age):
        self.age = age

    def chirp(self):
        print("ji")

summer = Chicken(2)


print("===>summer")
print(summer.__dict__)

print("===>Chicken")
print(Chicken.__dict__)

print("===>Bird")
print(Bird.__dict__)