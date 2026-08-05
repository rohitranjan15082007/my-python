# number = int(input("enter the number :"))
# i = 0
# while i < 0:
#     i = i + 1
#     r = number % 10
#     number = (number * 10) + r
# print("Reverse of the given number is :", number)


# chat gpt model 
number = int(input("enter the number : "))
rev = 0
m = number
while number > 0:
    r = number % 10
    rev = (rev * 10) + r
    number = number // 10
if rev == m:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    


