n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# n = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# while n > 0:
#     print(a, end=" ")
#     a, b = b, a + b
#     n -= 1