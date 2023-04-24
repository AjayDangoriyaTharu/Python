#Program to calculate simple interest.

def si():
    p=eval(input("Enter the principle :"))
    t=eval(input("Enter the time :"))
    r=eval(input("Enter the rate :"))
    si=p*t*r/100
    print("The simple interest is :",si)
si()