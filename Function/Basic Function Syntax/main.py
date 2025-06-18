# Problem: Write a function to calculate and return the square of a number.

def squareNum(a):
  return a**a

input_number = int(input("Enter your number for square."))
res = squareNum(input_number)
print("Your ans is ",res) 