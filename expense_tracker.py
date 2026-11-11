import math


expenses = []


def add_expense():
    description = input("Description: ")
    amount = float(input("Amount: "))
    expenses.append({
        "description": description,
        "amount": amount
    })
    print("Expense added!")


def show_expenses():
    if len(expenses) == 0:
        print("There's no expenses yet")
    else:
        print("\nExpenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense}")


def show_total():
    total = sum(expenses)
    print(f"Total expenses: {total}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
