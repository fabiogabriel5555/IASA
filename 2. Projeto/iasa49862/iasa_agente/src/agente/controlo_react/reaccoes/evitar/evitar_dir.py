from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst
from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from ecr.reaccao import Reaccao

"""
    Esta classe representa o sub-comportamento direcional 'EvitarDir' de um agente reativo.
    
    Este comportamento é uma reação que detecta um obstáculo em uma direção específica e gera 
    uma ação para evitá-lo, como parte do comportamento composto 'EvitarObst'.

    Herda da classe `Reaccao`, que define a estrutura básica de uma reação com um estímulo e 
    uma resposta.
    
    O estímulo (`EstimuloObst`) verifica a presença de um obstáculo na direção especificada, e a 
    resposta (`RespostaEvitar`) gera uma ação evitar. 
    
    Esta classe é utilizada no 'Agente Prospector' para concretizar o sub-objetivo de evitar 
    obstáculos em um espaço discreto com direções NORTE, SUL, ESTE e OESTE.
"""


class EvitarDir(Reaccao):

    """
        Este construtor configura a reação com um estímulo (`EstimuloObst`) que detecta a presença
        de um obstáculo na direção especificada e uma resposta (`RespostaEvitar`) que gera uma ação
        para evitar o obstáculo.

        A inicialização é delegada à classe mãe `Reaccao` com um estímulo (`EstimuloObst`) e uma
        resposta (`RespostaEvitar`)
    """
    def __init__(self, direccao):
        super().__init__(EstimuloObst(direccao), RespostaEvitar())