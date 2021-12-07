print("welcome to the love calculator")
name1 = input("please enter your name: ")
name2 = input("please enter your loved one's name ")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
combined_name = lower_name1 + lower_name2
T = lower_combined_name = combined_name.count("t")
R = lower_combined_name = combined_name.count("r")
U = lower_combined_name = combined_name.count("u")
E = lower_combined_name = combined_name.count("e")
L = lower_combined_name = combined_name.count("l")
O = lower_combined_name = combined_name.count("o")
V = lower_combined_name = combined_name.count("v")
E = lower_combined_name = combined_name.count("e")
true = T + R + U + E
love = L + O + V + E
love_score = str(true) + str(love)
print(love_score)
if_love_case = int(love_score)
if if_love_case >75:
    print("you have great futures")
    if if_love_case >=50:
        print("there's a hope for you !")
    else:
        print("have a hope for you buddy")
else:
    print("good luck")