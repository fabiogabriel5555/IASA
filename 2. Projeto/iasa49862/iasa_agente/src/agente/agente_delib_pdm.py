from controlo_delib.controlo_delib import ControloDelib
from pdm.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Simulador
from sae.agente.agente import Agente

"""
    Classe 'AgenteDelibPDM', derivada de 'Agente', que implementa um agente com uma arquitetura deliberativa para tomada 
    de decisões baseada em Processos de Decisão de Markov (PDM).

    Esta classe coordena o ciclo de tomada de decisão de um agente autónomo, integrando a assimilação de percepções, 
    a deliberação sobre objetivos, o planeamento de ações com base em políticas ótimas de PDM, e a execução de 
    movimentos. 
    
    Utiliza um controle deliberativo ('ControloDelib') para gerenciar o processo, apoiado por um  planeador 
    ('PlaneadorPDM') que gera planos otimizados usando iteração de valor.
    
    Esta classe é projetada para operar em ambientes com incerteza, onde o agente toma decisões sequenciais para 
    maximizar recompensas. 
"""

class AgenteDelibPDM(Agente):


    # Inicializa uma instância do agente deliberativo PDM com um controle deliberativo e um planeador PDM.
    def __init__(self):

        # Chama o construtor da classe base 'Agente' para inicializar funcionalidades básicas, como
        # percepção e atuação.
        super().__init__()

        # Cria uma instância de 'PlaneadorPDM', que será usada para gerar planos baseados em políticas ótimas de PDM.
        planeador = PlaneadorPDM()

        # Cria uma instância de 'ControloDelib', passando o planeador PDM, e armazena-a como atributo privado para
        # coordenar o ciclo deliberativo, incluindo deliberação, planeamento e execução.
        self.__controlo_delib = ControloDelib(planeador)

    # Executa o ciclo de vida do agente deliberativo PDM.
    #
    # Implementa o ciclo de tomada de decisão, obtendo uma percepção do ambiente, processando-a para gerar
    # uma ação com base na política ótima do PDM, exibindo o estado atual na interface visual, e executando a ação.
    def executar(self):

        # Obtém a percepção atual do ambiente chamando o metodo '_percepcionar', que retorna
        # informações sobre a posição do agente e os elementos do ambiente.
        percepcao = self._percepcionar()

        # Processa a percepção usando o metodo 'processar' do controle deliberativo, que atualiza o modelo do mundo,
        # delibera sobre objetivos, consulta a política ótima do plano PDM, e retorna a próxima ação a ser executada.
        accao = self.__controlo_delib.processar(percepcao)

        # Exibe o estado atual do controle deliberativo (modelo do mundo, plano PDM, e objetivos) na
        # interface visual, chamando o metodo 'mostrar' do controle deliberativo e passando a interface 'vista' do agente.
        self.__controlo_delib.mostrar(self.vista)

        # Executa a ação retornada chamando o metodo '_actuar', que ativa os atuadores do agente para realizar o
        # movimento ou interação no ambiente, conforme a política ótima do PDM.
        self._actuar(accao)

