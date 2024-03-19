class Persona:
    def __init__(self, nombre=None, edad=0):
        self.nombre = nombre
        self.edad = edad
    
    def ingresar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

class Empleado(Persona):
    def __init__(self, nombre=None, edad=0, sueldo=0):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def ingresar_datos_empleado(self):
        self.sueldo = int(input("Ingresar sueldo de la persona: "))

    def sueldo_empleado(self):
        super().imprimir_datos()
        print("Sueldo:", self.sueldo)
        if self.sueldo > 3000:
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")

            
persona1 = Persona()
persona1.ingresar_datos()
persona1.imprimir_datos()

empleado1 = Empleado()
empleado1.ingresar_datos()
empleado1.ingresar_datos_empleado()
empleado1.sueldo_empleado()
