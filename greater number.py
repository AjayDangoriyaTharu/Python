#Program to find largest out of three numbers

def compare():
  a = eval(input("Enter the 1st number :"))
  b = eval(input("Enter the 2nd number :"))
  c = eval(input("Enter the 3rd number :"))
  if (a > b) & (a > c) :
    print("Greater number is :",a)
  elif (b > a) & (b > c) :
      print("Greater number is :",b)
  else :
        print("Greater number is :",c)
compare()
