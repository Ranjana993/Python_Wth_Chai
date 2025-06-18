# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
  user_input = int(input("Enter your input in range of (1-10): "))
  if  1 <= user_input <=10:
    print(f"Valid input: {user_input}" )
    break
  else:
    print("Input out of range. Please enter a number between 1 and 10.")
