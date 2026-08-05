def game():
    print("🏝️ Welcome to the Adventure Game!")
    print("Your mission is to find the hidden treasure.\n")

    # Player state
    has_key = False
    has_sword = False
    has_shield = False
    health = 100

    # Start
    choice1 = input("You are at a crossroad. Go left or right? ").lower()

    if choice1 == "left":
        print("\n🌲 You enter a dark forest.")

        choice2 = input("You see a shiny object. Pick it up? (yes/no): ").lower()

        if choice2 == "yes":
            print("🗝️ You found a key!")
            has_key = True
        elif choice2 == "no":
            print("You ignored the object.")
        else:
            print("Invalid choice. Game Over ❌")
            return

        print("\nYou move ahead and find a cave.")

        choice3 = input("Do you want to enter the cave? (yes/no): ").lower()

        if choice3 == "yes":
            print("\n🐉 A Dragon appears!")

            # Check condition using OR
            if has_sword or has_shield:
                print("You are ready to fight!")

                fight = input("Fight or run? ").lower()

                if fight == "fight":
                    print("⚔️ You defeated the dragon!")
                    print("🏆 You found the treasure! YOU WIN 🎉")
                elif fight == "run":
                    print("You ran away safely.")
                else:
                    print("Invalid choice. Game Over ❌")
            else:
                print("❌ You have no weapons. The dragon defeated you!")
        elif choice3 == "no":
            print("You walk away and get lost. Game Over ❌")
        else:
            print("Invalid choice. Game Over ❌")

    elif choice1 == "right":
        print("\n🏰 You arrive at an abandoned castle.")

        choice2 = input("Do you want to enter the castle? (yes/no): ").lower()

        if choice2 == "yes":
            print("\nInside the castle, you find a chest.")

            if has_key:
                print("🔓 You used the key to open the chest.")
                print("⚔️ You found a sword!")
                has_sword = True
            else:
                print("The chest is locked. You need a key.")

            print("\nA guard attacks you!")

            choice3 = input("Fight or run? ").lower()

            if choice3 == "fight":
                if has_sword:
                    print("⚔️ You defeated the guard!")
                    print("🏆 You escaped with treasure! YOU WIN 🎉")
                else:
                    print("❌ You have no weapon. You lost!")
            elif choice3 == "run":
                print("You escaped safely.")
            else:
                print("Invalid choice. Game Over ❌")

        elif choice2 == "no":
            print("You stayed outside and nothing happened. Game Over ❌")
        else:
            print("Invalid choice. Game Over ❌")

    else:
        print("Invalid choice. Game Over ❌")


# Run the game
game()