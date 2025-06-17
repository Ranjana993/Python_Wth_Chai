# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

def recommend_pet_food(species, age):
  if species.lower() == "dog":
    if age < 2:
      return "Puppy food"
    elif age <= 5:
      return "Adult dog food"
    else:
      return "Senior dog food"
  elif species.lower() == "cat":
    if age < 1:
      return "Kitten food"
    elif age <= 5:
      return "Adult cat food"
    else:
      return "Senior cat food"
  else:
    return "Unknown species, no recommendation available."
    
# Example usage
species = input("Enter the pet's species (dog/cat): ")
age = int(input("Enter the pet's age in years: "))
food_recommendation = recommend_pet_food(species, age)
print(f"Recommended food for your {species} ({age} years old): {food_recommendation}")