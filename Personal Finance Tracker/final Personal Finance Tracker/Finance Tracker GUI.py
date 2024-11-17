import tkinter as tk
from tkinter import ttk
import json

class FinanceTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")# Set window title
        self.root.title=ttk.Frame(self.root, width=400, height=50)
        self.root.resizable(False,False)
        self.create_widgets()# Call method to create GUI widgets
        self.transactions = self.load_transactions("transactions.json")# Load transactions from file

    def create_widgets(self):
        
        #Title name lable
        label=tk.Label(self.root.title,text='Personal Finance Tracker')
        label['font']=('Britannic Bold',15)
        label.pack()
        self.root.title.pack()
        
        # Frame for table and scrollbar
        self.frame = ttk.Frame(self.root, width=400, height=300, borderwidth=10, relief=tk.GROOVE)
        self.frame.pack_propagate(False)
        self.frame.pack(side='bottom')

        # Treeview for displaying transactions
        self.treeview=ttk.Treeview(self.frame, columns=('Category','Amount','Date'), show= 'headings')
        self.treeview.heading('Category', text='Category', command=lambda: self.sort_by_column("Category", False))
        self.treeview.heading('Amount', text='Amount', command=lambda: self.sort_by_column("Amount", False))
        self.treeview.heading('Date', text='Date', command=lambda: self.sort_by_column("Date", False))
        self.treeview.column('Category', width=100)
        self.treeview.column('Amount', width=100)
        self.treeview.column('Date', width=100)
        self.treeview.pack(fill='both', expand=True)

        # Scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(self.treeview, orient='vertical', command=self.treeview.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        # Search bar and button
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.root, textvariable=self.search_var)
        self.search_entry.pack(side="top")
        self.search_button = ttk.Button(self.root, text="Search", command=self.search_transactions)
        self.search_button.pack(side="top")
        
    def load_transactions(self, filename):
        try:
            with open("FinanceTracker.json", "r") as file:
                transactions = json.load(file)# Load transactions from JSON file
        except FileNotFoundError:
            transactions = {}# If file not found, initialize transactions as empty dictionary
        return transactions        

    def display_transactions(self, transactions):
        # Remove existing entries
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Add transactions to the treeview
        for category, transactions_list in transactions.items():
            for transaction_dict in transactions_list:
                self.treeview.insert('', 'end', values=(category, transaction_dict['amount'], transaction_dict['date']))

    def search_transactions(self):
        # Placeholder for search functionality
        query = self.search_var.get().lower()
        filtered_transactions = {}
        for category, category_transactions in self.transactions.items():
            filtered_category_transactions = []
            for transaction in category_transactions:
                if query in str(transaction["amount"]).lower() or query in transaction["date"].lower() or query in category.lower():
                    filtered_category_transactions.append(transaction)
            if filtered_category_transactions:
                filtered_transactions[category] = filtered_category_transactions
        self.display_transactions(filtered_transactions)

    def sort_by_column(self, col, reverse):
        # Placeholder for sorting functionality
        data = [(self.treeview.set(child, col), child) for child in self.treeview.get_children("")]
        data.sort(reverse=reverse)
        for index, (val, child) in enumerate(data):
            self.treeview.move(child, "", index)
        self.treeview.heading(col, command=lambda: self.sort_by_column(col, not reverse))        

def main():
    root = tk.Tk()
    app = FinanceTrackerGUI(root)
    app.display_transactions(app.transactions)# Display transactions on startup
    root.mainloop()

if __name__ == "__main__":
    main()
