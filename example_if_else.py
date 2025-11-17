sub1 = int(input("Enter your first subject mark :"))

sub2 = int(input("Enter your second subject mark :"))

sub3 = int(input("Enter your third subject mark :"))


percentge=((sub1+sub2+sub3)/300)*100

if(percentge>40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("You are passed ! And your percentage is ",percentge)

else:
    print("you are failled !")