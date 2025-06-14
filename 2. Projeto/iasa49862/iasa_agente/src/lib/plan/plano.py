from abc import ABC, abstractmethod

class Plano(ABC):

    @abstractmethod
    def obter_accao(self, estado):
        """Abstract Method"""

    @abstractmethod
    def mostrar(self, vista):
        """Abstract Method"""