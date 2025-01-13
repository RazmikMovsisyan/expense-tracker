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