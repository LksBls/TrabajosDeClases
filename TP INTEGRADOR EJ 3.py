"""
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:Aplica el precio base a la primera docena
de unidades. Aplica un 10% de descuento a todas las unidades entre 13 y 100. Aplica un 25% de descuento a todas las unidades por
encima de las 100. Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante
sería:100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04

Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y
el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar:
Cantidad de ventas realizadas total. Cantidad de ventas en las que se aplicó un 10% de descuento. Cantidad de ventas en las que
SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.
><
"""

cantidad=int(input("Ingrese la cantidad o finalice con -1:"))
precioBase=int(input("Ingrese la el precio base:"))

contbase=0
cont10=0
cont25=0
ventas=0
ventas10=0
ventas25=0

while cantidad!=-1:

    if cantidad>=1 and cantidad<=12:
     contbase+=1
     ventas=ventas+(precioBase*cantidad)
    if cantidad>=13 and cantidad<=100:
     cont10+=1
     ventas10=ventas10+((precioBase-((precioBase*10)/100))*cantidad)
    if cantidad>100:
     cont25+=1
     ventas25=ventas25+((precioBase-((precioBase*25)/100))*cantidad)
    cantidad=int(input("Ingrese la cantidad o finalice con -1: "))
    if cantidad != -1:
     precioBase=int(input("Ingrese la el precio base:"))

suma=ventas+ventas10+ventas25
print("Las ventas totales realizadas fueron: ",contbase+cont10+cont25)
print("Las ventas con 10% de descuento fueron: ",cont10)
print("La cantidad de ventas con precio base fueron: ",contbase)
print("El valor total de las ventas fue: ",suma)