years = int(input("Enter a year: "))
if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
    print(years, "is a leap year.")
else:
    print(years, "is not a leap year.")