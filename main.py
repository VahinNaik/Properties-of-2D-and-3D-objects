import math 
print("cube:1 | sphere:2 | cylinder:3 | torus:4 | rectanguler prizem:5 |" )  
print("_______________________________")
s = int(input('input shape: '))
if s==1:
  e = float(input("what is the edege legnth: "))
  print(e)
  SA = (pow(e,2)*6)
  print("_______________________________")
  print("Surface area of Cube: ")
  print(SA)
  Vol = pow(e,3)
  print("_______________________________")
  print("volume of Cube: ")
  print(Vol)
elif s==2:
  r = float(input("what is the radius: "))
  SV = (1.33*math.pi*pow(r,3))
  print("_______________________________")
  print("Volume of sphere: ")
  print(SV)
  SA = (4*math.pi*pow(r,2))
  print("_______________________________")
  print("Surface area of sphere: ")
  print(SA)
elif s==3:
  r = float(input("what is radius: "))
  h = float(input("what is height: "))
  SA_1 = float(2*math.pi*(r)*(h))
  SA_2 = float(2*math.pi*pow(r,2))
  SA = (SA_1)+(SA_2)
  print("_______________________________")
  print("Surface Area of cylinder is: ")
  print(SA)
  print("_______________________________")
  print("Volume of cylinder is: ")
  Vol = (math.pi*pow(r,2)*h)
  print(Vol)
  cir = (math.pi*pow(r,2))
  print("_______________________________")
  print("Area of circle is: ")
  print(cir)
  rect = (2*math.pi*r*h)
  print("_______________________________")
  print("Area of rectangle is: ")
  print(rect)
elif s==4:
  r = float(input("what is inside radius: ")) 
  R = float(input("what is outside radius: "))
  SA = (4*pow(math.pi,2)*R*r)
  print("_______________________________")
  print("Surface Area of torus is: ")
  print(SA)
  Vol = (2*pow(math.pi,2)*R*pow(r,2))
  print("_______________________________")
  print("Volume of torus is: ")
  print(Vol)
elif s==5:
  L = float(input("what is legnth: ")) 
  W = float(input("what is width: ")) 
  H = float(input("what is height: ")) 
  SA = (2*(W*L+H*L+H*W))
  print("_______________________________")
  print("Surface Area of rectanguler pirzem is: ")
  print(SA)
  Vol = (L*W*H)
  print("_______________________________")
  print(" Volume of rectanguler pirzem is: ")
  print(Vol)
  B_1 = (H*W)
  print("_______________________________")
  print(" Area of base 1 on rectanguler pirzem is: ")
  print(B_1)
  B_2 = (W*L)
  print("_______________________________")
  print(" Area of base 2 on rectanguler pirzem is: ")
  print(B_2)