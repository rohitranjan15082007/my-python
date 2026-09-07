# /print the first name, domain name and extension of the email id
s1 = str(input("enter the email id:"))

x =("first name of email id: " + s1.split("@")[0])
print(x)
y =("domain name: " + s1.split("@")[1].split(".")[0])
print(y)
z =("extension: " + s1.split("@")[1].split(".")[1])
print(z)
