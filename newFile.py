start=int(input("Enter Start of range"))
end=int(input("Enter end of range"))

def checkPrime(number):
    factor=0
    for i in range(1,number+1,1):
        if(number%i==0):
            factor=factor+1
    if(factor<=2):
        return True
    else:
        return False
    
for i in range(start,end+1,1):
    if(checkPrime(i)):
        print(i)
    else:
        continue