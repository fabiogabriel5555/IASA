from abc import ABC

"""
    Classe abstrata 'ModeloPDM', que define a interface para um modelo de Processo de Decisão de Markov (PDM).

    Esta classe fornece a estrutura fundamental para modelar um PDM.
    
    Um PDM é composto por um conjunto de estados ( S ), ações possíveis em cada estado ( A(s) ), probabilidades 
    de transição ( T(s, a, s') ), recompensas associadas ( R(s, a, s') ), e estados sucessores ( suc(s, a) ). 
    
    A classe é projetada para suportar a tomada de decisão sequencial em ambientes com incerteza, permitindo o cálculo 
    de utilidades e políticas ótimas via algoritmos como iteração de valor.

    Como uma classe abstrata, 'ModeloPDM' define métodos que devem ser implementados por subclasses concretas, como 
    'ModeloAmbiente7x1', que modelam ambientes específicos. 
"""

class ModeloPDM(ABC):

    # Retorna o conjunto de estados do modelo.
    def S(self):
        """ABSTRACTED METHOD """

    # Retorna o conjunto de ações possíveis em um dado estado.
    def A(self, s):
        """ABSTRACTED METHOD """

    # Retorna a probabilidade de transição entre estados.
    def T(self, s, a, sn):
        """ABSTRACTED METHOD """

    # Retorna a recompensa associada a uma transição.
    def R(self, s, a, sn):
        """ABSTRACTED METHOD """

    # Retorna o conjunto de estados sucessores para uma ação em um estado.
    def suc(self, s, a):
        """ABSTRACTED METHOD """