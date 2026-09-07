item = str(input("enter the item name: "))
price = float(input("enter the item price: "))
dish = 20 - len(item)-len(str(price))
print(item + "== " * dish + str(price))