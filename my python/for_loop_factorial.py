# n = 7
# sum = 0 
# for i in range(1, n + 1):
#     sum += i
# print("The sum of numbers from 1 to", i, "is:", sum)


n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("The factorial of", n, "is:", factorial)