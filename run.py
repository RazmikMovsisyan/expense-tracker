from expense import Expense

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
    print(f"Getting User Expense")
    expense_name = input("Enter expense name: ")

    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break  # break out of loop if valid input
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc",
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