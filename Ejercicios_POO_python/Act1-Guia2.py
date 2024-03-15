class Persona:
    def __init__(self, name): 
        self.nombre = name
    
    def imprimir(self):
        print("Su nombre es:" , self.nombre)

persona1 = Persona('Nicolas')
persona2 = Persona('Matias')
persona1.imprimir()
persona2.imprimir()