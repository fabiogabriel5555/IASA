from abc import ABC, abstractmethod

# Estimulo: Define informação activadora de uma reacção
"""
Esta classe (Estimulo) é uma classe abstrata que representa a detecção de um padrão 
específico numa perceção. A sua função é:

    Analisar a perceção do ambiente.

    Determinar se há algum estímulo relevante 

    Ser usada como parte do mecanismo estímulo–resposta.
"""

class Estimulo(ABC):

    # Metodo abstrato que define a interface para a deteção de um estímulo numa perceção.
    # Este metodo deve ser implementado pelas subclasses
    @abstractmethod
    def detectar(self, percepcao):
        """Detectar estimula numa percepção"""
