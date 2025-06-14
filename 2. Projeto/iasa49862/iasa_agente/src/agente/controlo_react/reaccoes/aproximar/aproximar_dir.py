from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

"""
    Esta classe representa o sub-comportamento direcional 'AproximarDir' de um agente reativo.
    
    Este comportamento é uma reação que detecta um alvo em uma direção específica e gera uma ação
    de movimento nessa direção, como parte do comportamento composto 'AproximarAlvo'.

    Herda da classe 'Reaccao', que define a estrutura básica de uma reação com um estímulo e uma resposta.
    
    O estímulo é defenido para detectar alvos na direção especificada, e a resposta é um movimento
    nessa mesma direção. Utilizado no 'Agente Prospector' para concretizar o sub-objetivo de 
    aproximar-se de um alvo em um espaço discreto com direções NORTE, SUL, ESTE e OESTE.
"""

class AproximarDir(Reaccao):
    """
        Este construtor configura a reação com um estímulo (`EstimuloAlvo`) que detecta a presença
        de um alvo na direção especificada e uma resposta (`RespostaMover`) que gera uma ação de
        movimento nessa direção.
        A inicialização é delegada à superclasse `Reaccao`.
    """
    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))

