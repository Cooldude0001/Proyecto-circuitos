# Importaciones
from .Componente import Componente

# Definición de la clase Inductor
class Inductor(Componente):
    """Clase que representa un inductor electrico.

    Inicialice la clase Inductor con parametros de valor y nombre:

    param valor: representa el valor de la inducatancia de la instancia.
    Param nombre: representa el nombre de la instancia.
    """
    def __init__(self, valor, nombre):
        super().__init__(valor, nombre)
    
    # Método para entregar una representación de la instancia en str
    def __str__(self):
        return f"Inductor: {self._nombre} con valor de {self._valor}H Henrios."