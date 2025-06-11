# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

user_question = input("Please enter your age group: ")
if user_question.isdigit():
 age= int(user_question)
 if age <13:
  print("You are classified as a Child.")
 elif 13 <= age <=19:
  print("You are classified as a Teenager.")
 elif 20 <= age <=59:
  print("You are classified as an Adult.")
 elif age >= 60:
  print("You are classified as a Senior.")
else:
 print("Invalid input. Please enter a valid age as a number.")   

