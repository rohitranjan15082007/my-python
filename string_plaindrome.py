str = input("Enter a string: ")
x = str.replace(" " ,"")
print(x)
if x == x[::-1]:
    print(str,"The string is a palindrome.")
else:
    print("not plaindrome and its plaindrome " , (x+x[::-1]))