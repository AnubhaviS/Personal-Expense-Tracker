import os
from datetime import datetime

DATA_FILE = "expenses.txt"


def add_expense(amount, category, note):
    
    date = datetime.now().strftime("%Y-%m-%d")
    entry = f"{date},{amount},{category},{description}\n"

    with open(DATA_FILE, "a") as file:
        file.write(entry)


def read_expenses():
    expenses = []

    if not os.path.exists(DATA_FILE):
        return expenses

    with open(DATA_FILE, "r") as file:
        for line in file:
            date, amount, category, note = line.strip().split(",")
            expenses.append({
                "date": date,
                "amount": float(amount),
                "category": category,
                "note": note
            })

    return expenses


def show_all_expenses():
    expenses = read_expenses()

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print(
            f"{exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}"
        )


def show_category_summary():
    expenses = read_expenses()
    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n--- Category-wise Summary ---")
    for category, total in summary.items():
        print(f"{category}: ₹{total}")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                note = input("Note: ")
                add_expense(amount, category, note)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "2":
            show_all_expenses()

        elif choice == "3":
            show_category_summary()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()