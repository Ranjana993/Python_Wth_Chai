# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

input_number = int(input("Enter a number to print its multiplication table: "))

for i in range(1 , 11):
  if i == 5:
    continue
  res = input_number*i
  print(f"{input_number} X {i} = {res}")
