from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.recolher import Recolher
from sae.agente.agente import Agente

"""
Esta classe (AgenteReactivo) representa um agente reactivo simples, baseado numa arquitectura puramente reactiva.

    Este agente é construído com base num controlo reactivo, onde cada percepção do ambiente é imediatamente
    transformada numa acção, sem qualquer memória ou planeamento. Neste caso, o comportamento reativo 
    utilizado é o 'Explorar', que executa movimentos aleatórios no ambiente com uma certa probabilidade.

    A arquitectura do agente segue o ciclo clássico de execução:
        1. Percepcionar o ambiente.
        2. Processar a percepção usando o controlo reactivo.
        3. Activar a acção resultante.
        
Uma arquitetura de agentes reativos define um ciclo perceção–reação–ação  
"""

class AgenteReactivo(Agente):

    # Inicializa o agente reactivo com um comportamento de exploração baseado em probabilidade.
    # O comportamento 'Explorar' é passado ao controlo reactivo e define a tendência do agente
    # para se mover aleatoriamente pelo ambiente.
    def __init__(self):

        super().__init__()

        self.__controlo_react = ControloReact( Recolher() )

    # Executa o ciclo de vida do agente reativo:
    #     1. Percebe o ambiente através dos sensores.
    #     2. Usa o controlo reativo para decidir a ação a tomar com base na perceção.
    #     3. Executa a ação escolhida através dos atuadores.
    def executar(self):

        accao = self.__controlo_react.processar(self._percepcionar())

        self._actuar(accao)

