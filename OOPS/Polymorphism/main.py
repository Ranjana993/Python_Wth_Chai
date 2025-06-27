# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.



class Car:
  def __init__(self , brand , model):
    self.__brand = brand
    self.model = model
  def get_brand(self):
    return self.__brand +" !"
  def full_name(self):
    return "Hello"
  def fuel_type(self):
    return "Petrol or Diesel."


class ElectricCar(Car):
  def __init__(self ,brand , model, batter_size):
    super().__init__(brand , model)
    self.batter_size = batter_size
  def fuel_type(self):
    return "Electric charge."



electricCar  = ElectricCar("tesla" , " model S" , "85KWH")
print(electricCar.fuel_type())

safari = Car("Safari" , "Tata")
print(safari.fuel_type())