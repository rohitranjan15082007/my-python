n = int(input("enter a number: "))
i = 0
max_num = float('-inf')
min_num = float('inf')
while i < n:
    i += 1
    x = int(input("enter a number: " + str(i) + ": "))
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
print("The maximum number is:", max_num)
print("The minimum number is:", min_num)
    