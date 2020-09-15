import math  
"""NOMBRE: CARMEN REYNA CANDIA SUÑAGUA
   MATERIA: LAB-111"""

a=int(input("Ingrese el coeficiente A: "))
b=int(input("Ingrese el coeficiente B: "))
c=int(input("Ingrese el coeficiente C: "))
delta=b**2-4*a*c

if (delta>0):
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print ("la ecuacion tiene dos soluciones ",x1," y ",x2 )
elif delta==0:
   x1=(-b+math.sqrt(delta))/(2*a)
   print ("la ecuacion tiene una solucion ",x1)
else:
  print ("la ecuacion no tiene solucion real",a,"χ²+",b,"χ+", c)
