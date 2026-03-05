a = int(input("enter the a value"))
r = 0
num = a
while(a>0):
   s=a%10
   r=r+(s*s*s)
   a=a/10
if(num == r):
   print"armstrong number"
else:
   print"not an armstrong number"
