import math
a = 2
b = 2
c = 5
disc =  b ** 2 - 4 * a * c
print("The discriminant is:", disc)

if disc >= 0:
    # real roots
    print("Real roots")
    x1 = (- b + math.sqrt (disc)) / (2 * a)
    x2 = (- b - math.sqrt (disc)) / (2 * a)
    print("The roots of the quadratic equation are:", x1, "and", x2)
 
else:
    # complex roots
    print("Complex roots")
    realPart = - b / (2 * a)
    imaginaryPart = math.sqrt(-disc) / (2 * a)
    print("The roots of the quadratic equation are:", realPart, "+", imaginaryPart, "i and", realPart, "-", imaginaryPart, "i")
    