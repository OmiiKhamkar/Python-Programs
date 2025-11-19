u=int(input("Enter the Unites =>"))

if(u<=100):
    print("Your bill price is",u*5)
elif(u>100 and u<=200):
    print("Your bill price is",u*7)
elif(u>200 and u<=300):
    print("Your bill price is",u*10)
    if(u*10>=2000):
        print("your bill is Above 2000")
        print("Paid extra 10% charge =>",(u*10)/10)
elif(u>300):
    print("Your bill price is",u*12) 
    if(u*12>=2000):
        print("your bill is Above 2000")           
        print("Paid extra 10% charge =>",(u*12)/10)