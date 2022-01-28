print("welcome to ATM")
print("Enter your card")
pin=9999
total_balance=0
total=10000
pin_=int(input("Enter your Pin: "))
if pin_==pin:
    print("\nselect your options: \n1.Check your balance \n2.Deposite \n3.Withdrow:")
    user=input("Enter What you want:")
    if user=="1" or user=="check balance":
        print(total)
        print("\nThanks for using ATM\nHave a Good Day ")

    elif user=="2" or user=="deposite":
        deposite=int(input("enter how much you want to deposite:"))
        total_balance=(total+deposite)
        print("\nyou deposite successfully your main balance is ",total_balance)
        print("Thanks for using ATM\nHave a Good Day ")

    elif user=="3" or user=="withdrow":
        withdrow=int(input("enter how much you want to withdrow:"))
        if withdrow>total:
            print("your main balance is less")
            print("Thanks for using ATM\nHave a Good Day ")
        elif withdrow<total:
            total_balance=(total-withdrow)
            print("\nsuccessfully withdrow your balance is ",total_balance)
            print("Thanks for using ATM\nHave a Good Day ")
    else:
        print("Thanks for using ATM\nHave a Good Day 🥰🥰🥰🥰🥰🥰🥰🥰🥰")
else:
    print("your Pin is wrong")



