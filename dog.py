from animal import Animal
class Dog(Animal):

    def __init__(self, km):
        self.km = km
        super().__init__()

    def run(self):
        print(f'dog run km : {self.km}')

    def dogmakesound(self):
        super().makesound("hav hav")


    def move(self):
        print('move dog')