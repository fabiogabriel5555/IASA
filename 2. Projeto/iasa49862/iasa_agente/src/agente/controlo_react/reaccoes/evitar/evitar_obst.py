from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

"""
    Esta classe representa o comportamento composto 'EvitarObst' de um agente reativo.
    
    Este comportamento coordena sub-comportamentos direcionais (`EvitarDir`) para evitar obstáculos
    detectados em diferentes direções, utilizando uma hierarquia fixa de subsunção.

    Herda da classe `Hierarquia`, que implementa a lógica de seleção de ação baseada em uma 
    organização hierárquica de prioridade fixa entre os sub-comportamentos. 
    
    Faz parte da arquitetura do 'Agente Prospector', cujo objetivo inclui evitar obstáculos em um 
    espaço discreto com direções NORTE, SUL, ESTE e OESTE.
    
    Cada sub-comportamento `EvitarDir` é responsável por uma direção específica, e a hierarquia 
    determina a ação a ser executada com base na prioridade estabelecida.
"""

class EvitarObst(Hierarquia):

    """
        Este  construtor cria uma lista de sub-comportamentos `EvitarDir`, um para cada direção
        definida no enumerado `Direccao` (NORTE, SUL, ESTE, OESTE), e passa essa lista para o
        construtor da classe mãe `Hierarquia`.

        Este construtor utiliza list comprehension (forma eficiente de criar listas em uma linha)
        para instanciar os sub-comportamentos e delega a inicialização da lógica de hierarquia
        à classe mãe Hierarquia.
    """
    def __init__(self):
        super().__init__(
            [
                EvitarDir(direccao) for direccao in Direccao
            ]
        )



