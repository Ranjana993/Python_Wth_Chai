# Problem: Given a string, find the first non-repeated character.

input_string = input("Enter a string to find the first non-repeated character: ")

for char in input_string:
  if input_string.count(char) == 1:
    print("Char is :" ,char)
    break
