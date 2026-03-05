a=int(input("enter m1 :"))
b=int(input("enter m2 :"))
c=int(input("enter m3 :"))
d=int(input("enter m4 :"))
e=int(input("enter m5 :"))
avg=(a+b+c+d+e)/5
if(avg>=90):
   print  "o grade"
elif(avg>=80 and avg<=89):
   print "A+ grade"
elif(avg>=70 and avg<=79):
   print "A grade"
elif(avg>=60 and avg<=69):
   print "B+ grade"
elif(avg>=55 and avg<=59):
   print "B grade"
elif(avg>=50 and avg<=54):
   print "c grade"
elif(avg<50):
   print "fail"
