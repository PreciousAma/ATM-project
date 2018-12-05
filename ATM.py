#this is a python program for Atms', of Precious bank.

def main():
    user1_pin = "4565"
    user2_pin = "1234"
    user1_name =  "Chilaka Precious"
    user2_name =  "Femi Kolade"
    user1_amount = 500000
    user2_amount = 700000
    print("Welcome to Precious bank")
    tryagain = "2"
    while(tryagain == "2"):
        chances = 3
        while(chances is not 0):
            pin = input("Please enter your 4 digits pin: ")
            if(pin == "4565" or pin == "1234"):
                chances = 0
                if(pin == "4565"):
                    print("Welcome " + user1_name)
                    user1_amount = account_type(user1_amount)
                else:
                    print ("Welcome " + user2_name)
                    user2_amount = account_type(user2_amount)
            else:
                print("incorrect pin\n try again")
                chances = chances - 1
        tryagain = input("1)End Transaction \n2)Make another transaction\n>>>")
        if(tryagain == "1"): print("Thanks for banking with us")
            
def withdrawal(user_amount):
    while(True):
        withdrawal_amount = int(input("Please enter amount: "))
        if(withdrawal_amount <= user_amount):
                user_amount = user_amount - withdrawal_amount
                print("transaction compeleted \ntake your cash")
                return user_amount
        else: print("insufficient funds\n try again")       
    
def account_type(user_amount):
    while(True):
        print("Select account type by inputing the number")
        Type = input("1.)Savings  \n2.)Current\n>>>")
        if( Type == "1"):
            user_amount = prompt(user_amount)
            return user_amount
        elif(Type == "2"):
            user_amount = prompt(user_amount)
            return user_amount
        else:
            print("invalid selection try again")

def deposit(user_amount):
        amount_to_deposit = int(input("Enter amount to be deposited: "))
        user_amount = user_amount + amount_to_deposit
        print("transaction completed")
        return user_amount
        
def recharge(user_amount):
    while(True):
        withdrawal_amount = int(input("Please enter amount to recharge: "))
        if(withdrawal_amount <= user_amount):
            user_amount = user_amount - withdrawal_amount
            print("transaction compeleted")
            return user_amount
        else:
            print("insufficient funds\n try again")

def prompt(user_amount):
    print("Select Operation")
    print("1) Withdrawal \t\t3) Balance \n2) deposit \t\t4) Recharge")
    selection = input(">>> ")
    while(True):
        if(selection == "1"):
            user_amount = withdrawal(user_amount)
            return user_amount
        elif(selection == "2"):
            user_amount = deposit(user_amount)
            return user_amount
        elif(selection == "3"):
            print("Your account balance is: " + str(user_amount))
            return user_amount
        elif(selection == "4"):
            user_amount = recharge(user_amount)
            return user_amount
        else: print("invalid selection please try again")
        
main()
