atm_Pin = 1234
account_balance = 1000
if account_balance <= 0:
    print("Your account has insufficient funds. Please deposit money to continue.")
elif account_balance > 0:
    print("Welcome to the ATM Simulator!")
    entered_pin = int(input("Please enter your 4-digit PIN: "))
    if entered_pin == atm_Pin:
        print("PIN accepted. You can now perform transactions.")
        transaction_choice = input("Would you like to (1) Check Balance, (2) Withdraw, or (3) Deposit? Enter 1, 2, or 3: ")
        if transaction_choice == "1":
            print(f"Your current balance is: ${account_balance}")
        elif transaction_choice == "2":
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            if withdraw_amount <= account_balance:
                account_balance -= withdraw_amount
                print(f"Withdrawal successful. Your new balance is: ${account_balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        elif transaction_choice == "3":
            deposit_amount = float(input("Enter the amount to deposit: "))
            account_balance += deposit_amount
            print(f"Deposit successful. Your new balance is: ${account_balance}")
        else:
            print("Invalid choice. Please restart the ATM Simulator.")
    else:
        print("Incorrect PIN. Access denied.")