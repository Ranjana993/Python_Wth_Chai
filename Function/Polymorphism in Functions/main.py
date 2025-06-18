# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(a, b):
    # Try to convert to numbers if possible
    try:
        a_num = float(a)
        b_num = float(b)
        return a_num * b_num
    except ValueError:
        # If not numbers, try string multiplication
        if isinstance(a, str) and b.isdigit():
            return a * int(b)
        elif isinstance(b, str) and a.isdigit():
            return b * int(a)
        else:
            return "Cannot multiply these inputs."

a = input("Enter your first number or string: ")
b = input("Enter your second number or string: ")
res = multiply(a, b)
print(res)