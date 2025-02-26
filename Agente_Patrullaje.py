import random
import time

class Patrullero:
    def __init__(self, ruta):
        self.ruta = ruta  # Lista de posiciones que forman la ruta
        self.posicion = 0  # Índice de la ruta donde está el agente
        self.direccion = 1  # 1 para adelante, -1 para atrás
    
    def detectar_obstaculo(self):
        return random.random() < 0.2  # 20% de probabilidad de encontrar un obstáculo
    
    def cambiar_direccion(self):
        self.direccion = random.choice([-1, 1])
    
    def mover(self):
        if self.detectar_obstaculo():
            print(f"🚧 Obstáculo detectado en {self.ruta[self.posicion]}! Cambiando dirección...")
            self.cambiar_direccion()
        else:
            nueva_posicion = self.posicion + self.direccion
            if 0 <= nueva_posicion < len(self.ruta):
                self.posicion = nueva_posicion
            else:
                print("⚠️ Fin del camino, cambiando dirección...")
                self.cambiar_direccion()
        print(f"🔍 Patrullero en {self.ruta[self.posicion]}")
    
    def patrullar(self, pasos=20):
        for _ in range(pasos):
            self.mover()
            time.sleep(0.5)

# Definir una ruta de patrullaje
ruta_patrullaje = ["Punto A", "Punto B", "Punto C", "Punto D", "Punto E"]

# Crear el agente y ejecutarlo
agente = Patrullero(ruta_patrullaje)
agente.patrullar()

# Definir una ruta de patrullaje
ruta_patrullaje = ["Punto A", "Punto B", "Punto C", "Punto D", "Punto E"]

# Crear el agente y ejecutarlo
agente = Patrullero(ruta_patrullaje)
agente.patrullar()