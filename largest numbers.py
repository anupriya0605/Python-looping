a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=int(input("enter a third number"))
if(a > b) and (a > c):
   print "greatest number is",a
elif(b > a) and (b > c):
   print "greatest number is",b
else:
   print "greatest number is",c
