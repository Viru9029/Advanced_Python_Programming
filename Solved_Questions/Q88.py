#Q6: Write a python program to create user-defined exception
class Error(Exception):
    """Base class for below user defined exception"""

class BudgetIsHigh(Error):
    """Raised when customer budget is high"""

class BudgetIsLow(Error):
    """Raised when customer budget is Low"""

InBudget_Value = 2000
while True :
    Customer_Budget = int(input("Enter the Customer Budget : "))

    try:
        if Customer_Budget < InBudget_Value:
            raise BudgetIsLow
        elif Customer_Budget > InBudget_Value:
            raise BudgetIsHigh
    except BudgetIsLow:
        print("This value is below the budget")

    except BudgetIsHigh:
        print("This value is Above the budget")

    print("You guessed it correctly!")

