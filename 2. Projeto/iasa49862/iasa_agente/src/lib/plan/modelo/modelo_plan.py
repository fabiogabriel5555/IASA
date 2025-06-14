from abc import ABC,abstractmethod


class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        """ABSTRACT METHOD"""

    @abstractmethod
    def obter_estados(self):
        """ABSTRACT METHOD"""

    @abstractmethod
    def obter_operadores(self):
        """ABSTRACT METHOD"""