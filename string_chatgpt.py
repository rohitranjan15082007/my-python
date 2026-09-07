# strings = []

# print("Enter strings one by one.")
# print("Press Enter without typing anything to finish.")

# while True:
#     s = input("Enter string: ")

#     if s == "":
#         break

#     strings.append(s)

# sub_string = input("Enter substring to search: ")

# found = False

# for s in strings:
#     if sub_string in s:
#         print(f"'{sub_string}' found in: {s}")
#         found = True

# if not found:
#     print(f"'{sub_string}' was not found in any string.")


import json
import os

FILE_NAME = "strings.json"

# JSON database को load करना
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        strings = json.load(file)
else:
    strings = []

# नई strings enter करना
print("Enter strings one by one.")
print("Press Enter without typing anything to finish.")

while True:
    s = input("Enter string: ")

    if s == "":
        break

    strings.append(s)

# JSON database में save करना
with open(FILE_NAME, "w", encoding="utf-8") as file:
    json.dump(strings, file, ensure_ascii=False, indent=4)

print("\nStrings saved successfully!")

# Substring search
sub_string = input("\nEnter substring to search: ")

found = False

for s in strings:
    if sub_string in s:
        print(f"'{sub_string}' found in: {s}")
        found = True

if not found:
    print(f"'{sub_string}' was not found in any string.")