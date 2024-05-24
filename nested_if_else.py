# we are going to check the age and height to get into roller coster 
# age <12 need to pay 5rs
# age b/w 12 to 18 need to pay 7rs
# age above 18 need to pay 10rs
print("......welcome to the roller coster.....")
height = int(input("Enter your height : "))
if height >=120:
    print("you can get into the roller coster!")
    age = int(input("Enter your age : "))
    if(age <= 12):
        print("you need to pay 5rs")
    elif age <= 18:
        print("you need to pay 7rs ")
    else:
        print("you need to pay 10rs")
else:
    print("sorry! your height is less than 120 you cannot")
