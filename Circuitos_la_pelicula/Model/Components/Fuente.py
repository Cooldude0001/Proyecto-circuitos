# Importaciones
from .Componente import Componente

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
        self._tipo = tipo
    
    # Funciones para cambiar atributos de la instancia  
    def cambiar_tipo(self, nuevo_tipo: str):
        """Funcion que cambia el atributo tipo, ingrese en mayúsculas el 
        dominio AC o DC.
        """
        if nuevo_tipo not in ["DC", "AC"]:
            print ("Debe ingresar un dominio válido.")
            return None
        
        self._tipo = nuevo_tipo
           
    # Funciones para obtener atributos de la instancia
    def obtener_tipo(self):
        """Funcion que retorna el tipo de dominio de corriente de la 
        instancia.
        """
        return self._tipo
    
    # Método para entregar una representación de la instancia en str
    def __str__(self):
        return f"Fuente {self._nombre} de {self._valor} de tipo {self._tipo}."