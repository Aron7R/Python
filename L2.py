# OOP1

class Car:

def __init__(self,Name,Engine,Model,Price):

self.Engine = Engine
self.Name = Name
self.Model = Model
self.Price = Price


def Stop(self):
print(self.Name," Car is being stopped")

def Run(self):
print(self.Name," Car is Running")


bmw = Car("BMW","V8",13,87806)
ferrari = Car("Ferrari","M9",10,97908)

print(bmw.Price)
print(ferrari.Price)

bmw.Run()
bmw.Stop()

lambo = Car("Lamborghini","A1","7H",9000)
lambo.Run()
lambo.Stop() 