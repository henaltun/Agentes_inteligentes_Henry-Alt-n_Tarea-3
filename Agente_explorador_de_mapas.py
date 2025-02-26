import random
import time

class Explorador:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.posicion = (0, 0)  # Inicia en la esquina superior izquierda
        self.visitados = set()
        self.visitados.add(self.posicion)
    
    def obtener_movimientos(self):
        x, y = self.posicion
        movimientos = []
        posibles = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for nx, ny in posibles:
            if 0 <= nx < self.filas and 0 <= ny < self.columnas and (nx, ny) not in self.visitados:
                movimientos.append((nx, ny))
        return movimientos
    
    def mover(self):
        movimientos = self.obtener_movimientos()
        if movimientos:
            self.posicion = random.choice(movimientos)
            self.visitados.add(self.posicion)
        print(f"🗺️ Explorador en {self.posicion}")
    
    def explorar(self, pasos=20):
        for _ in range(pasos):
            self.mover()
            time.sleep(0.5)

# Definir dimensiones del mapa
filas, columnas = 5, 5

# Crear el agente y ejecutarlo
agente = Explorador(filas, columnas)
agente.explorar()
