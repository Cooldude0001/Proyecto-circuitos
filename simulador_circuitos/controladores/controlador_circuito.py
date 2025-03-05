from modelos.circuito import Circuito
from modelos.fuente import FuenteDC
from modelos.componente import Resistencia, Inductancia, Capacitancia
from vistas.vista_grafica import VistaGrafica
from tkinter import messagebox
import numpy as np


class ControladorCircuito:
    def __init__(self, vista):
        """
        Inicializa el controlador del simulador de circuitos.

        Parámetros:
        - vista: Vista del simulador de circuitos.
        """
        self.vista = vista
        self.vista_grafica = VistaGrafica()

    def graficar_circuito(self):
        """
        Obtiene los valores ingresados por el usuario, valida las entradas,
        crea el circuito y grafica su respuesta.
        """
        try:
            voltaje = self.validar_entrada(self.vista.entrada_voltaje.get(), "Voltaje")
            resistencia_val = self.validar_entrada(self.vista.entrada_resistencia.get(), "Resistencia")
            capacitancia_val = (
                self.validar_entrada(self.vista.entrada_capacitancia.get(), "Capacitancia")
                if self.vista.combo_tipo.get() in ["RC", "RLC"]
                else 0
            )
            inductancia_val = (
                self.validar_entrada(self.vista.entrada_inductancia.get(), "Inductancia")
                if self.vista.combo_tipo.get() in ["RL", "RLC"]
                else 0
            )
            tiempo_inicial = self.validar_entrada(self.vista.entrada_tiempo_inicial.get(), "Tiempo inicial")
            tiempo_final = self.validar_entrada(self.vista.entrada_tiempo_final.get(), "Tiempo final")

            if tiempo_final <= tiempo_inicial:
                raise ValueError("El tiempo final debe ser mayor que el tiempo inicial.")

            fuente = FuenteDC(voltaje)
            resistencia = Resistencia(resistencia_val)
            capacitancia = Capacitancia(capacitancia_val) if self.vista.combo_tipo.get() in ["RC", "RLC"] else None
            inductancia = Inductancia(inductancia_val) if self.vista.combo_tipo.get() in ["RL", "RLC"] else None

            componentes = [resistencia]
            if capacitancia:
                componentes.append(capacitancia)
            if inductancia:
                componentes.append(inductancia)

            tiempo = np.linspace(tiempo_inicial, tiempo_final, 1000)
            circuito = Circuito(
                self.vista.combo_tipo.get(),
                self.vista.combo_configuracion.get(),
                fuente,
                componentes
            )
            v_c, i_c, i_l, i_r, v_r, v_l = circuito.calcular_respuesta(tiempo)

            self.vista_grafica.mostrar_grafica(
                tiempo, v_c, i_c, i_l, i_r, v_r, v_l,
                self.vista.combo_tipo.get(), self.vista.combo_configuracion.get()
            )

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

    def validar_entrada(self, valor, nombre):
        """
        Valida que una entrada sea un número positivo.

        Parámetros:
        - valor: Valor ingresado por el usuario.
        - nombre: Nombre del campo que se está validando.

        Retorna:
        - El valor convertido a float si es válido.

        Lanza:
        - ValueError si el valor no es un número o no es positivo.
        """
        try:
            valor = float(valor)
            if valor < 0:
                raise ValueError(f"{nombre} debe ser un valor positivo.")
            return valor
        except ValueError:
            raise ValueError(f"{nombre} debe ser un número válido.")