# Finner løsninger til alle andregradslikninger på formen ax^2+bx+c=0
import math

def losninger(a, b, c):
  diskreminant = b**2 - 4*a*c
  if diskreminant < 0:
    return "Likningen har ingen løsning"
  
  Losning1 = round((-b + math.sqrt(diskreminant))/(2*a), 2)
  losning2 = round((-b - math.sqrt(diskreminant))/(2*a), 2)

  if diskreminant == 0:
    return losning1 #et flyttall avrundet til to desimaler
  else: 
    return (losning1, losning2) #en tuppel med to flyttall som begge er avrundet til to desimaler
  
  print(losninger(1, 27, 1))
  

