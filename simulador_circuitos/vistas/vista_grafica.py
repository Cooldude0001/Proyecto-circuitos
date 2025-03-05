import matplotlib.pyplot as plt
from PIL import Image
import os


class VistaGrafica:
    def __init__(self):
        """Inicializa la vista de la gráfica."""
        self.ruta_imagenes = os.path.join(os.path.dirname(__file__), "imagenes")

    def mostrar_grafica(self, tiempo, v_c, i_c, i_l, i_r, v_r, v_l, tipo, configuracion):
        """
        Muestra la gráfica de la respuesta del circuito.

        Parámetros:
        - tiempo: Array de valores de tiempo.
        - v_c: Voltaje en el capacitor.
        - i_c: Corriente en el capacitor.
        - i_l: Corriente en la inductancia.
        - i_r: Corriente en la resistencia.
        - v_r: Voltaje en la resistencia.
        - v_l: Voltaje en la inductancia.
        - tipo: Tipo de circuito ('RC', 'RL', 'RLC').
        - configuracion: Configuración del circuito ('serie' o 'paralelo').
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Graficar la respuesta del circuito
        if tipo in ['RC', 'RLC']:
            ax1.plot(tiempo, v_c, label="Voltaje en el capacitor", linestyle="--")
            ax1.plot(tiempo, i_c, label="Corriente en el capacitor", linestyle="-")
        if tipo in ['RL', 'RLC']:
            ax1.plot(tiempo, i_l, label="Corriente en la bobina", linestyle=":")
            ax1.plot(tiempo, v_l, label="Voltaje en la bobina", linestyle="--")
        ax1.plot(tiempo, i_r, label="Corriente en la resistencia", linestyle="-.")
        ax1.plot(tiempo, v_r, label="Voltaje en la resistencia", linestyle="-.")

        ax1.set_xlabel("Tiempo (s)")
        ax1.set_ylabel("Magnitud")
        ax1.set_title(f"Respuesta del circuito {tipo} ({configuracion})")
        ax1.grid()
        ax1.legend()

        # Mostrar la imagen del circuito
        ruta_imagen = os.path.join(self.ruta_imagenes, f"{tipo}_{configuracion}.png")
        try:
            imagen = Image.open(ruta_imagen)
            ax2.imshow(imagen)
            ax2.axis("off")
            ax2.set_title("Diagrama del circuito")
        except FileNotFoundError:
            ax2.text(0.5, 0.5, "Imagen no encontrada", ha="center", va="center", fontsize=12, color="red")

        # Establecer un tamaño mínimo para la ventana de la gráfica
        manager = plt.get_current_fig_manager()
        manager.window.minsize(800, 400)

        plt.tight_layout()
        plt.show()