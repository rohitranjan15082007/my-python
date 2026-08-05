has_upper = False
has_length = False
has_special = False
has_number = False
password = input("enter your password :")
if len(password) > 8:
    has_length = True
if any (num.isdigit() for num in password):
    has_number = True
if any(char.isupper() for char in password):
    has_upper = True
if any(not char.isalnum() for char in password):
    has_special = True   
if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password) and len(password) > 8:
    print("Password is valid")
if has_length and has_upper and has_special and has_number:
    print("password is valid")
else:
    print("password is not valid")