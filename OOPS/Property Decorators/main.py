# Problem: Use a property decorator in the Car class to make the model attribute read-only.

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

# CAR
car = Car("Tata" , "Tata")

print(car.general_des())