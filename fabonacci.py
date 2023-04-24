a=0
b=1
i=1
n=int(input("Enter the  term :"))
for i in range(n+1):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
