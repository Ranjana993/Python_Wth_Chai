# Problem: Reverse a string using a loop.



input_string = input("Enter a string to reverse: ")
reversed_string = "" 
for char in input_string:
  reversed_string = char + reversed_string 
print(f"The reversed string is: {reversed_string}")  # 


