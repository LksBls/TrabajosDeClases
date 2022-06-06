"""
Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa "12345"
se debe imprimir "5"

"""

n = int(input("Ingrese un número entero:"))

cont = 0

if n < 0:
    n = n*(-1)
while n != 0:
 n = n // 10
 cont +=1
     
print("El número ingresado tiene: ",cont,"digitos")