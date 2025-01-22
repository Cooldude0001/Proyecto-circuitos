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

    def cambiar_valor(self, nuevo_valor: float):
        pass

    def cambiar_nombre(self, nuevo_nombre: str):
        pass
