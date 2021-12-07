print("welcome to tip calculator!")
bill = float(input ("please enter your total amount :"))
tip = float(input("Please enter the tip you wish to give to :"))
split = float(input("how you want to split your transaction"))
your_amount = tip/100*bill+bill
per_person = round(your_amount/split, 2)
your_amount = print(f"your final amount is {your_amount} , and per person its {per_person} ")