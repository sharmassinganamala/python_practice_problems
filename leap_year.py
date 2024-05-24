# checking an yar is leap or not
# If a year is divisible by 4, it is a leap year.
# However, if that year is divisible by 100, it is not a leap year, unless…
# It is also divisible by 400, in which case, it is a leap year.
year = int(input("Enter an year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
