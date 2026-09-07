# phrase1 = input("enter the string 1 :")
# phrase2 = input("enter the string 2 :")
# lower1= phrase1.lower()
# lower2 = phrase2.lower()
# count1 = lower1.count()
# count2 = lower2.count()
# if count1 == count2  :
#     print("anagram")
# else:
#     print("not anagram")



s1 = input("enter the phrase 1 ")
s2 = input("enter the phrase 2 ")
s1 = s1.lower()
s2 = s2.lower()
for x in s1 :
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print("not alangram")
            break
else:
  print("alangram")        