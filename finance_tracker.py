# Finance Tracker Application
# This application allows users to track their expenses by category.

def add_expenses(expenses):
    ''' Function to add expenses to the tracker. '''

    while True:
        description = input("\nEnter expense description: ")
        category = input("Enter category: ")
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError:
            print("Invalid amount. Please try again.")
            continue

        if category not in expenses:
            expenses[category] = []

        expenses[category].append((description, amount))
        print("Expense added successfully.")

        another = input("Add another expense? (y/n): ").lower()
        if another != 'y':
            break

    return expenses

def view_expenses(data):
    ''' Function to view all expenses by category. '''
    if not data:
        print("No expenses recorded yet.")
        return
    
    for category, expenses in data.items():
        print(f"\nCategory: {category}")
        for desc, amt in expenses:
            print(f"  - {desc}: ${amt:.2f}")

def view_summary(data):
    ''' Function to view a summary of expenses by category. '''
    if not data:
        print("No expenses recorded yet.")
        return

    print("\nSummary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")

def main():
    ''' Main function to run the Finance Tracker application. '''
    print("Welcome to the Finance Tracker!")
    expenses = {}
    while True:
        choice = input("\nChoose an option:\n1. Add Expenses\n2. View Expenses\n3. View Summary\n4. Exit\n> ")
        
        if choice == '1':
            expenses = add_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_summary(expenses)
        elif choice == '4':
            print(expenses)
            print("Exiting Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()