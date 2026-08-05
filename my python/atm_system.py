# ATM System
# user_name = input("Enter your username: ")
# password = input("Enter your password: ")

# if user_name == "Rajivjindal" and password == "Rajiv@123":
#     print("✅ Login successful!")
# else:
#     print("❌ Invalid username or password. Please try again.")
#     while true:
#         user_name = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if user_name == "Rajivjindal" and password == "Rajiv@123":
#             print("✅ Login successful!")
#             break
#         else:
#             print("❌ Invalid username or password. Please try again.")
# choice = input("Do you want to (1) Check Balance, (2) Withdraw, or (3) Deposit or (4) Exit? enter 1, 2, 3 or 4: ")

# account_balance = 1000.0  # Initial account balance

# if choice == "1":
#     print(f"Your current balance is: ${account_balance:.2f}")

# def deposit(amount):
#     global account_balance
#     if amount > 0:
#         account_balance += amount
#         print(f"✅ Deposited: ${amount:.2f}. New balance: ${account_balance:.2f}")
#     else:
#         print("❌ Deposit amount must be positive.")

# if choice == "3":
#     deposit_amount = float(input("Enter the amount to deposit: "))
#     while deposit_amount <= 0:
#         print("❌ Deposit amount must be positive. Please try again.")
#         deposit_amount = float(input("Enter the amount to deposit: "))
#     deposit(deposit_amount)

# if choice == "2":
#     withdraw_money = float(input("Enter the amount to withdraw: "))
#     while withdraw_money <= 0:
#         print("❌ Withdrawal amount must be positive. Please try again.")
#         withdraw_money = float(input("Enter the amount to withdraw: "))
#     if withdraw_money <= account_balance:
#         account_balance -= withdraw_money
#         print(f"✅ Withdrawal successful. New balance: ${account_balance:.2f}")
#     else:
#         print("❌ Insufficient funds for this withdrawal.")

#     if account_balance <= 0:
#         print("❌ Your account has insufficient funds. Please deposit money to continue.")



# chat gpt answer
# Correct credentials
correct_username = "Rajivjindal"
correct_password = "Rajiv@123"

# Login
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print("✅ Login successful!\n")
    
    account_balance = 1000.0  # Initial balance

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"💰 Current Balance: ${account_balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                account_balance += amount
                print(f"✅ Deposited: ${amount:.2f}")
            else:
                print("❌ Invalid amount")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("❌ Invalid amount")
            elif amount > account_balance:
                print("❌ Insufficient balance")
            else:
                account_balance -= amount
                print(f"✅ Withdrawn: ${amount:.2f}")

        elif choice == "4":
            print("👋 Thank you for using ATM!")
            break

        else:
            print("❌ Invalid choice")

else:
    print("❌ Invalid login. Program stopped.")