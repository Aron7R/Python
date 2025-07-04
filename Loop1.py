class Car:

def __init__(self,Name,Engine,Model,Price):
 self.Engine = Engine
 self.Name = Name
 self.Model = Model
 self.Price = Price

AUDI = Car("AUDI","C17",7,500000)
Lamborghini = Car("LAMBO","M10",90,10000)

print(AUDI.Engine)
