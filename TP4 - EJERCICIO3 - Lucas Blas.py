"""
Trabajo Práctico 4 - Estructura iterativa:

Ejercicio N°3:
Realizar un programa para ingresar desde el teclado un conjunto de números y
mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
con un valor -1.
"""

n = int(input("Ingrese un número:"))

mayor = n
menor = n

while n != -1:
    
    if n > mayor:
     mayor = n
    if n < menor:
     menor = n
     
    n = int(input("Ingrese otro número, presione -1 para finalizar:"))
    
print("El número mayor es:",mayor,"y el número menor es:",menor)

