amount = float(input("Enter the bill amount: "))
if amount >= 10000:
    discount = amount * 0.25
    final_amount = amount - discount
    print(f"You have received a 25% discount. The final bill amount is: {final_amount}")
elif amount >= 5000:
    discount = amount * 0.15
    final_amount = amount - discount
    print(f"You have received a 15% discount. The final bill amount is: {final_amount}")
elif amount >= 1000:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"You have received a 10% discount. The final bill amount is: {final_amount}")
elif amount < 999:
    discount = amount * 0.05
    final_amount = amount - discount
    print(f"You have received a 5% discount. The final bill amount is: {final_amount}")

else:
    print("No discount applicable.")