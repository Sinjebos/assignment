
def login():
    print("Welcome to the bank of Zeros and Ones!")
    user_login = True
    while user_login:
        try:
            pinkod = int(input("Enter your pin, 4 or 6 digits: "))
            if pinkod >= 1000 and pinkod <= 999999:
                print("Valid pin. Welcome human")
                user_login = False
            else:
                print("Invalid pin")
        except Exception:
            print("Invalid pin")


def account():
    balance = 0
    bank = True
    try:
        while bank:
            option = int(input(("What do you wanna do?\n[1] Deposit money.\n[2] Withdraw money.\n[3] Check balance.\n[4] Collect interest.\n[5] End.\nOption :: ")))
            if option == 1:
                deposit = float(input("How much do you wanna deposit?\nAmount ::  "))
                balance = balance + deposit
                print(f"Current balance is: {balance}")
            elif option == 2:
                withdraw = float(input("How much do you wann withdraw?\nAmount :: "))
                balance = balance - withdraw
                print(f"Current balance is: {balance}")
            elif option == 3: 
                print(f"Current balance is: {balance}")
            elif option == 4:
                pass
            elif option == 5:
                print("See ya later alligator")
                bank = False
    except Exception:
        print("Invalid input")


# fixa senare, fattar ej vad som händer på koden under
'''
def interest():
    years_to_skip = int(input("How many years of interest do you seek to collect?\nAmount of years :: "))
    if 1 < balance < 1000:
        balance = balance * years_to_skip
        print(f"Your balance is now {balance}")
    elif 1001 < balance < 5000:
        balance = balance * years_to_skip
        print(f"Your balance is now {balance}")        
    elif 5001 < balance < 10000:
        balance = balance * years_to_skip
        print(f"Your balance is now {balance}")
    elif balance > 10001:
        balance = balance * years_to_skip
        print(f"Your balance is now {balance}")
    else:
        print("You dont have enough money")
'''

login()
account()