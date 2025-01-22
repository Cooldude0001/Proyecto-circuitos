# Importaciones
from .Componente import Componente

# Definición de la clase Resistencia
class Resistencia(Componente):
    """Clase que representa una resistencia electrica.

    Inicialice la clase Resistencia con parametros de valor y nombre:

    param valor: representa el valor de la resistencia de la instancia.
    Param nombre: representa el nombre de la instancia.
    """ 
    def __init__(self, valor, nombre):
        super().__init__(valor, nombre)
    
    # Método para entregar una representación de la instancia en str
    def __str__(self):
        return f"Resistencia: {self._nombre} con valor {self._valor}Ω ohms."