from expense import Expense
import calendar  # module to handle month range and days
import datetime  # module to work with current date and time

EXPENSE_FILE_PATH = "expenses.csv"  
BUDGET = 2000

def main():
    print(f"Running Expense Tracker!")
    
    # Get user to input an expense
    expense = get_user_expense()

    # Write the expenses to a file
    save_expense_to_file(expense, EXPENSE_FILE_PATH)

    # Read file and summarize all expenses
    summarize_expenses(EXPENSE_FILE_PATH, BUDGET)
    
def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")

    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break  # break out of loop if valid input
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}") # to start from 1 instead of 0

        value_range = f"[1 - {len(expense_categories)}]" #length of categories instead of manual typing
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(
                    name=expense_name, category=selected_category, amount=expense_amount
                )
                return new_expense
            else:
                print("Invalid category. Please try again!")
        except ValueError:
            print("Invalid input. Please enter a valid category number.")
    
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expenses(expense_file_path, budget):
    print(f"🎯 Summarizing User Expense")
    
    expenses = []  # empty list to hold expense objects
    with open(expense_file_path, "r") as f:
        for line in f:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}  # a dictionary to store the sum of expenses depending on which category
    for expense in expenses:
        amount_by_category[expense.category] = amount_by_category.get(expense.category, 0) + expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum(expense.amount for expense in expenses)
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days if remaining_days > 0 else 0
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m" #print text in green color for emphasis

if __name__ == "__main__":
    main()  #call the main function to run the script
