# Problem: Calculate the sum of even numbers up to a given number n.



n = int(input("Enter a number: "))
sum_of_evens = 0
for i in range(2, n + 1, 2):
    sum_of_evens += i

print(f"The sum of even numbers up to {n} is {sum_of_evens}.")