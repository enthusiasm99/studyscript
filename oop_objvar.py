# coding = UTF-8
class Robot:
    """表示有一个带有名字的机器人。"""


    #一个类变量，用来记录机器人的数量
    population = 0

    def __init__(self, name):
        #初始化数据
        self.name = name
        print("(Initialization {})".format(self.name))

        #当有人创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} is the last one.".format(self.name))
        else:
            print("There are still {} robots  working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候"""
        print("Greetings, my master call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
print(Robot.say_hi.__doc__)
droid1.say_hi()

Robot.how_many()

droid2 = Robot("C-3P0")
print(Robot.say_hi.__doc__)
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here. \n")

print("Robot have finished their work. So let's destroy them.")

droid1.die()
droid2.die()

Robot.how_many()






