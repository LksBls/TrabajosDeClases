"""
Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número -1.
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válida una edad entre 0 y 100).
> <
"""

edad = int(input("Ingrese la edad o presione -1 para finalizar:"))

menores = 0
mayores = 0
contMenores = 0
contMayores = 0
edadGeneral = 0
promedioMayores = 0
promedioMenores = 0
grupoMenor = 0
grupoMayor = 0

while edad != -1:
    if edad < -1 or edad > 100:
        print("Edad incorrecta")
    if edad <= 17:
        menores = edad
        contMenores += 1
        edadGeneral = edad + edadGeneral
        grupoMenor = edad
        promedioMenores = grupoMenor / contMenores
    if edad >= 18:
        mayores = edad
        contMayores += 1
        edadGeneral = edad + edadGeneral
        grupoMayor = edad
        promedioMayores = grupoMayor / contMayores
    
    edad = int(input("Ingrese otra edad o presione -1 para finalizar:"))
    
promedio = edadGeneral / (contMenores+contMayores)

print("La cantidad de personas mayores son:",contMayores)
print("La cantidad de personas menores son:",contMenores)
print("El promedio de edad de las personas mayores es:",promedioMayores)
print("El promedio de edad de las personas menores es:",promedioMenores)
print("El promedio de edad general es:",promedio)

