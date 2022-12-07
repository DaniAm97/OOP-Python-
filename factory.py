class Cola(object):
    def drink(self):
        print("Drink Cola")



class Sprite(object):
    def drink(self):
        print('Drink sprite')


class Factory(object):
    def __init__(self,x):
        self.x = x


    def get_object(self):
        if self.x > 10:
            return Cola()
        else:
            return Sprite()
