# Write a Python program to display the examination schedule. (extract the date from exam_st_date)
examination_schedule = input("Enter yor examination_schedule in 1/02/2022 format : ").strip("/")
print(len(examination_schedule))
print(examination_schedule[0:len(examination_schedule)])
#here i have used the len funtion to calculate the length of list to print last element of the list 