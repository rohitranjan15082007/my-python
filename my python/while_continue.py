n = int(input("Enter a number: "))
i = 0
while i < 500:
    i += 1
    if i % n == 0:
        continue
    print(i)