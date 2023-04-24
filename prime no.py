f=0
n=int(input("Enter a positive integer :"))
if (n == 0) or (n == 1):
    f=1
i=2
for i in range(n//2):
    a=n % i
    if a == 0 :
        f=1
        break
if f == 0:
    print("The number is Prime :",n)
else:
    print("The number is not prime :",n)