from collections import deque
import time

class AgenteNavegacion:
    def __init__(self, laberinto, inicio, meta):
        self.laberinto = laberinto
        self.inicio = inicio
        self.meta = meta
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    
    def buscar_ruta(self):
        cola = deque([(self.inicio, [self.inicio])])
        visitados = set()
        visitados.add(self.inicio)
        
        while cola:
            (x, y), ruta = cola.popleft()
            if (x, y) == self.meta:
                return ruta
            
            for dx, dy in self.movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.filas and 0 <= ny < self.columnas and self.laberinto[nx][ny] == 0 and (nx, ny) not in visitados:
                    cola.append(((nx, ny), ruta + [(nx, ny)]))
                    visitados.add((nx, ny))
        return []
    
    def navegar(self):
        ruta = self.buscar_ruta()
        if ruta:
            for paso in ruta:
                print(f"🚀 Agente en {paso}")
                time.sleep(0.5)
            print("🎯 Meta alcanzada!")
        else:
            print("❌ No se encontró una ruta a la meta.")

# Definir el laberinto (0 = camino, 1 = pared)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)

# Crear el agente y ejecutarlo
agente = AgenteNavegacion(laberinto, inicio, meta)
agente.navegar()