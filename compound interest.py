#Program to calculate compound interest.

def ci():
    p=eval(input("Enter the principle :"))
    t=eval(input("Enter the time :"))
    r=eval(input("Enter the rate :"))
    a=p*(1+r/100)**t
    ci=a-p
    print("The value of ci is :",ci)
ci()