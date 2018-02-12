class Bird(object):
    def __init__(self, sound):
        self.sound = sound
        print("My sound is:", sound)

    def chirp(self):
        print(self.sound)


summer = Bird('ji')
summer.chirp()






class Bird:
    def __init__(self, sound):
        self.sound = sound
        print('My sound is ', sound)
    def jiao(self):
        print(self.sound)

winter = Bird('ji')
winter.jiao()


class Bird:
    def jiao(self, sound):
        print(sound)

    def re_jiao(self, sound, n):
        for i in range(n):
            self.jiao(sound)
summer = Bird()
summer.jiao("ji")
summer.re_jiao("ji", 10)













