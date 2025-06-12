# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = input("Enter the student's score :").strip()
if score.isdigit():
  score =int(score)
  if score >=90 and score <=100:
    print("Student geade is A")
  elif score >= 80 and score < 90:
    print("The student grade is B.")
  elif score >=70 and score<80:
    print("The stdudent grade is C.")
  elif score >=60 and score <70:
    print("The student grade is D.")
  else:
    print("The student grade is F.")        
