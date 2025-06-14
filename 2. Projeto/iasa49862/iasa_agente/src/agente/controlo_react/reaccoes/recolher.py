from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from agente.controlo_react.reaccoes.explorar.explorar_mem import ExplorarMem
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.hierarquia import Hierarquia

"""
    Esta classe representa o comportamento composto 'Recolher' de um agente reativo.
    
    Este comportamento coordena sub-comportamentos para alcançar o objetivo principal do 
    'Agente Prospector':
        navegar em um espaço discreto, evitar obstáculos e recolher alvos, 
        utilizando uma hierarquia fixa de prioridade.
    
    Os sub-comportamentos incluídos são:
        `AproximarAlvo` (aproximar-se de alvos), 
        `EvitarObst` (evitar obstáculos), 
        `ExplorarMem` (exploração com memória) e
        `Explorar` (exploração aleatória com intensidade específica), 
    organizados em níveis de competência.
    
    Herda da classe `Hierarquia`, que implementa a lógica de seleção de ação baseada em uma 
    organização hierárquica fixa entre os sub-comportamentos. 
"""

class Recolher(Hierarquia):

    """
        Construtor responsável por cria uma lista de sub-comportamentos na seguinte ordem de
        prioridade:
            `AproximarAlvo`,
            `EvitarObst`,
            `ExplorarMem` e
            `Explorar` (com intensidade 0.7),
        e passa essa lista para o construtor da classe base `Hierarquia`.

        A ordem reflete a hierarquia fixa de competência, onde aproximar alvos tem maior
        prioridade, seguido por evitar obstáculos e exploração.
    """
    def __init__(self):
        super().__init__(
            [
                AproximarAlvo(), EvitarObst(), ExplorarMem(), Explorar(0.7)
            ]
        )