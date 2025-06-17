# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

input_password = input("Enter your password: ")
if len(input_password)<6:
    print("Weak Password.")
elif 6 <= len(input_password) <=10 :
  print("Medium Password.")
elif len(input_password) > 10:
  print("Strong Password.")
else:
  print("Invalid password")          