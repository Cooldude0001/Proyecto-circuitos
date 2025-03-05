class Componente:
    def __init__(self, valor):
        """
        Inicializa un componente con un valor específico.

        Parámetros:
        - valor: Valor del componente (resistencia, capacitancia, inductancia, etc.).
        """
        self.valor = valor


class Resistencia(Componente):
    def __init__(self, valor):
        """
        Inicializa una resistencia con un valor específico.

        Parámetros:
        - valor: Valor de la resistencia en ohmios (Ω).
        """
        super().__init__(valor)


class Inductancia(Componente):
    def __init__(self, valor):
        """
        Inicializa una inductancia con un valor específico.

        Parámetros:
        - valor: Valor de la inductancia en henrios (H).
        """
        super().__init__(valor)


class Capacitancia(Componente):
    def __init__(self, valor):
        """
        Inicializa una capacitancia con un valor específico.

        Parámetros:
        - valor: Valor de la capacitancia en faradios (F).
        """
        super().__init__(valor)