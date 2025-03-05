import tkinter as tk
from vistas.vista_circuito import VistaCircuito
from controladores.controlador_circuito import ControladorCircuito


def main():
    root = tk.Tk()
    controlador = ControladorCircuito(None)
    vista = VistaCircuito(root, controlador)
    controlador.vista = vista
    root.mainloop()


if __name__ == "__main__":
    main()