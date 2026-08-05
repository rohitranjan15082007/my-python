n = int(input("enter a number: "))
sum = 0
i = 1
print("enter a number:", n , "number")
while i <= n:
    i += 1
    x =int(input("enter a number: " + str(i-1) + ": "))
    sum += x

print("The sum of numbers from 1 to", n, "is:", sum)