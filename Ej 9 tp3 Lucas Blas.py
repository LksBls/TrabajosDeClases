"""Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo
básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto
por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del
bruto por cada año de antigüedad. También se le realizan los siguientes descuentos: Jubilación:
11%, Obra Social: 3%, Sindicato: 3%.
Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (‘s’ o
‘c’). Se debe informar: (reemplazar los 9 por los valores que correspondan)
"""

sueldoBasico = float(input("Ingrese el sueldo basico:"))
antiguedad = int(input("Ingrese antiguedad:"))
estadoCivil = input("Ingrese 's' si es soltero o 'c' si es casado:")

s = sueldoBasico * 0.05
c = sueldoBasico * 0.07

if estadoCivil == "s":
    sueldoSoltero = sueldoBasico + s * antiguedad
    jubilacionSoltero = sueldoSoltero * 0.11
    obraSocialSoltero = sueldoSoltero * 0.03
    sindicatoSoltero = sueldoSoltero * 0.03
    print("Estado civil: Soltero")
    print("Sueldo básico:     Antiguedad:     Descuentos:     Importe:")
    print(" ",sueldoBasico,"          ",antiguedad,"                            +",sueldoBasico * antiguedad * 0.05)
    print("                                   Jubilación     -",jubilacionSoltero)
    print("                                   Obra social    -",obraSocialSoltero)
    print("                                   Sindicato      -",sindicatoSoltero)
    print("                                                  -------------")
    print("                                      Sueldo neto: $",sueldoSoltero - (jubilacionSoltero + obraSocialSoltero + sindicatoSoltero))


if estadoCivil == "c":
    sueldoCasado = sueldoBasico + c * antiguedad
    jubilacionCasado = sueldoCasado * 0.11
    obraSocialCasado = sueldoCasado * 0.03
    sindicatoCasado = sueldoCasado * 0.03
    print("Estado civil: Casado")
    print("Sueldo básico:     Antiguedad:     Descuentos:     Importe:")
    print(" ",sueldoBasico,"          ",antiguedad,"                            +",sueldoBasico * antiguedad * 0.07)
    print("                                   Jubilación     -",jubilacionCasado)
    print("                                   Obra social    -",obraSocialCasado)
    print("                                   Sindicato      -",sindicatoCasado)
    print("                                                  -------------")
    print("                                    Sueldo neto: $",sueldoCasado - (jubilacionCasado + obraSocialCasado + sindicatoCasado))

else:
    print("ERROR")
    