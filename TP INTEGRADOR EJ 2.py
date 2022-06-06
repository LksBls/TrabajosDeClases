"""
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen
considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10.
Terminada la carga de datos, informar:
Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
><
"""
aprobados = 0
desaprobados = 0
aplazados = 0
porcentajeAplazados = 0

legajo = int(input("Ingrese número de legajo del alumno o ingrese -1 para finalizar:"))
notaFinal = int(input("Ingrese nota de examen final:"))

while legajo != -1:

    if notaFinal < 1 or notaFinal > 10:
        print("ERROR - La nota debe ser entre 1 y 10")
    if notaFinal >= 4:
        aprobados += 1
    if notaFinal <= 3:
        desaprobados += 1
    if notaFinal == 1:
        aplazados += 1
    
        
    legajo = int(input("Ingrese número de legajo del alumno o ingrese -1 para finalizar:"))
    if legajo != -1:
     notaFinal = int(input("Ingrese nota de examen final:"))

totalAlumnos = aprobados + desaprobados
porcentajeAplazados = aplazados * 100 / totalAlumnos
       
print("Cantidad de alumnos que aprobaron el examen:",aprobados)
print("Cantidad de alumnos que desaprobaron el examen:",desaprobados)
print("Porcentaje de alumnos aplazados:",porcentajeAplazados)