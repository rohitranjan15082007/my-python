tum_sapne_me_ho = False 
print("Tum ek sapne mein ho. Tumhare paas ek chabi hai aur thumra ek dost bhi hai saath mein.")
choice = input("thumare pass ek jadu ke chabi hai but use ek baar he istamal kae sakte ho to tum apne dost se pucho ge ke kab istamal karna hai? (yes/no): ") .lower()
if choice == "yes":
    tum_sapne_me_ho = True
    print("istamal karne ke liye tumhare dost ne kaha ke use abhi istamal karo. Tumne jadu ke chabi ka istamal kiya aur tumhare sapne mein ek sundar jagah khul gayi! 🎉")
    if tum_sapne_me_ho == True:
        print("Tumhare sapne mein tumhare dost ne kaha ke tumhare paas ek aur jadu ke chabi hai. Tumhe kya karna chahiye? (use/ignore): ")
        choice2 = input().lower()
        if choice2 == "use":
            print("Tumne jadu ke chabi ka istamal kiya aur tumhare sapne mein ek aur sundar jagah khul gayi! 🎉")
        elif choice2 == "ignore":
            print("Tumne jadu ke chabi ka istamal nahi kiya. Tumhare sapne mein kuch bhi nahi hua. Game Over!")
        else:
            print("Invalid choice. Game Over!")