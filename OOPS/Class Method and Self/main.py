# Problem: Add a method to the Car class that displays the full name of the car (brand and model).


class Car:
  def __init__(self , brand , model):
    self.branch = brand
    self.model = model
  def full_name(self):
    return "Hello"

car_ref = Car("tata" , "Jaguar")
print(car_ref.full_name())  