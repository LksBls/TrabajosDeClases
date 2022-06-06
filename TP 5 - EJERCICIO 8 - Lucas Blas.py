"""
Una empresa cuenta con N empleados, divididos en tres categorías (1,2 y 3).
Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar
un informe que contenga:

- Importe total de salarios pagados por la empresa.
- Cantidad de empleados que ganan más de $200.000.
- Cantidad de empleados que ganan menos de $50.000, cuya categoría sea 3.
- Legajo del empleado que más gana.
- Sueldo más bajo.
- Importe total de sueldos por cada categoría.
- Salario promedio.

"""

legajo = int(input("Ingrese el legajo del empleado:"))
categoria = int(input("Ingrese la categoria:"))
salario = int(input("Ingrese el salario:"))

salarioTotal = 0
empleadoAlto = 0
empleados3 = 0
sueldoMaximo = 0
legajoMaximo = 0
peorSalario = salario
salarioPromedio = 0
cont = 0

sueldoTotal1 = 0
sueldoTotal2 = 0
sueldoTotal3 = 0

while legajo != -1:
    salarioTotal = salarioTotal + salario
    if salario >= 200000:
     empleadoAlto += 1
    if salario <= 50000 and categoria == 3:
     empleados3 += 1
    if salario > sueldoMaximo:
     sueldoMaximo = salario
     legajoMaximo = legajo
    if salario < peorSalario:
     peorSalario = salario
    if categoria == 1:
     sueldoTotal1 = salario + sueldoTotal1
    if categoria == 2:
     sueldoTotal2 = salario + sueldoTotal2
    if categoria == 3:
     sueldoTotal3 = salario + sueldoTotal3
    cont +=1
     
    legajo = int(input("Ingrese el legajo del empleado o ingrese -1 para finalizar:"))
    if legajo != -1:
     categoria = int(input("Ingrese la categoria:"))
     salario = int(input("Ingrese el salario:"))
     
salarioPromedio = salarioTotal//cont

print("Importe total de salarios:",salarioTotal)
print("Cantidad de empleados que ganan más de $200.000:",empleadoAlto)
print("Cantidad de empleados de categoría 3 que ganan menos de $50.000:",empleados3)
print("Legajo del empleado que más gana:",legajoMaximo)
print("Sueldo más bajo:",peorSalario)
print("Importe total de sueldos de categoria 1:",sueldoTotal1)
print("Importe total de sueldos de categoria 2:",sueldoTotal2)
print("Importe total de sueldos de categoria 3:",sueldoTotal3)
print("Salario promedio:",salarioPromedio)














