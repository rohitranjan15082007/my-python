import random
import string

# -----------------------------
# SETTINGS
# -----------------------------
TOTAL_TICKETS = input("enter the number of ticket : ")

# -----------------------------
# GENERATE UNIQUE TICKET ID
# -----------------------------
def generate_ticket_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=5))
    return f"{letters}{numbers}"

# -----------------------------
# GENERATE MULTIPLE TICKETS
# -----------------------------
tickets = []

for i in range(TOTAL_TICKETS):
    ticket = {
        "ticket_id": generate_ticket_id(),
        "status": "unscratched",
        "user_id": None
    }
    tickets.append(ticket)

# -----------------------------
# PRINT SAMPLE
# -----------------------------
print("Total Tickets Generated:", len(tickets))
print("\nSample Tickets:")
for t in tickets[TOTAL_TICKETS]:  # Print first 100 tickets as a sample
    print(t)