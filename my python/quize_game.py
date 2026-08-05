# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}! Welcome to the quiz game.")


# print("You chose Math quiz!")
#             # Add Math quiz questions here
# "area of circle = '74'"
# 'what is the radius?'
# radius = input("Enter the radius: ")
#             if radius == "4.85":
#                 print("Correct!")
#             else:
#                 print("Incorrect. The correct answer is 4.85.")
#                 # Provide additional explanation or feedback here
#                 print("The area of a circle is πr². If the area is 74, then r² = 74/π ≈ 23.56, so r ≈ 4.85. However, for this quiz, we'll assume r = 4.85.")
#             print("You chose Science quiz!")
#             # Add Science quiz questions here 
#             "how many planets are in our solar system?"
#             answer = input("Enter your answer: ")  
#             if answer == "8":
#                 print("Correct!")
#             else:
#                 print("Incorrect. The correct answer is 8.")
#                 # Provide additional explanation or feedback here
#                 print("There are 8 planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.")

#             print("You chose History quiz!")
#             # Add History quiz questions here
#             "who was the first president of the United States?"
#             answer = input("Enter your answer: ")
#             if answer == "George Washington":
#                 print("Correct!")
#             else:
#                 print("Incorrect. The correct answer is George Washington.")
#                 # Provide additional explanation or feedback here
#                 print("George Washington was the first president of the United States, serving from 1789 to 1797.")
            

#     # marks system and grade system
# marks = 0
# if  radius == "4.85":
#         marks += 1
# if  answer == "8":
#         marks += 1
# if answer == "George Washington":
#         marks += 1

# print(f"Your score is {marks} out of 3.")
# if marks == 3:
#         print("Excellent! You got all the answers right.")
# elif marks == 2:
#         print("Good job! You got most of the answers right.")
# else:
#         print("Keep practicing! You'll get better.")


# chat gpt


user_name = input("Enter your name: ")
print(f"\nHello, {user_name}! Welcome to the quiz game.\n")

score = 0

# 🔢 Question 1 (Math)
print("Q1: If area of circle is 74, what is radius (approx)?")
radius = input("Enter your answer: ")

if radius == "4.85":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. Correct answer is 4.85")

# 🔬 Question 2 (Science)
print("\nQ2: How many planets are in our solar system?")
ans2 = input("Enter your answer: ")

if ans2 == "8":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. Correct answer is 8")

# 📜 Question 3 (History)
print("\nQ3: Who was the first president of the United States?")
ans3 = input("Enter your answer: ").lower()

if ans3 == "george washington":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Incorrect. Correct answer is George Washington")

# 🎯 Final Score
print(f"\nYour score is {score}/3")

if score == 3:
    print("🏆 Excellent!")
elif score == 2:
    print("👍 Good job!")
elif score == 1:
    print("🙂 Average")
else:
    print("😅 Keep practicing!")