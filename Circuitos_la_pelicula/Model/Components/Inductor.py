from Componente import Componente

class Inductor(Componente):
    """Clase que representa un inductor electrico.

    Inicialice la clase Inductor con parametros de valor y nombre:

    param valor: representa el valor de la inducatancia de la instancia.
    Param nombre: representa el nombre de la instancia.
    """
    def __init__(self, valor, nombre):
        super().__init__(valor, nombre)
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor

    def __str__(self):
        return f"Inductor: {self.nombre} con valor de {self.valor}H Henrios."

        