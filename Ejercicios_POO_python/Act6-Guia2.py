class Familia:
    def atributos(self, nombre_padre, nombre_madre, lista_hijos):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.lista_hijos = lista_hijos

    def __str__(self):
        return f"Padre: {self.nombre_padre}\nMadre: {self.nombre_madre}\nHijos: {(self.lista_hijos)}"


family = Familia()
family.atributos(nombre_padre="Juan", nombre_madre="Marta", lista_hijos=["Martin", "Agustin", "Maria"])
print(family)