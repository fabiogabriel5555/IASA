from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae import Simulador
from sae.agente.agente import Agente

"""
    Classe 'AgenteDelib', derivada de 'Agente', que implementa um agente com uma arquitetura deliberativa para 
    tomada de decisões baseada em planeamento.

    Esta classe coordena o ciclo de tomada de decisão de um agente autónomo, integrando a assimilação de percepções, a 
    deliberação sobre objetivos, o planeamento de ações e a execução de movimentos. Utiliza um controle deliberativo 
    (`ControloDelib`) para gerenciar o processo, apoiado por um planeador (`PlaneadorPEE`) que gera planos otimizados 
    usando algoritmos de procura, como `ProcuraCustoUnif`.
"""

class AgenteDelib(Agente):

    # Inicializa uma instância do agente deliberativo com um controle deliberativo e um planeador.
    def __init__(self):

        # Chama o construtor da classe base `Agente`.
        super().__init__()

        # Cria uma nova instância de `PlaneadorPEE`, que será usada para gerar planos de ação com base no modelo do
        # mundo e nos objetivos.
        planeador = PlaneadorPEE()

        # Cria uma nova instância de `ControloDelib`, passando o planeador, e armazena-a no atributo privado
        # `__controlo_delib`, que coordenará o ciclo deliberativo do agente.
        self.__controlo_delib = ControloDelib(planeador)


    # Executa o ciclo de vida do agente deliberativo.
    #
    # Este mEtodo implementa o ciclo de tomada de decisão, obtendo uma percepção do ambiente, processando-a para gerar
    # uma ação, exibindo o estado atual na interface visual e executando a ação. Ele reflete o processo cíclico de
    # tomada de decisão.
    def executar(self):

        # Obtém a percepção atual do ambiente chamando o mEtodo `_percepcionar`, que retorna informações sobre a
        # posição do agente e os elementos do ambiente.
        percepcao = self._percepcionar()

        # Processa a percepção usando o metodo `processar` do controle deliberativo, que atualiza o modelo do mundo,
        # delibera sobre objetivos, planeia ações e retorna a próxima ação a ser executada.
        accao = self.__controlo_delib.processar(percepcao)

        # Exibe o estado atual do controle deliberativo (modelo do mundo, plano e objetivos) na interface visual,
        # chamando o metodo `mostrar` do controle deliberativo e passando a interface `vista` do agente.
        self.__controlo_delib.mostrar(self.vista)

        # Executa a ação retornada chamando o metodo `_actuar`, que ativa os atuadores do agente para realizar o
        # movimento ou interação no ambiente.
        self._actuar(accao)

