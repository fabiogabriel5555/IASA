from abc import ABC, abstractmethod

"""
    Classe abstrata 'Planeador', que define a interface para planeadores em sistemas de planeamento automático.

    Esta classe estabelece o contrato para planeadores que geram planos de ação com base num modelo de planeamento e 
    objetivos. 
    
    Um planeador é responsável por determinar uma sequência de ações ou uma política que permita alcançar os objetivos 
    especificados, sendo aplicável em contextos como procura em espaços de estados ou tomada de decisão sequencial em PDMs 
    
    A classe é projetada para integrar-se com agentes deliberativos e simuladores.

    Como classe abstrata, 'Planeador' define o método abstrato 'planear', que deve ser implementado por subclasses 
    concretas, como 'PlaneadorPEE', para suportar diferentes estratégias de planeamento, incluindo procura informada 
    (e.g., A*) ou algoritmos baseados em PDMs, como iteração de valor. 
"""

class Planeador(ABC):

    # Metodo abstrato para gerar um plano de ação.
    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """ABSTRACT METHOD"""
