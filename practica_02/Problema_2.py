"""Usando el concepto de herencia y encapsulación (para el atributo saldo)
para crear el siguiente programa (3 ptos):
Reglas:
- Crear una clase llamada Persona (Que heredará de la anterior Clase) y
agregar un atributo sueldo a esta clase (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en su cuenta cada vez que use el método transferencia
- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando
una transferencia y con dos personas. """

class Empleado:
    nacionalidad = "peruana"
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        #self.año = 2030
    def sol_nombre(self):
        self.nombre = input("Nombre: ")
    def sol_edad(self):
        self.edad = input("Edad: ")
    def cumpleaños(self):
        self.edad = self.edad + 1
    def aumentosueldo(self):
            self.sueldo = self.sueldo + 3 * self.sueldo / 10
    def edaden2030(self, año = 2040, edad = 60):
        if edad <= self.edad:
            print("No es posible la edad futura")
        else:
            print("En el año 2040, el empleado tendra :{}".format(edad))
class Persona(Empleado):
    sueldo = 4000
    def __init__(self, transferir):
        self.transferir = transferir
    def transferencia(self):



