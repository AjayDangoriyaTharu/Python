

x= 1
y= 5
def fun():
    print(x)
    name = 'A'
    d = id(name)
    print(type(d))
    print(type(name))
    global y
    y=y+1
    print(y)
fun()
print(y)