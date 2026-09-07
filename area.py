# Calculate the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = int(0.5 * base * height)
print("The area of the triangle is:", area)

# Calculate the area of a trapazium
base1 = float(input("Enter the first base of the trapezium: ")) 
base2 = float(input("Enter the second base of the trapezium: "))
height = float(input("Enter the height of the trapezium: "))
area = int(0.5 * (base1 + base2) * height)
print("The area of the trapezium is:", area)

# Calculate the area of a circle
radius = float(input("Enter the radius of the circle: "))
area = int(3.14 * radius * radius)
print("The area of the circle is:", area)
# calculate the arer of rectangle
length = float(input("enter the length of rectangle"))
breadth = float(input("enter the breadth of rectangle"))
print("area of rectangle :" , length* breadth)