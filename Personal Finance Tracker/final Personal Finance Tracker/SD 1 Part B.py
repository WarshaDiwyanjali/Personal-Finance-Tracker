#importing json
import json

# Global dictionary to store transactions
FILENAME = "FinanceTracker.json"

   # File handling functions

# Function to load transactions from the file
def load_transactions():
    try:
        with open(FILENAME, "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {}  # If file not found, initialize an empty dictionary
    return transactions

# Function to save transactions to the file
def save_transactions(transactions):
    with open(FILENAME, "w") as file:
        json.dump(transactions, file, indent=2)

# Function to read transactions from a file
def read_bulk_transactions_from_file(filename):
    try:
        with open(filename, "r") as file:
            transactions = json.load(file)
        return transactions
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {}  # If file not found, return an empty dictionary

# Feature implementations

# Function to add a new transaction
def add_transaction(category, amount, date):
    transactions = load_transactions()  # Load existing transactions
    if category not in transactions:
        transactions[category] = []  # If category doesn't exist, create a new one
    transactions[category].append({"amount": amount, "date": date})  # Add new transaction
    save_transactions(transactions)  # Save updated transactions to the file
    print("Transaction added!")

# Function to view all transactions
def view_transactions():
    all_transactions = load_transactions()  # Load all transactions
    for category, transactions in all_transactions.items():
        print(f"{category}:")
        for index, transaction in enumerate(transactions, start=1):
            print(f" {index}. Amount: {transaction['amount']}, Date: {transaction['date']}")
        print()

def delete_transaction(category, index):
    transactions = load_transactions()  # Load existing transactions
    new_index = index - 1
    if category in transactions and 0 <= new_index < len(transactions[category]):
        del transactions[category][new_index]  # Delete transaction
        if len(transactions[category]) == 0:
            del transactions[category]  # If no transactions left in the category, delete the category
        save_transactions(transactions)  # Save updated transactions to the file
        print("Transaction Deleted!")
    else:
        print("Invalid category or index!")

# Function to update a transaction
def update_transaction(category, index, amount, date):
    transactions = load_transactions()  # Load existing transactions
    new_index = index - 1
    if category in transactions and 0 <= new_index < len(transactions[category]):
        transactions[category][new_index] = {"amount": amount, "date": date}  # Update transaction
        save_transactions(transactions)  # Save updated transactions to file
        print("Successfully Updated!")
    else:
        print("Invalid category or index!")

# Function to display summary of transactions
def display_summary():
    all_transactions = load_transactions()  # Load all transactions
    for category, transactions in all_transactions.items():
        total_amount = sum(transaction['amount'] for transaction in transactions)  # Calculate total amount
        print(f"{category}: Total Amount: {total_amount}")

# Function to launch gui
def launch_gui():
    import subprocess
    subprocess.run(["python", "Finance Tracker GUI.py"])

# Main menu function
def main_menu():
    while True:
        print("\n1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Summary of Transaction")
        print("5. Delete Transaction")
        print("6. Launch GUI")         
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(category, amount, date)
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_transactions()
            category = input("Enter category: ")
            index = int(input("Enter index to update: "))
            amount = float(input("Enter new amount: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            update_transaction(category, index, amount, date)
        elif choice == "4":
            display_summary()
        elif choice == "5":
            view_transactions()
            category = input("Enter category: ")
            index = int(input("Enter index to delete: "))
            delete_transaction(category, index)
        elif choice == "6":
            launch_gui()            
        elif choice == "7":
            print("Thanks for using FinanceTracker!")
            break
        else:
            print("Invalid choice!")

# Entry point of the program
if __name__ == "__main__":
    main_menu()  # Call the main_menu function to start the program
