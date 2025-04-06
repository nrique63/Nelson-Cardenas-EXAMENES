nombre = "Enrique Cardenas"
salario = 2500
edad = 18
compania = "UNMSM"
print(type(nombre))
print(type(salario))
print(type(edad))
print(type(compania))
stedad = str(edad)
if edad > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
if edad < 30:
    print("Usted tiene un bono del 5% en el mes de diciembre")
porcen = 5*salario/100
pot = pow(salario,2)

bonof = pot + porcen
print("El bono final es de {}".format(bonof))
