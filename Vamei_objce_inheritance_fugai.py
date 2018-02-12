class Bird():
    def jiao(self):
        print('make sound')

class Chicken(Bird):
    def jiao(self, sound):
        super().jiao()
        print('jiji')


bird = Bird()
bird.jiao()

chicken = Chicken()
chicken.jiao()
