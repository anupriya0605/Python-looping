a=int(input("enter the 4 digit number:"))
sum=0
if(a>=1000 and a<=9999):
   while(a>0):
      sum += a%10
      a=a/10
