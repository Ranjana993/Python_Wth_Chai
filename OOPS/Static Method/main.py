# Problem: Add a static method to the Car class that returns a general description of a car.


class Car:
  total_car = 0
  def __init__(self , brand , model):
    self.__brand = brand
    self.model = model
    Car.total_car += 1
  def get_brand(self):
    return self.__brand +" !"
  def full_name(self):
    return "Hello"
  def fuel_type(self):
    return "Petrol or Diesel."
  @staticmethod
  def general_des():
    return "Cars are means of transport . "


class ElectricCar(Car):
  def __init__(self ,brand , model, batter_size):
    super().__init__(brand , model)
    self.batter_size = batter_size
  def fuel_type(self):
    return "Electric charge."


# CAR
car1 = Car("Tata" , "Tata")
car2 = Car("Toyota" , "Toyota")
car3 = Car("NewCar" , "NewCar")
car4 = Car("test" , "test")

print(car4.general_des())