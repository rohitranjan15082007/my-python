temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F): ") .strip().upper()

if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
elif unit == "F":
    celsius = (temperature - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius:.2f}")
else:
    print("Invalid unit. Please enter either 'C' or 'F'.")