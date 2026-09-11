import random
d={}
def sign_up():
    name=input('ENTER YOUR NAME AS PER ADHAAR ID:')
    password=input("ENTER THE PASSWORD FOR YOUR ACCOUNT:")
    balance=int(input("ENTER THE INITIAL AMOUNT YOU WANT TO DEPOSIT:"))
    account=random.randint(10000,99999)
    d[account] = {
        "NAME": name,
        "PASSWORD": password,
        "BALANCE": balance,
    }
    print(f"ACCOUNT CREATED SUCCESSFUL 🎉 THANK YOU FOR CHOOSING OUR BANK 🙏")
    print(f"YOUR ACCOUNT NAME IS:{name}\nYOUR ACCOUNT NUMBER IS:{account}")
    
def checkbalance():
    print(f"YOUR CURRENT BANK BALANCE IS:{d[account]['BALANCE']}")
    
def deposit():
    deposit_amount=int(input("HOW MUCH YOU WANT TO DEPOSIT:"))
    d[account]['BALANCE']+=deposit_amount
    print(f"✅AMOUNT DEPOSITED SUCCESSFULLY")
    print(f"YOUR CURRENT BANK BALANCE IS:{d[account]['BALANCE']}")
    
    
def withdraw():
    withdraw_amount=int(input("HOW MUCH YOU WANT TO WITHDRAW:"))
    if withdraw_amount>d[account]['BALANCE']:
        print(f"❌ YOU HAVE INSUFFICIENT BALANCE !")
    else:
        d[account]['BALANCE']=d[account]['BALANCE']-withdraw_amount
        print(f"✅TRANSACTION SUCCCESSFULL\nTRANSACTION ID IS:{random.randint(100000,999999)}")
        print(f"YOUR CURRENT BANK BALANCE IS:{d[account]['BALANCE']}")
print("-----------------------------")
print("     WELCOME TO OUR BANK     ")
print("-----------------------------")
while True:
    print("         1.SIGN IN           ")
    print("     2.NEW USER?REGISTER     ")
    print("            3.EXIT           ")
    print("-----------------------------")
    ch=int(input("ENTER YOUR CHOICE:"))
    if ch==1:
        
        account=int(input("ENTER ACCOUNT NUMBER : "))
        password=input("ENTER YOUR PASSWORD : ")
        if account in d and password==d[account]['PASSWORD']:
            print('LOGIN SUCCESSFULL')
            while True:
                
                print("1.CHECK BALANCE\n2.DEPOSIT\n3.WITHDRAW\n4.EXIT")
                choice=int(input("ENTER YOUR CHOICE(1-4):"))
                if choice==1:
                    checkbalance()
                elif choice==2:
                    deposit()
                elif choice==3:
                    withdraw()
                elif choice==4:
                    print("THANK YOU")
                    break
                else:
                    print("Oops! PLEASE ENTER VALID CHOICE ")
                    
                    
        else:
            print("❌INAVLID NAME OR INVALID PASSWORD !")
    elif ch==2:
        sign_up()
    elif ch==3:
        break
    else:
        print("PLEASE ENTER VALID CHOICE")
    
