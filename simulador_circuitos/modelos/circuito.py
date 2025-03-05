import numpy as np
from .componente import Resistencia, Inductancia, Capacitancia


class Circuito:
    def __init__(self, tipo, configuracion, fuente, componentes):
        """
        Inicializa un circuito eléctrico con sus componentes y configuración.

        Parámetros:
        - tipo: Tipo de circuito ('RC', 'RL', 'RLC').
        - configuracion: Configuración del circuito ('serie' o 'paralelo').
        - fuente: Objeto de la clase FuenteDC que representa la fuente de voltaje.
        - componentes: Lista de objetos de la clase Componente.
        """
        self.tipo = tipo
        self.configuracion = configuracion
        self.fuente = fuente
        self.componentes = componentes

    def calcular_respuesta(self, tiempo):
        """
        Calcula la respuesta del circuito en función del tiempo.

        Parámetros:
        - tiempo: Array de valores de tiempo para los cuales se calculará la respuesta.

        Retorna:
        - v_c: Voltaje en el capacitor.
        - i_c: Corriente en el capacitor.
        - i_l: Corriente en la inductancia.
        - i_r: Corriente en la resistencia.
        - v_r: Voltaje en la resistencia.
        - v_l: Voltaje en la inductancia.
        """
        resistencia_total = sum(
            c.valor for c in self.componentes if isinstance(c, Resistencia)
        )
        inductancia_total = sum(
            c.valor for c in self.componentes if isinstance(c, Inductancia)
        )
        capacitancia_total = sum(
            c.valor for c in self.componentes if isinstance(c, Capacitancia)
        )

        # Inicialización de señales
        v_c = np.zeros_like(tiempo)
        i_c = np.zeros_like(tiempo)
        i_l = np.zeros_like(tiempo)
        i_r = np.zeros_like(tiempo)
        v_r = np.zeros_like(tiempo)
        v_l = np.zeros_like(tiempo)

        # Cálculos para circuitos en SERIE
        if self.configuracion == 'serie':
            if self.tipo == 'RC':
                tau = resistencia_total * capacitancia_total
                v_c = self.fuente.voltaje * (1 - np.exp(-tiempo / tau))
                i_r = (self.fuente.voltaje / resistencia_total) * np.exp(-tiempo / tau)
                i_c = i_r
                v_r = i_r * resistencia_total

            elif self.tipo == 'RL':
                tau = inductancia_total / resistencia_total
                i_l = (self.fuente.voltaje / resistencia_total) * (1 - np.exp(-tiempo / tau))
                i_r = i_l
                v_r = i_r * resistencia_total
                v_l = self.fuente.voltaje - v_r

            elif self.tipo == 'RLC':
                frecuencia_natural = 1 / np.sqrt(inductancia_total * capacitancia_total)
                coeficiente_amortiguamiento = resistencia_total / (2 * inductancia_total)

                if coeficiente_amortiguamiento**2 < frecuencia_natural**2:
                    frecuencia_amortiguada = np.sqrt(
                        frecuencia_natural**2 - coeficiente_amortiguamiento**2
                    )
                    amplitud = self.fuente.voltaje / (inductancia_total * frecuencia_amortiguada)
                    i_r = amplitud * np.exp(-coeficiente_amortiguamiento * tiempo) * np.sin(
                        frecuencia_amortiguada * tiempo
                    )
                else:
                    constante_decaimiento_1 = (
                        -coeficiente_amortiguamiento
                        + np.sqrt(coeficiente_amortiguamiento**2 - frecuencia_natural**2)
                    )
                    constante_decaimiento_2 = (
                        -coeficiente_amortiguamiento
                        - np.sqrt(coeficiente_amortiguamiento**2 - frecuencia_natural**2)
                    )
                    amplitud_1 = self.fuente.voltaje / (
                        2 * inductancia_total * np.sqrt(
                            coeficiente_amortiguamiento**2 - frecuencia_natural**2
                        )
                    )
                    amplitud_2 = -amplitud_1
                    i_r = (
                        amplitud_1 * np.exp(constante_decaimiento_1 * tiempo)
                        + amplitud_2 * np.exp(constante_decaimiento_2 * tiempo)
                    )

                v_r = i_r * resistencia_total
                i_l = np.cumsum(i_r) * (tiempo[1] - tiempo[0])
                v_l = inductancia_total * np.gradient(i_l, tiempo)
                q_c = np.cumsum(i_r) * (tiempo[1] - tiempo[0])
                v_c = q_c / capacitancia_total

        # Cálculos para circuitos en PARALELO
        elif self.configuracion == 'paralelo':
            v_c = self.fuente.voltaje * np.ones_like(tiempo)
            v_r = self.fuente.voltaje * np.ones_like(tiempo)
            v_l = self.fuente.voltaje * np.ones_like(tiempo) if self.tipo in ['RL', 'RLC'] else np.zeros_like(tiempo)

            if self.tipo == 'RC':
                i_r = v_r / resistencia_total
                i_c = capacitancia_total * np.gradient(v_c, tiempo)

            elif self.tipo == 'RL':
                i_r = v_r / resistencia_total
                i_l = (1 / inductancia_total) * np.cumsum(v_l) * (tiempo[1] - tiempo[0])

            elif self.tipo == 'RLC':
                i_r = v_r / resistencia_total
                i_l = (1 / inductancia_total) * np.cumsum(v_l) * (tiempo[1] - tiempo[0])
                i_c = capacitancia_total * np.gradient(v_c, tiempo)

        return v_c, i_c, i_l, i_r, v_r, v_l