# calculate displacement
initial_velocity = float(input("Enter the initial velocity: "))
final_velocity = float(input("Enter the final velocity: "))
acceleration = float(input("Enter the acceleration: "))
displacement = (final_velocity**2 - initial_velocity**2 )/( 2 * acceleration )

print("The displacement is:", displacement) 