#Program to calculate simple or compound interest according to user’s choice. 

def condition():
    n = eval(input("Enter the 1 for SI and 2 for CI :"))
    if n==1 :
        def si():
            p=eval(input("Enter the principle :"))
            t=eval(input("Enter the time :"))
            r=eval(input("Enter the rate :"))
            si=p*t*r/100
            print("The simple interest is :",si)
        si()
    elif n==2:
        def ci():
            p=eval(input("Enter the principle :"))
            t=eval(input("Enter the time :"))
            r=eval(input("Enter the rate :"))
            a=p*(1+r/100)**t
            ci=a-p
            print("The value of ci is :",ci)
        ci()
    else:
        print("Invalid Number")
condition()