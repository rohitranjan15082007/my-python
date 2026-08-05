password = input("Enter your password: ")

if (len(password) > 8 and
    (any(char.isupper() for char in password) or
    any(char.islower() for char in password) )and
    any(char.isdigit() for char in password) and
    any(not char.isalnum() for char in password)):
    
    print("Password is valid")
else:
    print("Password is not valid")