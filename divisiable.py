i=1
print("The numbers are:",end= " ")
for i in range(100):
    if i%2==0 and i%3==0 and i%5==0:
        print(i ,end= " " )
    i=i+1