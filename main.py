from animal import Animal
from dog import Dog
from bird import Bird

from factory import Factory
from singleton import Singleton

if __name__ == '__main__':

    r = Factory(15)
    r.get_object().drink()
    #or this syntax
    x = r.get_object()
    x.drink()

from person import  Person
    p = Person()
    '''obj1 = Singleton()
    print(obj1)

    obj2 = Singleton()
    print(obj2)'''




    # a.sleep(3)
    #
    # d = Dog(10)
    # d.run()
    # d.dogmakesound()
    # b = Bird(10)
    # b.fly()
    # b.move()
    # d.move()




