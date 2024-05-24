# pizza bill calculation
print("welcome to pizza store! ")
print("Which size pizza do you want  : ")
pizza_size = input()
bill = 0
if pizza_size == "s":
    bill = 10
    print(f"The amount of smalli pizza is {bill}")
elif pizza_size == "m":
    bill = 15
    print(f"The amount of medium pizza is {bill}")
elif pizza_size == "l":
    bill = 20
    print(f"the pizza amount for large is {bill}")
else:
    print("Enter a valid input ")
print("you want extra pepper : ")
extra_pepper = input()
if extra_pepper == "y":
    bill = bill + 5
    print(f"The total bill is {bill} ")
else:
    print(f"The total bill is {bill}")
print("And you want extra chease : ")
extra_chease = input()
if extra_chease == "y":
    bill = bill + 5
    print(f"The total bill is {bill}")
else:
    print(f"The total bill is {bill}")
