class Vehiculo:
    def desplazarse(self):
        pass

class Automovil(Vehiculo):
    def desplazarse(self):
        return "El automóvil se desplaza por la carretera."

class Motocicleta(Vehiculo):
    def desplazarse(self):
        return "La motocicleta se desplaza por la carretera o el camino."

class Bicicleta(Vehiculo):
    def desplazarse(self):
        return "La bicicleta se desplaza por el camino o el carril bici."

# Función para desplazarse con cualquier vehículo
def desplazarse_con_vehiculo(vehiculo):
    print(vehiculo.desplazarse())

# Crear instancias de diferentes tipos de vehículos
mi_automovil = Automovil()
mi_motocicleta = Motocicleta()
mi_bicicleta = Bicicleta()

# Llamar al método desplazarse() para cada vehículo
print(mi_automovil.desplazarse())
print(mi_motocicleta.desplazarse())
print(mi_bicicleta.desplazarse())

# Polimorfismo: Llamar a la función desplazarse_con_vehiculo con diferentes tipos de vehículos
print("Desplazamiento de cualquier vehículo:")
desplazarse_con_vehiculo(mi_automovil)  # Polimorfismo
desplazarse_con_vehiculo(mi_motocicleta)  # Polimorfismo
desplazarse_con_vehiculo(mi_bicicleta)  # Polimorfismo
