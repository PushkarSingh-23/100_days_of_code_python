print("highest score program:")
student_score = [78 , 56 ,54 , 98 , 78 , 77 , 79 , 77 ,]
print(student_score)
print(sum(student_score))
print(len(student_score))
print(max(student_score))
print(min(student_score))
highest_score = 0
for student in student_score:
    if student > highest_score:
     highest_score = student
print(f"highest_score = " ,{highest_score})