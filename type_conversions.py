print("type conversions problems \n")

#it could not run because the num is an integer it could not combine with string
# num = 6
# print("The name having " + num + " characters ")


# now it will works....we need to convert from int to string to combine with it
num = 6
new_num = str(num)
print("the name having " + new_num + " charactrs\n")


# now it show the type of the num value
num = 6
print(type(num))
print("\n")

# float
num1 = 3.45
print(type(num1))
print("\n")


# combine to int values by converting into strings
num2 = 6
num3 = 7
new_num2 = str(num2)
new_num3 = str(num3)
print(new_num2 + new_num3)  #now it prints 67