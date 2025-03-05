from tkinter import ttk


class VistaCircuito:
    def __init__(self, root, controlador):
        """
        Inicializa la vista del simulador de circuitos.

        Parámetros:
        - root: Ventana principal de la aplicación.
        - controlador: Controlador que maneja la lógica de la aplicación.
        """
        self.root = root
        self.controlador = controlador
        self.configurar_ui()

    def configurar_ui(self):
        """Configura la interfaz de usuario."""
        self.root.title("Simulador de Circuitos")
        self.root.minsize(300, 400)

        # Hacer que las columnas y filas sean responsive
        for i in range(2):
            self.root.columnconfigure(i, weight=1)
        for i in range(9):
            self.root.rowconfigure(i, weight=1)

        # Campos de entrada para los valores de los componentes
        etiqueta_voltaje = ttk.Label(self.root, text="Voltaje de la fuente (V):")
        etiqueta_voltaje.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entrada_voltaje = ttk.Entry(self.root)
        self.entrada_voltaje.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.entrada_voltaje.insert(0, "10")

        etiqueta_resistencia = ttk.Label(self.root, text="Resistencia (Ω):")
        etiqueta_resistencia.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entrada_resistencia = ttk.Entry(self.root)
        self.entrada_resistencia.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.entrada_resistencia.insert(0, "10")

        etiqueta_capacitancia = ttk.Label(self.root, text="Capacitancia (F):")
        etiqueta_capacitancia.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entrada_capacitancia = ttk.Entry(self.root)
        self.entrada_capacitancia.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.entrada_capacitancia.insert(0, "0.01")

        etiqueta_inductancia = ttk.Label(self.root, text="Inductancia (H):")
        etiqueta_inductancia.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entrada_inductancia = ttk.Entry(self.root)
        self.entrada_inductancia.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        self.entrada_inductancia.insert(0, "0.01")

        # Campos de entrada para el rango de tiempo
        etiqueta_tiempo_inicial = ttk.Label(self.root, text="Tiempo inicial (s):")
        etiqueta_tiempo_inicial.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entrada_tiempo_inicial = ttk.Entry(self.root)
        self.entrada_tiempo_inicial.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
        self.entrada_tiempo_inicial.insert(0, "0")

        etiqueta_tiempo_final = ttk.Label(self.root, text="Tiempo final (s):")
        etiqueta_tiempo_final.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entrada_tiempo_final = ttk.Entry(self.root)
        self.entrada_tiempo_final.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        self.entrada_tiempo_final.insert(0, "1")

        # Combobox para seleccionar el tipo de circuito y la configuración
        etiqueta_tipo = ttk.Label(self.root, text="Tipo de circuito:")
        etiqueta_tipo.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.combo_tipo = ttk.Combobox(self.root, values=["RC", "RL", "RLC"])
        self.combo_tipo.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
        self.combo_tipo.current(0)

        etiqueta_configuracion = ttk.Label(self.root, text="Configuración:")
        etiqueta_configuracion.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.combo_configuracion = ttk.Combobox(self.root, values=["serie", "paralelo"])
        self.combo_configuracion.grid(row=7, column=1, padx=10, pady=10, sticky="ew")
        self.combo_configuracion.current(0)

        # Botón para graficar
        boton_graficar = ttk.Button(self.root, text="Graficar", command=self.controlador.graficar_circuito)
        boton_graficar.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="ew")