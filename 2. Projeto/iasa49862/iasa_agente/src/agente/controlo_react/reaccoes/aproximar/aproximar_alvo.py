from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae.ambiente.direccao import Direccao

"""
    Esta Classe representa o comportamento composto 'AproximarAlvo' de um agente reativo.
    
    Este comportamento coordena sub-comportamentos direcionais (AproximarDir) para aproximar 
    o agente do alvo mais próximo detectado, utilizando um mecanismo de seleção de ação baseado 
    em prioridade.

    O comportamento é parte da arquitetura do 'Agente Prospector', cujo objetivo é recolher alvos
    em um espaço discreto com obstáculos, movendo-se nas direções NORTE, SUL, ESTE e OESTE.
    Cada sub-comportamento direcional gera uma prioridade baseada na proximidade do alvo detectado,
    e a ação com maior prioridade é selecionada para execução.

    Herda da classe 'Prioridade', que implementa a lógica de seleção de ação por prioridade.
"""

class AproximarAlvo(Prioridade):
    """
        Este construtor inicia uma lista de sub-comportamentos 'AproximarDir', um para cada direção definida no enumerado
        'Direccao' (NORTE, SUL, ESTE, OESTE), e passa essa lista para o construtor da classe base 'Prioridade'.
    """
    def __init__(self):
        (super().__init__(
            [
                AproximarDir(direccao) for direccao in Direccao
            ]
        ))