# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

def greet(name="User"):
  return f"Welcome {name}!,Hope you're doing great."

res = greet()
print(res)