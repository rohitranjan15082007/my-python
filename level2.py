# 🟡 Level 2 — String Logic
# 11. Take a string and count the number of vowels.
# s1 = str(input("enter the string :"))
# vowel =s1.find( "a","e","i","o","u")
# print(vowel)
# i not know how to solve it

str = input("enter the string :")
vowels = 0
while str:
    char = str[0].lower()
    if char in "aeiou":
        vowels += 1
    str= str[1:]
print(vowels)
    
# Input: programming
# Output: 3
# 12. Count vowels and consonants separately.
string = input("enter the string :").lower()
vowels = 0
consonants = 0

for char in string:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print(f"Vowels: {vowels}, Consonants: {consonants}")
# 13. Reverse a string without using [::-1].
str = input("enter the string :")
reversed_str = ""
for char in str:
    reversed_str = char + reversed_str
print(reversed_str)
# 14. Check whether a string is a palindrome.
str = input("enter the string :")
if str == str[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# madam → Palindrome
# hello → Not Palindrome
# 15. Count the number of words in a sentence.
str = input("enter the string :")
words = str.split()
print(f"Number of words: {len(words)}")
# Input: I am learning Python
# Output: 4
# 16. Find the longest word in a sentence.
str = input("enter the string :")
words = str.split()
longest_word = max(words, key=len)
print(f"Longest word: {longest_word}")
# 17. Find the shortest word in a sentence.
shortest_word = min(words, key=len)
print(f"Shortest word: {shortest_word}")
# 18. Count how many times each character occurs.
str = input("enter the string :")
char_count = {}
for char in str:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# Input: banana

# b = 1
# a = 3
# n = 2
# 19. Remove all spaces from a string.
str = input("enter the string :")
spaceless_str = str.replace(" ", "")
print(spaceless_str)
# Input: hello world python
# Output: helloworldpython
# 20. Replace every space with -.
str = input("enter the string :")
hyphenated_str = str.replace(" ", "-")
print(hyphenated_str)
# Input: I love Python
# Output: I-love-Python