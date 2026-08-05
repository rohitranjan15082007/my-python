marks = float(input("Enter your obtained marks: "))

choice = input("Did you receive extra marks? (yes/no): ").lower()

extra_marks = 0  # default value

if choice == "yes":
    extra_marks = float(input("Enter your extra marks: "))
    print(f"You have received extra marks: {extra_marks}")
    if extra_marks > 20:
        print("Extra marks cannot be more than 20. Setting extra marks to 20.")
        extra_marks = 0
    else:
        print("Extra marks cannot be more than 20. Setting extra marks to 20.")
        extra_marks = 20
else:
    print("You have not received extra marks.")

total_marks = marks + extra_marks

print(f"Total marks: {total_marks}")

if total_marks >= 90:
    print("You have got A grade.")
elif total_marks >= 80:
    print("You have got B grade.")
elif total_marks >= 70:
    print("You have got C grade.")
elif total_marks >= 60:
    print("You have got D grade.")
else:
    print("You have got F grade.")


