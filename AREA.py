#Program to calculate area of different shapes, such as, triangle, rectangle, circle and square.

def triangle():
    h=eval(input("Enter the of hight of triangle :"))
    b=eval(input("Enter the base of triangle :"))
    a1=(h*b)/2
    print("The area of triangle is :",a1,"cm²")
triangle() 

def rectangle():
    l=eval(input("Enter the of lenght of rectangle :"))
    b2=eval(input("Enter the of base 0f rectangle :"))
    a2=l*b2
    print("The area of rectangle is :",a2,"cm²")
rectangle()

def circle():
    r=eval(input("Enter the of radius of circle :"))
    a3=(22*r*r)/7
    print("The area of circle is :",a3,"cm²")
circle()

def square():
    l2=eval(input("Enter the of length of square :"))
    a4=l2*l2
    print("The area of square is :",a4,"cm²")
square()