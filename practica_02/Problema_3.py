"""3. Escribir un programa para gestionar una billetera electrónica (3 ptos):
Reglas:
-El programa deberá considerar 2 cuentas bancarias para el
constructor: 1 en soles y otra en dólares. Considerar el nombre y
apellido del titular
-Deberá tener un método para transferir entre sus cuentas, pero
para realizar esto debe hacer una conversión de monedas.
-Tendrá otro método para retirar dinero, esto debe actualizar ambas
cuentas y mostrar en pantalla los montos actualizados, a su vez
validar si tiene fondos suficientes o no para el retiro, mostrar un
mensaje que indique no tiene suficientes en caso fuera el caso.
-Instanciar 3 veces los casos de transferencias para ver reflejado el
uso de tus métodos creados. """
class Titular:
    def __init__(self, monto_soles, monto_dolares):
        self.monto_soles = monto_soles
        self.monto_dolares = monto_dolares
    def transf_soles_a_dolares(self):  #cuenta en dolares aumenta, cuenta en soles disminuye
        var_1 = float(input("Cuanto es la cantidad de soles que desea transferir"))
        if var_1 < self.monto_soles:
          self.monto_dolares = self.monto_dolares + var_1*0.27
          self.monto_soles = self.monto_soles - var_1
        else:
          print("Fondos insuficientes")


    def trans_dolares_a_soles(self):  #cuenta en soles aumenta, cuenta en dolares disminuye
        var_2 = float(input("Cuanto es la cantidad de dolares que desea transferir"))
        if var_2 < self.monto_dolares:
          self.monto_soles = self.monto_soles + var_2*3.66
          self.monto_dolares = self.monto_dolares - var_2
        else:
          print("Fondos insuficientes")

    def retirar_dinero(self):
        cuenta_ = input("De que cuenta desea retirar dinero")
        valor_ = int(input("Cuanto desea retirar"))
        if cuenta_ == "dolares":
            self.monto_dolares = self.monto_dolares - valor_
        if cuenta_ == "soles":
            self.monto_soles = self.monto_soles - valor_


nelson_cardenas = Titular(1000, 1000)
nelson_cardenas.transf_soles_a_dolares()
nelson_cardenas.trans_dolares_a_soles()
nelson_cardenas.trans_dolares_a_soles()
nelson_cardenas.retirar_dinero()
print("El dinero actual en la cuenta en dolares es : {}".format(nelson_cardenas.monto_dolares))
print("El dinero actual en la cuenta en soles es : {}".format(nelson_cardenas.monto_soles))

