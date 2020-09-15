"""NOMBRE: CARMEN REYNA CANDIA SUÑAGUA
   MATERIA: LAB-111"""

x=int(input("Ingrese un tiempo en SEGUNDOS: "))
h=int(input("Ingrese un tiempo que tardara en realizar la tarea (HORAS): "))
m=int(input("Ingrese un tiempo que tardara en realizar la tarea (MINUTOS): "))
s=int(input("Ingrese un tiempo que tardara en realizar la tarea (SEGUNDOS): "))

z=s+(m*60)+(h*3600)

if (x>=z) :
    print ("finaliza la tarea en el tiempo de 0",h,":",m,":",s)
else:
    print ("no logra finalizar la tarea en un tiempo de  0",h, ":",m,":",s," !!!")
  

