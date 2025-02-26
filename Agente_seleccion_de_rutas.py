import heapq
import time

class AgenteSeleccionRutas:
    def __init__(self, entorno, inicio, meta):
        self.entorno = entorno
        self.inicio = inicio
        self.meta = meta
        self.filas = len(entorno)
        self.columnas = len(entorno[0])
        self.movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    
    def calcular_mejor_ruta(self):
        heap = [(-self.entorno[self.inicio[0]][self.inicio[1]], self.inicio, [self.inicio])]
        visitados = set()
        
        while heap:
            utilidad, (x, y), ruta = heapq.heappop(heap)
            if (x, y) == self.meta:
                return ruta, -utilidad
            
            visitados.add((x, y))
            
            for dx, dy in self.movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.filas and 0 <= ny < self.columnas and (nx, ny) not in visitados:
                    nueva_utilidad = utilidad - self.entorno[nx][ny]
                    heapq.heappush(heap, (nueva_utilidad, (nx, ny), ruta + [(nx, ny)]))
        return [], 0