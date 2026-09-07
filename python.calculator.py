print("===== CALCULATOR =====")

result = float(input("Enter number: "))

while True:
    operator = input("Enter operator (+, -, *, /, %, **): ")

    if operator.lower() == "exit":
        print("Calculator closed.")
        break

    num2 = float(input("Enter number: "))

    if operator == "+":
        result += num2

    elif operator == "-":
        result -= num2

    elif operator == "*":
        result *= num2

    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
            continue
        result /= num2

    elif operator == "%":
        result %= num2

    elif operator == "**":
        result **= num2

    else:
        print("Invalid operator!")
        continue

    print("=", result)

# import tkinter as tk

# # Create window
# window = tk.Tk()
# window.title("Calculator")
# window.geometry("350x500")
# window.resizable(False, False)

# # Display
# display = tk.Entry(
#     window,
#     font=("Arial", 28),
#     justify="right",
#     bd=10
# )
# display.pack(fill="both", padx=10, pady=10, ipady=15)


# # Add value to display
# def click(value):
#     display.insert(tk.END, value)


# # Clear display
# def clear():
#     display.delete(0, tk.END)


# # Calculate result
# def calculate():
#     try:
#         expression = display.get()
#         result = eval(expression)
#         display.delete(0, tk.END)
#         display.insert(0, result)

#     except:
#         display.delete(0, tk.END)
#         display.insert(0, "Error")


# # Change positive/negative
# def plus_minus():
#     try:
#         value = float(display.get())

#         display.delete(0, tk.END)
#         display.insert(0, -value)

#     except:
#         pass


# # Buttons
# buttons = [
#     ("AC", 0, 0),
#     ("+/-", 0, 1),
#     ("%", 0, 2),
#     ("/", 0, 3),

#     ("7", 1, 0),
#     ("8", 1, 1),
#     ("9", 1, 2),
#     ("*", 1, 3),

#     ("4", 2, 0),
#     ("5", 2, 1),
#     ("6", 2, 2),
#     ("-", 2, 3),

#     ("1", 3, 0),
#     ("2", 3, 1),
#     ("3", 3, 2),
#     ("+", 3, 3),

#     ("0", 4, 0),
#     (".", 4, 1),
#     ("=", 4, 2),
# ]


# # Create buttons
# for text, row, column in buttons:

#     if text == "AC":
#         command = clear

#     elif text == "=":
#         command = calculate

#     elif text == "+/-":
#         command = plus_minus

#     else:
#         command = lambda value=text: click(value)

#     button = tk.Button(
#         window,
#         text=text,
#         font=("Arial", 18),
#         command=command
#     )

#     button.grid(
#         row=row,
#         column=column,
#         padx=5,
#         pady=5,
#         ipadx=15,
#         ipady=15
#     )


# # Start calculator
# window.mainloop()

# import tkinter as tk

# window = tk.Tk()
# window.title("Calculator")
# window.geometry("350x500")
# window.resizable(False, False)

# display = tk.Entry(
#     window,
#     font=("Arial", 28),
#     justify="right",
#     bd=10
# )
# display.pack(fill="x", padx=10, pady=10, ipady=15)

# result = 0
# operator = None
# new_number = True


# def number(value):
#     global new_number

#     if new_number:
#         display.delete(0, tk.END)
#         new_number = False

#     display.insert(tk.END, value)


# def operation(op):
#     global result, operator, new_number

#     try:
#         current = float(display.get())
#     except ValueError:
#         return

#     if operator is None:
#         result = current

#     else:
#         calculate(current)

#     operator = op
#     new_number = True


# def calculate(current=None):
#     global result, operator, new_number

#     if current is None:
#         try:
#             current = float(display.get())
#         except ValueError:
#             return

#     if operator == "+":
#         result = result + current

#     elif operator == "-":
#         result = result - current

#     elif operator == "*":
#         result = result * current

#     elif operator == "/":
#         if current == 0:
#             display.delete(0, tk.END)
#             display.insert(0, "Error")
#             result = 0
#             operator = None
#             new_number = True
#             return

#         result = result / current

#     display.delete(0, tk.END)
#     display.insert(0, str(result))

#     operator = None
#     new_number = True


# def equal():
#     calculate()


# def clear():
#     global result, operator, new_number

#     result = 0
#     operator = None
#     new_number = True

#     display.delete(0, tk.END)


# def plus_minus():
#     try:
#         current = float(display.get())
#         current = -current

#         display.delete(0, tk.END)
#         display.insert(0, str(current))

#     except ValueError:
#         pass


# # Buttons

# buttons = [
#     ("AC", clear),
#     ("+/-", plus_minus),
#     ("%", lambda: percentage()),
#     ("/", lambda: operation("/")),

#     ("7", lambda: number("7")),
#     ("8", lambda: number("8")),
#     ("9", lambda: number("9")),
#     ("*", lambda: operation("*")),

#     ("4", lambda: number("4")),
#     ("5", lambda: number("5")),
#     ("6", lambda: number("6")),
#     ("-", lambda: operation("-")),

#     ("1", lambda: number("1")),
#     ("2", lambda: number("2")),
#     ("3", lambda: number("3")),
#     ("+", lambda: operation("+")),

#     ("0", lambda: number("0")),
#     (".", lambda: number(".")),
#     ("=", equal),
# ]


# def percentage():
#     try:
#         current = float(display.get())
#         current = current / 100

#         display.delete(0, tk.END)
#         display.insert(0, str(current))

#     except ValueError:
#         pass


# # Create buttons

# row = 0
# column = 0

# for text, command in buttons:

#     button = tk.Button(
#         window,
#         text=text,
#         font=("Arial", 18),
#         command=command
#     )

#     button.grid(
#         row=row,
#         column=column,
#         padx=5,
#         pady=5,
#         ipadx=15,
#         ipady=15
#     )

#     column += 1

#     if column == 4:
#         column = 0
#         row += 1


# window.mainloop()