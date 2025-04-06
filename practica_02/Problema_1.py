"""1. Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
 - Crear una clase llamada Empleado donde sus atributos deben ser nombre,
edad, sueldo y de nacionalidad peruana, tendrá un método para solicitar su
nombre y otro para solicitar su edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Empleado y usar su nuevo método
aumentoSueldo para incrementar su sueldo en un 30% (mínimo instanciar
la clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).
-Crear un siguiente método que retorne un mensaje donde indique que: “En
el año XXXX tendrá XX años”, el año se ingresará por parámetro y la
edad también, realizar una validación si la edad ingresada por parámetro
es menor a la del constructor indicar que no es posible realizar la
operación (Mostrar por pantalla este valor) """
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


empleado_1 = Empleado("Nelson", 65, 100)
empleado_1.cumpleaños()
empleado_1.aumentosueldo()
empleado_1.aumentosueldo()
empleado_1.edaden2030()

print("La edad despues del cumpleaños del empleado es :{}".format(empleado_1.edad))
print("El nuevo sueldo de la persona 1 es de : {}".format(empleado_1.sueldo))


