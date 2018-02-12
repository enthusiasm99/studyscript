class Bird:
    feather = True
    reproduction = 'egg'
    def jiao(self, sound):
        print(sound)

class Chicken(Bird):
    how_to_move =  'walk'
    edible = True

class Swan(Bird):
    how_to_move = 'swim'
    edible = False

summer = Chicken()
print(summer.feather)
summer.jiao('jijiji')


