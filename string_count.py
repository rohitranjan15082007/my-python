string = str(input("enter the string :"))
sub = str(input("enter the substring :"))
n = string.find(sub,0 ,len(string) ) 
if sub == -1:
    print("substring found at index", n)
else:
    print("substring not found")