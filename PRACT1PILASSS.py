class PilaNueva:
    def _init_(self, capacidad):
        self.items = []
        self.capacidad = capacidad
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.items.append(elemento)
            self.tope += 1
            print(f"Insertado {elemento}. Pila: {self.items}")
        else:
            print(f"Error: Desbordamiento. No se puede insertar {elemento}")

    def eliminar(self):
        if self.tope > 0:
            elemento = self.items.pop()
            self.tope -= 1
            print(f"Eliminado {elemento}. Pila: {self.items}")
            return elemento
        else:
            print("Error: Subdesbordamiento. La pila está vacía")
            return None

pila = PilaNueva(8)

print("a. Insertar X")
pila.insertar('X')

print("\nb. Insertar Y")
pila.insertar('Y')

print("\nc. Eliminar Z")
pila.eliminar()

print("\nd. Eliminar T")
pila.eliminar()

print("\ne. Eliminar U")
pila.eliminar()

print("\nf. Insertar V")
pila.insertar('V')

print("\ng. Insertar W")
pila.insertar('W')

print("\nh. Eliminar P")
pila.eliminar()

print("\ni. Insertar R")
pila.insertar('R')

print(f"\nEstado final de la pila: {pila.items}")
print(f"Cantidad de elementos en la pila: {pila.tope}")