# Importaciones
from Componente import Componente 

# Definición de la clase Fuente
class Fuente(Componente):
    """Clase que representa una fuente AC o DC.
    
    Initialice la clase Fuente con parametros valor, nombre y tipo.

    param valor: representa el voltaje (valor) de la fuente.
    Param nombre: representa el nombre de la instancia.
    param tipo: representa si la fuente proporciona una corriente AC o DC.
    """
    def __init__(self, valor, nombre, tipo: str):
        super().__init__(valor, nombre)
        self.tipo = tipo