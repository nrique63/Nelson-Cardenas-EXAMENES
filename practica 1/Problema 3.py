lista = ["Enrique", 2500, 18, "UNMSM", 6250125, True]
sueldo = 2500
canhijos = 0
lista.append(0)
bono_familiar = 8*2500/100


if canhijos > 0:
  lista.append(bono_familiar)
  print("Obtiene el bono familiar el cual es de {}".format(bono_familiar))
  print(lista)
if canhijos == 0:
  print("No cumple para obtener el bono familiar")
  print(lista)