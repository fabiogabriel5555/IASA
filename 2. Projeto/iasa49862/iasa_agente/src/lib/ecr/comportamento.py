from abc import ABC, abstractmethod

"""
Esta Classe (comportamento) é uma classe abstrata que define a estrutura base que todos 
os comportamentos devem seguir. Esta classe:

    Estabelece um contrato: obriga as subclasses a implementarem o método activar(percepcao).

    Garante a modularidade e extensibilidade do sistema, ou seja, podem se criar novos 
    comportamentos desde que sigam a interface.
    
"""

class Comportamento(ABC):


    # Este metodo define a lógica de ativação de um comportamento com base na perceção do ambiente.
    # Ele deve ser implementado por todas as subclasses de Comportamento.
    @abstractmethod
    def activar(self, percepcao):
        """Metodo activar"""


