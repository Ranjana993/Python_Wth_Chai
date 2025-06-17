# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

input_distance = float(input("Enter the distance in kilometers: "))
if input_distance < 3:
  print("You should walk.")
elif 3<= input_distance <=15:
  print("You should bike.")
elif input_distance > 15:
  print("You should take a car.")
else:
  print("Invalid distance entered.")      

