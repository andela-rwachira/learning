'''
An example of polymorphism - subclasses inherit then override
the attributes and methods of a parent class.
'''


class Car(object):
    '''
    Car is an abstract class that
    defines the methods but does not implement them
    '''

    def __init__(self, name):
        self.name = name

    def Start(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def Stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class oldCar(Car):
    def Start(self):
        return ("I'm too old to start")

    def Stop(self):
        return ("If you stop me, I might never start again")


class newCar(Car):
    def Start(self):
        return ("Let's go!")

    def Stop(self):
        return ("If you insist")


cars = [
    oldCar("Nissan'97"),
    newCar("Tesla'16"),
    oldCar("Toyota'89")
]

for car in cars:
    print (car.name + ' : ' + car.Start())
    print (car.name + ' : ' + car.Stop())


'''
An example of overloading - a method that can take multiple inputs
and perform the same operation on each of them.
'''


class Greetings:

    def sayHello(self, name=None, num=None):
        if name is not None and num is not None:
            print ('Hello ' + name + '. Visitor number:', int(num))
        elif name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello')


obj = Greetings()

obj.sayHello()
obj.sayHello('Rehema')
obj.sayHello('Rehema', 16)
