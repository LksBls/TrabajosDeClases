#Banco

#Alumno: Lucas Blas

mil=1000
quinientos=500
cien=100
cincuenta=50
diez=10

dinero=int(input("Inserte la cantidad de dinero que desea extraer:"))

mil1=dinero//mil
resto1=dinero%mil
quinientos1=resto1//quinientos
resto2=resto1%quinientos
cien1=resto2//cien
resto3=resto2%cien
cincuenta1=resto3//cincuenta
resto4=resto3%cincuenta
diez1=resto4//diez


print ("Se extrajo",mil1,"billetes de mil",quinientos1,"billetes de quinientos",cien1,"billetes de cien",cincuenta1,
       "billetes de cincuenta",diez1,"billetes de diez")