# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

day = input("Please enter the day of the week: ").strip().lower()
age = input("Please enter your age: ").strip()
if age.isdigit():
  age = int(age)
  if age < 18:
    ticket_price = 8
  else:
    ticket_price = 12
  if day == "wednesday":
    ticket_price -= 2
    print(f"The ticket price is: ${ticket_price}")
  else:
    print("Invalid input. Please enter a valid age as a number.")


