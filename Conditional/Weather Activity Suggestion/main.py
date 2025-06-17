# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).



input_weather = input("Enter the current weather (Sunny, Rainy, Snowy): ").strip().lower()
if input_weather =="sunny":
  print("Go for a walk!")
elif input_weather =="rainy":
  print("Read a book!")
elif input_weather=="snowy":
  print("Build a snowman!")
else:
  print("Weather not recognized.Please enter Sunny ,Rainy or Snowy.")      