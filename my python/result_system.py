# student = input("enter you name :")
# chem = float(input("enter your chemestry marks :;"))
# phy = float(input("enter your physic marks:"))
# math = float(input("enter your math marks :"))
# extra_marks = ("did you recive extra marks ( yes/no ) :")
# extra_marks = 0 
# if extra_marks == "yes" :
#    float(input ( "enter your extra marks "))
   
#    print(f"You have received extra marks: {extra_marks}")
#    while extra_marks == True :
#      if extra_marks > 20:
#         print("Extra marks cannot be more than 20. Setting extra marks to 20.")
#         extra_marks = 0
#      else:
#         print("Extra marks cannot be more than 20. Setting extra marks to 20.")
#         extra_marks = 20
# elif extra_marks == "no"  :
#    print("you no recive extra marks")

#    total_marks = chem + phy + math + extra_marks
#    percentage = total_marks /300 * 100
#    print ( f"total marks obtain :{total_marks}")
#    print( f"total percentage of three sub :{percentage}")

#    if percentage >= 90 :
#       print("you have got A grade")
#    elif percentage >= 80 :  
#       print("you have got B grade")
#    elif percentage >= 70 :
#         print("you have got C grade")
#    elif percentage >= 60 :
#         print("you have got D grade")
#    else :
#         print("you have got F grade")

# written by chat gpt

student = input("Enter your name: ")

chem = float(input("Enter your chemistry marks: "))
phy = float(input("Enter your physics marks: "))
math = float(input("Enter your math marks: "))

choice = input("Did you receive extra marks? (yes/no): ").lower()

extra_marks = 0

if choice == "yes":
    while True:
        extra_marks = float(input("Enter your extra marks (max 20): "))
        if extra_marks <= 20:
            break
        else:
            print("❌ Extra marks cannot be more than 20. Try again.")

    print(f"You have received extra marks: {extra_marks}")

else:
    print("You did not receive extra marks.")

# ✅ Calculation (always outside condition)
total_marks = chem + phy + math + extra_marks
percentage = (total_marks / 300) * 100

print(f"Total marks obtained: {total_marks}")
print(f"Percentage: {percentage:.2f}%")

# ✅ Fail condition
if chem < 33 or phy < 33 or math < 33:
    print("Status: Fail ❌")
else:
    print("Status: Pass ✅")

# ✅ Grade
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
else:
    print("Grade: F")