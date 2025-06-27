# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
  def __init__(self , brand , model):
    self.__brand = brand
    self.model = model
  def get_brand(self):
    return self.__brand +" !"
  def full_name(self):
    return "Hello"


class ElectricCar(Car):
  def __init__(self ,brand , model, batter_size):
    super().__init__(brand , model)
    self.batter_size = batter_size


electricCar  = ElectricCar("tesla" , " model S" , "85KWH")

print(electricCar.full_name())
print(electricCar.get_brand())



