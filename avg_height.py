print("average height of  students :")
student_heights = input("Input a list of students height :").split(" ")
for n in range(0 , len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height =total_height / number_of_students
print(average_height)
#here i could i have used the sum and len funtion insted 
#of for loop but to understand i have used for loop i have used
#here sum funtion gives the summ of all elements present in array of list
#and the len funtion gives the length of the list of elements