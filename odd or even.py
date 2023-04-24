#Program to check the given no. is even or odd.

def odd_or_even():
    c = eval(input("Enter the number :"))
    if c % 2 == 0:
        print("The  number is even :",c)
    else:
        print("The  number is odd :",c)
odd_or_even()