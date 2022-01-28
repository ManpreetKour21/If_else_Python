language=input("enter your language=")
if language=="english":
    print("choose your transaction\n1.balance enquary\n2.withdraw money\n3.deposit\n5.transfer money\n6.quite")
    transaction=input("enter your transaction=")
    if transaction=="balance enquary":print
        swipe=input("do you want swipe your card=")
        if swipe=="yes":
            atm_pin=9140
           ("atm programm\nwelcome to my atm\nswipe your card here")
 pin=int(input("enter your pin"))
            if pin==balance=10,000
atm_pin:
                print("here you swipe your card,thanks for using")
            else:
                print("wrong pin")
        else:
            print("thanks for using atm")
    elif transaction=="withdraw money":
        balance=int(input("enter your balance="))
        amount=int(input("enter your amount="))
        total=balance-amount
        if amount>0:
            atm_pin=9140
            pin=int(input("enter your pin"))
            if pin==atm_pin:
                print(total)
                print("collect your cash")
            else:
                print("wrong pin")
        else:
            print("enter a valid amount to proceed")
    elif transaction=="deposit":
        balance=int(input("enter your balance="))
        deposit=int(input("enter your deposit amount="))
        total=balance+deposit
        if deposit>0:
            atm_pin=9140
            pin=int(input("enter your pin"))
            if pin==atm_pin:
                print(total)
                print("your deposit is done successsfully and thanks for using atm")
            else:
                print("wrong pin")
        else:
            print("enter a valid deposit amount")
    elif transaction=="transfer_money":
        balance=int(input("enter your balance="))
        transfer_money=int(input("enter your amout to transfer money="))
        total=balance-transfer_money
        if transfer_money>0:
            atm_pin=9140
            pin=int(input("enter your pin"))
            if pin==atm_pin:
                print(total)
                print("your money has been transfered and thanks for using atm")
            else:
                print("wrong pin")
        else:
            print("please enter a valid amount to proceed")
    elif transaction=="quite":
        quite=input("enter yes if you want to quite=")
        if quite=="yes":
            atm_pin=9140
            pin=int(input("enter your pin"))
            if pin==atm_pin:
                print("quite")
            else:
                print("wrong pin")
        else:
            print("choose any transaction please")
    else:
        print("wrong pin,try again")
else:
    print("language is not found")