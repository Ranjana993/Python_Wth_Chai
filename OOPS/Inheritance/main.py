# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.


class Car:
  def __init__(self , brand , model):
    self.branch = brand
    self.model = model
  def full_name(self):
    return "Hello"

# car_ref = Car("tata" , "Jaguar")
# print(car_ref.full_name()) 

class ElectricCar(Car):
  def __init__(self ,brand , model, batter_size):
    super().__init__(brand , model)
    self.batter_size = batter_size


electricCar  = ElectricCar("tesla" , " model S" , "85KWH")

print(electricCar.full_name())