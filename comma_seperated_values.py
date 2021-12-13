#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
values = input("please enter multiple values seperated by commas")
values = values.split(",")
print(values)
list = values
print(list)
tuple = tuple(list)
print(tuple)