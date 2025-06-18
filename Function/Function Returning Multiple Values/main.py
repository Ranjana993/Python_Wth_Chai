# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def area(r):
  area_of_circle = round(math.pi*r*r,2)
  circumference_of_circle= round(2*math.pi*r,2)
  return area_of_circle , circumference_of_circle


res = area(2)
print(res)
