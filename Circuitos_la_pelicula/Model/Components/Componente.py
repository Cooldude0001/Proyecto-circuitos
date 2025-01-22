#  Definición de la clase Componente
class Componente:
    """Clase que representa un componente electronico generico.

    Inicialice la clase Componente con parametros de valor y nombre:

    param valor: representa el valor en ohms, capacitancia o inductancia de la 
    instancia.
    Param nombre: representa el nombre de la instancia.
    """
    def __init__(self, valor: float, nombre: str):
        self._valor = valor
        self._nombre = nombre

    # Métodos para cambiar atributos de la instancia
    def cambiar_valor(self, nuevo_valor: float):
        """Funcion que cambia el atributo valor por un str cualquiera."""
        self.valor = nuevo_valor

    def cambiar_nombre(self, nuevo_nombre: str):
        """Funcion que cambia el atributo nombre por un str cualquiera."""
        self._nombre = nuevo_nombre

    # Métodos para obtener atributos
    def obtener_valor(self):
        """Funcion que retorna el valor de la instancia."""
        return self._valor
    
    def obtener_nombre(self):
        """Funcion que retorna el nombre de la instancia."""
        return self._nombre