def multiply():
    n=int(input("Enter the no of rows :"))
    a=1
    b=1
    for a in range(n):
        for b in range(11):
            c=a*b
            print(b,"*",a,"=",c, end="   ")
        print()
multiply()