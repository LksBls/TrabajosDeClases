"""
Escribir una función para ingresar desde el teclado una serie de números entre A
y B y guardarlos en una lista. En caso de ingresar un valor fuera de rango la fun-
ción mostrará un mensaje de error y solicitará un nuevo número. Para finalizar la
carga se deberá ingresar -1. La función recibe como parámetros los valores de A
y B, y devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como
valor de retorno. Tener en cuenta que A puede ser mayor, menor o igual a B.

"""

def serieDeNumeros(a,b):
    
    minimo = 0
    maximo = 0
    suma = 0
    
    if a > b:
        maximo = a
        minimo = b
    else:
        maximo = b
        minimo = a
    
    respuesta = []
    
    n = int(input("Ingrese un numero o -1 para finalizar: "))
    
    while n != -1:
        if n > maximo or n < minimo:
            print("ERROR - El numero debe estar entre ",a," y ",b)
        else:
            respuesta.append(n)
        n = int(input("Ingrese un numero o -1 para finalizar: "))
            
    return respuesta

n1 = int(input("Ingrese el número A: "))
n2 = int(input("Ingrese el número B: "))
print("Escribir numeros entre A y B")
lista = serieDeNumeros(n1,n2)
print(lista)



            
            
        