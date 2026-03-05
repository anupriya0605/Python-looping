temp = raw_input("enter the temperature:")
hum = raw_input("enter the humidity:")
if(temp == "warm" or temp == "cold") and (hum == "dry" or hum == "humid"):
   print "finding activity"
   if(temp == "warm") and (hum == "dry"):
      print "play basketball"
   elif(temp == "warm") and (hum == "humid"):
      print "play tennis"
   elif(temp == "cold") and (hum == "dry"):
      print "play cricket"
   else:
      print "play swim"
else:
   print "invalid input"
