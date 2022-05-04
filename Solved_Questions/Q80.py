"""
1.	Define a class to represent a bank account. Include the following members:

Data Members:
a.Name of the Depositor
b.Account Number
c.Type of Account
d.Balance amount in the account

Data Methods:
a.To assign initial values
b.To deposit an amount
c.To withdraw an amount
d.To display name and balance.

Output:
1.	New customer
2.	Deposit
3.	Withdrawal
4.	Display
5.	Exit

"""
class Bank_Account:

    def customer_name_account(self):
        self.Name_of_customer = str(input("Enter Name of customer : "))
        self.Account_no = int(input("Enter Account number : "))
        self.Type_of_Account = str(input("Enter type of Account : "))
    def assign_intial_value(self):
        self.Balance_amount = 5000
    def deposit_an_amount(self):
        self.deposite_amount = int(input("Enter the deposite amount in Rs. "))
        self.total_amount = self.Balance_amount + self.deposite_amount
    def withdraw_an_amount(self):
        self.withdraw_amount = int(input("Enter the withdraw amount Rs. "))
        if self.total_amount <= self.withdraw_amount:
            print("Insufficient Fund")
        self.remaining_amount = self.total_amount - self.withdraw_amount
    def display_name_and_balance(self):
        print("Name of Customer : ",self.Name_of_customer)
        print("Account No : ",self.Account_no)
        print("Account Type : ",self.Type_of_Account)
        print("Total Account Balance is : Rs.",self.remaining_amount)
    def menu_program(self):
        while True:
            print("*** Menu ***\n1.New Customer\n2.Deposit\n3.Withdrawal\n4.Display\n5.Exit")
            choice = int(input("Enter the menu choice : "))
            if choice == 1:
                self.customer_name_account()
                self.assign_intial_value()
            if choice == 2:
                self.deposit_an_amount()
            if choice == 3:
                self.withdraw_an_amount()
            if choice == 4:
                self.display_name_and_balance()
            if choice == 5:
                print("DATA SAVE SUCCESFULLY")
                break
            else:
                pass


c1 = Bank_Account()
c1.menu_program()
