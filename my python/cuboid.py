# Calculate the volume of a cuboid
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
volume = length * width * height
area = 2 * (length * width + length * height + width * height)
lateral_surface_area = 2 * height * (length + width)
daigonal = (length**2 + width**2 + height**2)**0.5
print("The volume of the cuboid is:", volume)
print("The surface area of the cuboid is:", area)
print("The lateral surface area of the cuboid is:", lateral_surface_area)       
print("The diagonal of the cuboid is:", daigonal)