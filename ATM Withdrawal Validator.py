balance=int(input(" Enter your bank balance =>"))
withdrawal=int(input("Enter your withdrawal amount =>"))

if(balance>=withdrawal and withdrawal>=100):
    print("Withdrawal!")
    print("Deduct 10 rupees transaction fee \n Available Balance =>",(balance-withdrawal)-10)
    

else:
    print("Please check the balance or withdrawal 100 or more ! ")    