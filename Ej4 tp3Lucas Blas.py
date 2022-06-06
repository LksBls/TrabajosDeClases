
#Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe
#recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.
#• Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#• Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#• Se debe recuperar cuando al menos una de las dos notas es menor a 4.


nota1 = int(input("Ingrese la nota del primer parcial:"))
nota2 = int(input("Ingrese la nota del segundo parcial:"))

promedio = (nota1+nota2)//2
    
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("ERROR - La nota no puede ser menor a 0 o mayor a 10")

elif promedio >= 7:
    print("El alumno promociona")

elif promedio >= 4:
    print("El alumno aprueba")
    
else:
    print("El alumno debe recuperar")