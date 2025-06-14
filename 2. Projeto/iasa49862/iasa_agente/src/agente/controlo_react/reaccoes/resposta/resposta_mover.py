from lib.ecr.resposta import Resposta
from lib.sae.agente.accao import Accao

"""
    Esta classe representa a resposta 'RespostaMover' de um agente reativo.
    
    Herda da classe `Resposta` e configura uma ação de movimento (`Accao`) em uma direção 
    específica.
    
    A direção da ação é definida no momento da inicialização e passada para a superclasse.

    Esta classe é utilizada no 'Agente Prospector' como parte de sub-comportamentos como 
    'AproximarDir', para concretizar o sub-objetivo de mover o agente em direção a um alvo 
    em um espaço discreto com direções NORTE, SUL, ESTE e OESTE. 
"""

class RespostaMover(Resposta):

    """
        Construtor responsável por criar uma instância de `Accao` com a direção fornecida e a
        passar para o construtor da classe mãe `Resposta`, que configura a ação a ser ativada
        posteriormente.
    """
    def __init__(self, direcao):
        super().__init__( Accao(direcao) )
