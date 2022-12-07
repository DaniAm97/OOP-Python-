from animal import Animal
class Bird(Animal):

    def __init__(self, km):
        self.__km = km
        super().__init__()



    def bird_make_sound(self):
        print(super().makesound("lalalal"))

    def fly(self):

        print(f'this bird can fly {self.__km} hours without stoping')

    def move(self):
        print('bird move')


