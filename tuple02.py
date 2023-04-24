a=("Ajay",20,30,40,'SandY')
list = list(a)
print(a)
list.append((100,"Hello","Tharu"))
a= tuple(list)
print(a)
list.extend([20,30.49,"Dangoriya"])
a= tuple(list)
print(a)
list.remove("Ajay")
a= tuple(list)
print(a)

print(a.count(20))

list1 = list.copy()
a= tuple(list)
print(a)

list.reverse()
a= tuple(list)
print(a)

list=list1
list1.clear()
a= tuple(list1)
print(a)


b = (2,34,5,145,65,4,0)
list = list(b)
list.sort()
b = tuple(list)
print(b)

list.sort(reverse=True)
b = tuple(list)
print(b)
