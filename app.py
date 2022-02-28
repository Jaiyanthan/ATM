class ATM:
    def __init__(self, account_balance=0):
        self = self
        self.account_balance = account_balance

    def withDraw(self):
        Org_CardNumber = "1234_4567_8901"
        Org_PinNUmber = "4858"
        CardNumber = input("Enter your card number")
        PinNumber = input("Enter your pin number")
        if CardNumber == Org_CardNumber and PinNumber == Org_PinNUmber:
            amount = input("Enter the amount to withdraw")
            print("Process Successful")
            reciept = input("Reciept ?  y for Yes and n for No")
            if  reciept == 'y':
                print(f'₹{amount} has been withdrawed by user. Thank You')
        else:
            print("Incorrect Card No or Pin No")

    def balanceCheck(self):
         Org_CardNumber = "1234_4567_8901"
         Org_PinNUmber = "4858"
         CardNumber = input("Enter your card number")
         PinNumber = input("Enter your pin number")
         if CardNumber == Org_CardNumber and PinNumber == Org_PinNUmber:  
             print(f'Your account balance is {self.account_balance}')
         else:
            print("Incorrect Card No or Pin No")           

    def cashDeposit(self):
        Org_CardNumber = "1234_4567_8901"
        Org_PinNUmber = "4858"
        CardNumber = input("Enter your card number")
        PinNumber = input("Enter your pin number")
        if CardNumber == Org_CardNumber and PinNumber == Org_PinNUmber:  
             dep_amount = input("Enter your deposit amount")
             self.account_balance = int(dep_amount) + self.account_balance            

        else:
            print("Incorrect Card No or Pin No")          

Input = input("What do you want ? '\n' 1.For Withdrawal enter(w) '\n' 2.For deposit enter(d) '\n' 3.For account balance press(b)")
My_ATM = ATM()

if Input == 'w':
    My_ATM.withDraw()
if Input == 'b':
    My_ATM.balanceCheck()
if Input == 'd':
    My_ATM.cashDeposit()

# else:
#     print("Enter a valid answer")        