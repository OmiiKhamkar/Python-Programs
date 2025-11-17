n1 = int(input("Enter Your first numbers :"))
n2 = int(input("Enter Your second numbers :"))
n3 = int(input("Enter Your third numbers :"))
n4 = int(input("Enter Your fourth numbers :"))

if(n1>n2 and n1>n3 and n1>n4):
    print("First number is greater",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("Second numnber is greater",n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print("Third number is greater ",n3)    
else:
    print("fourth number is greater",n4)

