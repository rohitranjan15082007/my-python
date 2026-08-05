# 1. Variables banaye (Ye memory mein store karta hai ki kya hai hamare paas)
has_key = False

print("Tum ek purane mahal ke gate par khade ho.")
choice = input("Kya tum gate kholna chahte ho? (yes/no): ")

# 2. Logic (If-else)
if choice == "yes":
    print("Darwaza band hai! Shayad tumhe chabi (key) ki zaroorat hai.")
    
    # Nested Input
    find_key = input("Kya tumhe zameen par chabi mili? (yes/no): ")
    if find_key == "yes":
        has_key = True
        print("Bahut achhe! Ab tumhare paas chabi hai.")
    else:
        print("Tumhe chabi nahi mili. Game Over!")
else:
    print("Tum wapas chale gaye. Bye!")

# 3. Final Check (Logical condition)
if has_key == True:
    print("Tumne chabi se darwaza khola aur jeet gaye! 🎉")