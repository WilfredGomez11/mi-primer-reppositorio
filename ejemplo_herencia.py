# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        return f"El animal {self.nombre} emite un sonido"

# Definición de la subclase Perro que hereda de Animal
class Perro(Animal):
    def emitir_sonido(self):
        return f"El perro {self.nombre} hace guau"

# Definición de la subclase Gato que hereda de Animal
class Gato(Animal):
    def emitir_sonido(self):
        return f"El gato {self.nombre} hace miau"

# Creación de objetos
perro = Perro("Bobby")
gato = Gato("Whiskers")

# Llamadas a métodos
print(perro.emitir_sonido()) # Salida: El perro Bobby hace guau
print(gato.emitir_sonido())   # Salida: El gato Whiskers hace miau