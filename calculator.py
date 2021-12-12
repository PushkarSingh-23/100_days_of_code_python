print("welcome to my calculator")
num1 = int(input("enter num 1 "))
num2 = int(input("enter num 2 "))
operator = (input("Enter operator '+' '-' '*' '/' "))
if operator == '+':
   print(f"{round((num1 + num2) , 3)}  is your result")
elif operator == '-':
    print(f"{round((num1 - num2) , 3)}  is your result")
elif operator == '*':
    print(f"{round((num1 * num2) , 3)}  is your result")
elif operator == '/':
    print(f"{round((num1/num2) , 3)}  is your result")
else:
    print("Invalid operator")
