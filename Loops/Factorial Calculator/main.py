# Problem: Compute the factorial of a number using a while loop.


n = int(input("Enter a positive integer: "))
factorial = 1
while n >1:
  factorial *=n
  n-=1

print("The factorial is:", factorial)