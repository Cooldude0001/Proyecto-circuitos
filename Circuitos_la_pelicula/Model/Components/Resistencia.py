# Importaciones
from Componente import Componente

# Definición de la clase Resistencia
class Resistencia(Componente):
    """Clase que representa una resistencia electrica.

    Inicialice la clase Resistencia con parametros de valor y nombre:

    param valor: representa el valor de la resistencia de la instancia.
    Param nombre: representa el nombre de la instancia.
    """ 
    def __init__(self, valor, nombre):
        super().__init__(valor, nombre)

    def cambiar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def cambiar_valor(self, nuevo_valor):
        self._valor = nuevo_valor

    def __str__(self):
        return f"Resistencia: {self._nombre} con valor {self._valor}Ω ohms."
    
pana_1 = Resistencia(300,"R1")
print(pana_1)