n1 =int(input("Enter the first no =>"))

n2 =int(input("Enter the first no =>"))

n3 =int(input("Enter the first no =>"))

if(n1==n2 and n1==n3):
    print("All numbers are equal")
elif(n1==n2 or n1==n3):
    print("Two numbers are equal")
elif(n2==n1 or n2==n3):
    print("Two numbers are equal")
elif(n3==n1 or n3==n2):
    print("Two numbers are equal")    
else:
    print("Different numbers")        