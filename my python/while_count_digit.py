number = int(input("enter the number :"))
count_digit = 0
while number > 0:
    number = number // 10
    count_digit += 1
print("number of digits in the given number is :", count_digit)
