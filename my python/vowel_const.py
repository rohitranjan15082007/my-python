vowel = str(input("Enter a letter: "))
if not vowel.isalpha():
    print("Invalid input! Please enter a letter only.")         
elif vowel== "a" or vowel== "e" or vowel== "i" or vowel== "o" or vowel== "u":
    print("The letter is a vowel.")
elif vowel== "y"  :
    print("The letter is sometimes a vowel and sometimes a consonant.")
else:
    print("The letter is a consonant.")


# vowel = input("Enter a letter: ")

# if not vowel.isalpha():
#     print("Invalid input! Please enter a letter only.")

# elif vowel.lower() in "aeiou":
#     print("The letter is a vowel.")

# elif vowel.lower() == "y":
#     print("The letter is sometimes a vowel and sometimes a consonant.")

# else:
#     print("The letter is a consonant.")