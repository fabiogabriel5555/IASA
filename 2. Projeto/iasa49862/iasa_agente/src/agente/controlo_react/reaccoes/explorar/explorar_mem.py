from ecr.resposta import Resposta
from sae.agente.avancar import Avancar

"""
    Esta classe representa o comportamento 'ExplorarMem' de um agente reativo com memória.
    
    Implementa uma lógica de exploração que registra situações (posição e direção) na memória e 
    gera uma ação de avanço apenas quando a situação atual não foi previamente visitada.
    
    Mantém uma memória limitada por um tamanho máximo, removendo as entradas mais antigas quando
    o limite é excedido. A resposta padrão é um avanço (`Avancar`), ativado somente em situações
    novas.

    Utilizada no 'Agente Prospector' para concretizar o sub-objetivo de explorar o ambiente, 
    evitando repetições de posições e direções já exploradas. 
"""

class ExplorarMem:
    """
        Construtor responsável por defenir o tamanho máximo da memória e inicializar uma lista
        vazia para armazenar situações.

        Configura uma resposta padrão com a ação `Avancar`, que será ativada em situações novas.
    """
    def __init__(self, dim_max_mem = 100):

        # Define o tamanho máximo da memória
        self._dim_max_mem = dim_max_mem

        # Inicializa a memória como uma lista vazia
        self._memoria = []

        # Define a resposta padrão como um avanço (instância de `Avancar` encapsulada em `Resposta`)
        self._resposta = Resposta( Avancar() )

    """
        Método responsável por gerar uma ação de exploração com base na percepção atual e na 
        memória de situações.

        Constrói um tuplo `situacao` com a posição e direção atuais do agente. Se essa situação 
        não estiver na memória, adiciona-a à lista `_memoria`, remove a entrada mais antiga se o 
        limite `_dim_max_mem` for excedido, e ativa a resposta de avanço (`Avancar`). 
        
        Se a situação já foi visitada, nenhuma ação é retornada.
    """
    def activar(self, percecpcao):

        # Obtém a situação atual do agente (posição e direção)
        situacao = (percecpcao.posicao, percecpcao.direccao)

        # Verifica se a situação já foi visitada, e se for uma situação nova:
        if situacao not in self._memoria:

            # Adiciona a situação a memória
            self._memoria.append(situacao)

            # Se a memória exceder o tamanho máximo permitido:
            if len(self._memoria) > self._dim_max_mem:

                # Remove a entrada mais antiga
                self._memoria.pop(0)

            # Ativa a resposta de avanço e retorna a ação gerada
            return self._resposta.activar(percecpcao)
