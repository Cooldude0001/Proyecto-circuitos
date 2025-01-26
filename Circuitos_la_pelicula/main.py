# # Importaciones
from Model.Components.Resistencia import Resistencia
from Model.Components.Inductor import Inductor
from Model.Components.Condensador import Capacitor
from Model.Components.Fuente import Fuente

from Model.Circuit.Circuito import Circuito

if __name__ == "__main__":
    pana_1 = Resistencia(300, "R1")
    pana_2 = Inductor(650, "H1")
    pana_3 = Capacitor(100, "C1")
    pana_4 = Fuente(5, "Fuente", "DC")

    # Prueba
    circuito = Circuito("Circuito 1", [pana_1, pana_2, pana_3, pana_4], "Serie")
    print(circuito.corriente)