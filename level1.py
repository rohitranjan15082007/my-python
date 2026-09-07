# 🟢 Level 1 — Basic String Practice
# Try these without looking up the solution.
# 1. Take a string from the user and print it.
user_string = str (input("enter the string : ")) 
print(user_string)
# 2. Take a string and print its length using len().
x = len(user_string)
print(x)
# 3. Convert a string to uppercase.
y = user_string.upper()
# 4. Convert a string to lowercase.
z = user_string.lower()
print(z)
# 5. Convert "hello world" into "Hello World".
s1 = "hellow world"
c = s1.title()
print(c)
# 6. Count how many times "a" appears in a string.
d = s1.count("a")
print(d)
# 7. Check whether the word "python" exists in a string.
s2 = "python is easy "
f = s2.find("python")
print(f)

# 8. Print the first character of a string.
g = user_string[0]
print(g)
# 9. Print the last character of a string.
l = user_string[-1]
print(l)
# 10. Print characters from index 2 to 6.
r = user_string[2:7]
print(r)
# Example:
# Input: programming
# Output: ogr