# Importaciones
from ..Components.Componente import Componente
from ..Components.Resistencia import Resistencia
from ..Components.Fuente import Fuente

# Definición de la clase circuito
class Circuito:
    """Clase utilizada para modelar circuitos.
    
    Inicialice la clase Circuito con los parametros.
    """
    def __init__(self, nombre: str, componentes: list[Componente], tipo: str):
        self.nombre = nombre
        self.componentes = componentes
        self.tipo = tipo
        self.corriente = self.obtener_corriente()

    def obtener_corriente(self):
        for compo in self.componentes:
            if type(compo) == Fuente:
                voltaje = compo.obtener_valor()
            if type(compo) == Resistencia:
                resistencia = compo.obtener_valor ()
        
        return voltaje / resistencia
    
    def __str__(self):
        string = f"""Circuito "{self.nombre}" en {self.tipo} compuesto por:"""
       
        # Ciclo para ordenar representacion_str con los componentes
        for componente in self.componentes:
            txt= f"""
{componente.obtener_nombre()}: {componente.obtener_valor()}"""
            string += txt

        return string