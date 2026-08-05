# n = 8789

# while n > 0:
#     last_num = n % 10
#     print("The last digit is:", last_num)
#     n = n // 10

# n = 7867635
# i = 0 
# while n > 0 :
#     i = i + 1
#     n = n // 10
# print (i)
   
# n = int(input("Enter a number: "))
# sum = 0
# while n > 0:
#     last_num = n % 10
#     n = n // 10
#     # print("The last digit is:", last_num)
#     sum = sum + last_num
# print("The sum of the digits is:", sum)


# num = int(input("Enter a number: "))
# i = 0
# while num > 0:
#     last_digit = num % 10
#     i = i * 10 + last_digit
#     num = num // 10
# print("The number of digits is:", i)


# num = int(input("Enter a number: "))
# i = 0
# m = num
# while num > 0:
#     last_digit = num % 10
#     i = i * 10 + last_digit
#     num = num // 10
# # print("The reverse of the number is:", i)
# if m == i:
#         print("The number is a palindrome")
# elif m != i:
#         print("The number is not a palindrome" , i )




# n = 15
# i = 1
# sum = 0

# while i <= n:
#     sum = sum + i
#     i = i + 1

# print("The sum of the first", n, "natural numbers is:", sum)



# n = 8
# i = 1
# sum = 0
# print("The first", n, "natural numbers are:")
# while i <= n:
#     x =int(input("enter a number: " + str(i-1) + ": "))
#     i = i + 1
#     sum = sum + x

# print("The sum of the first", n, "natural numbers is:", sum)



n = int(input("enter a number: "))
print("The first", n, "natural numbers are:")
i = 1
max_num = float('-inf')
min_num = float('inf')
while i <= n:
    x = int(input("enter a number: " + str(i) + ": "))
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
    i += 1

print("The maximum number is:", max_num)
print("The minimum number is:", min_num)