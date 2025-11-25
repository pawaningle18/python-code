def prime(n):
    if(n<=1):
        return 'not_prime'
    for i in range(2,n):
        if n%i==0:
            return 'not_prime'
        
    return 'prime'
    


    
num=int(input("enter the integer: "))
if prime(num):
    print("the number is :",prime(num))
else:
    print("the number is not prime")
    