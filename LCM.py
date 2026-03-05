a=int(input("enter the a:"))
b=int(input("enter the b:"))
if(a>b):
   greater = a
else:
   greater = b
   while True:
      if(greater%a==0 and greater%b==0):
         lcm=greater
         break
      greater=greater+1
print " LCM = ", lcm
