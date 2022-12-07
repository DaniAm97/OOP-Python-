from abc import ABC,abstractmethod
class Animal(ABC):
    __name = ''

    def __init__(self):
        self.time = 0

    def sleep(self, time):
        self.time = time
        print('sleep in hours: ' + str(self.time))

    def makesound(self,sound):
        self.sound = sound
        print(self.sound)

    @abstractmethod
    def move(self):
        pass




