"""
BINARIO A DECIMAL

Alumno: Lucas Blas

"""

binario = int(input("Escribir el número binario:"))

binario0=(binario%10)*2**0
binario1=((binario%100)//10)*2**1
binario2=((binario%1000)//100)*2**2
binario3=((binario%10000)//1000)*2**3

suma=binario0+binario1+binario2+binario3

print ("El número decimal es: ",suma)