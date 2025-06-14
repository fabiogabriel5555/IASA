from controlo_delib.modelo.estado_agente import EstadoAgente
from controlo_delib.modelo.operador_mover import OperadorMover
import math

from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento

"""
    Classe 'ModeloMundo' responsável por representar e gerenciar o modelo interno do ambiente de um agente autónomo.

    O modelo do mundo mantém uma representação do estado atual do agente, dos estados possíveis, dos elementos do 
    ambiente (como alvos e obstáculos) e dos operadores disponíveis para transições. Ele suporta o planeamento 
    deliberativo ao fornecer informações sobre o ambiente e atualizar-se com base em percepções.

    A classe implementa a interface necessária para integração com planeadores, como o `PlaneadorPEE`, permitindo a 
    geração de planos de ação com base em estados e operadores. Ela também facilita o raciocínio prático, suportando a 
    exploração de opções e a avaliação de estados no contexto do processo de tomada de decisão.

    Esta classe encapsula o estado atual, os estados possíveis, os elementos do ambiente e os operadores como atributos 
    privados, acessíveis via propriedades e métodos, e fornece funcionalidades para atualizar o modelo, calcular 
    distâncias e exibir o ambiente.
"""


class ModeloMundo(ModeloPlan):

    # Inicializa uma instância do modelo do mundo com atributos vazios e operadores predefinidos.
    def __init__(self):

        # Define o atributo privado `__estado` como None, indicando que o estado atual do agente ainda não foi
        # estabelecido, aguardando a primeira percepção.
        self.__estado    = None

        # Inicializa o atributo privado `__estados` como uma lista vazia, que armazenará os estados possíveis do
        # ambiente, a serem preenchidos com base em percepções.
        self.__estados   = []

        # Define o atributo privado `__alterado` como False, indicando que o modelo não foi modificado desde a última
        # atualização.
        self.__alterado  = False

        # Inicializa o atributo privado `__elementos` como um dicionário vazio, que mapeará posições a elementos do
        # ambiente, como alvos e obstáculos.
        self.__elementos = {}

        # Cria uma lista de instâncias de `OperadorMover` para cada direção em `Direccao`, associando cada operador ao
        # modelo atual, permitindo transições no espaço de estados.
        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]


    # Propriedade que devolve o estado de alteração do modelo do mundo.
    @property
    def alterado(self):
        return self.__alterado


    # Propriedade que devolve o dicionário de elementos do ambiente.
    @property
    def elementos(self):
        return self.__elementos


    # Metodo que devolve o estado atual do agente no ambiente.
    # Retorna a instância de `EstadoAgente` que representa a posição atual do agente, essencial para o planeamento e a
    # execução de ações no controle deliberativo.
    def obter_estado(self):
        # Retorna o valor do atributo privado `__estado`, que contém a instância de `EstadoAgente` representando a
        # posição atual do agente.
        return self.__estado


    # Metodo que devolve a lista de estados possíveis no ambiente.
    # Retorna uma lista de instâncias de `EstadoAgente`, cada uma representando uma posição válida no ambiente, usada
    # pelo planeador para explorar o espaço de estados.
    def obter_estados(self):
        # Retorna o valor do atributo privado `__estados`, que contém a lista de estados possíveis gerada a partir das
        # posições do ambiente.
        return self.__estados


    # Metodo que devolve a lista de operadores de movimento disponíveis.
    # Retorna a lista de instâncias de `OperadorMover`, cada uma associada a uma direção, permitindo ao planeador
    # simular transições entre estados.
    def obter_operadores(self):
        # Retorna o valor do atributo privado `__operadores`, que contém a lista de operadores de movimento
        # inicializados na criação do modelo.
        return self.__operadores


    # Metodo que devolve o elemento associado à posição de um estado.
    # Consulta o dicionário de elementos para verificar se há um elemento (como alvo ou obstáculo) na posição do
    # estado fornecido, retornando None se não houver.
    def obter_elemento(self, estado):
        # Usa o metodo `get` do dicionário `__elementos` para obter o elemento associado à posição do estado,
        # retornando None se a posição não estiver mapeada.
        return self.__elementos.get(estado.posicao, None)


    # Metodo que calcula a distância euclidiana entre a posição de um estado e o estado atual do agente.
    # Utiliza a função `math.dist` para calcular a distância entre as posições, suportando a seleção de objetivos
    # baseada em proximidade no controle deliberativo.
    def distancia(self, estado):
        # Calcula a distância euclidiana entre a posição do estado fornecido e a posição do estado atual do agente,
        # usando a função `math.dist`.
        return math.dist(estado.posicao, self.__estado.posicao)


    # Metodo que atualiza o modelo do mundo com base em uma nova percepção do ambiente.
    # Atualiza o estado atual do agente, verifica se os elementos do ambiente foram alterados e, se necessário,
    # atualiza os elementos e os estados possíveis. Este metodo é essencial para o processo cíclico de tomada de
    # decisão, permitindo a adaptação do modelo às mudanças no ambiente.
    def actualizar(self, percepcao):

        # Cria uma nova instância de `EstadoAgente` com a posição fornecida na percepção, atualizando o estado atual
        # do agente no modelo.
        self.__estado   = EstadoAgente(percepcao.posicao)

        # Compara o dicionário atual de elementos com o dicionário de elementos da percepção, definindo `__alterado`
        # como True se houver diferenças, indicando a necessidade de reconsideração.
        self.__alterado = self.__elementos != percepcao.elementos

        # Verifica se o modelo foi alterado, executando atualizações adicionais apenas se necessário para evitar
        # processamento redundante.
        if self.__alterado:

            # Atualiza o dicionário `__elementos` com os novos elementos fornecidos pela percepção, refletindo a
            # configuração atual do ambiente.
            self.__elementos = percepcao.elementos

            # Cria uma nova lista de instâncias de `EstadoAgente` para todas as posições fornecidas na percepção,
            # atualizando os estados possíveis no ambiente.
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]


    # Metodo que exibe o estado do modelo do mundo em uma interface visual.
    # Itera sobre os elementos do ambiente, exibindo alvos e obstáculos na interface fornecida, e marca a posição
    # atual do agente. Este metodo suporta a visualização do ambiente para depuração ou interação com o usuário
    def mostrar(self, vista):

        # Itera sobre os pares (posição, elemento) no dicionário `__elementos`, processando cada elemento do ambiente.
        for (posicao, elemento) in self.__elementos.items():

            # Verifica se o elemento é um alvo ou obstáculo, exibindo apenas esses tipos para evitar sobrecarga visual.
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:

                # Chama o metodo `mostrar_elemento` da interface visual, passando a posição e o elemento para exibição.
                vista.mostrar_elemento(posicao, elemento)

        # Chama o metodo `marcar_posicao` da interface visual, marcando a posição atual do agente no ambiente.
        vista.marcar_posicao(self.__estado.posicao)


    # Este metodo utiliza o operador `in` para determinar se o estado fornecido está presente na lista de estados
    # possíveis (`__estados`), permitindo verificar a validade de um estado no contexto do ambiente. É essencial
    # para o planeamento deliberativo, garantindo que apenas estados válidos sejam considerados durante a procura.
    def __contains__(self, estado):

        # Verifica se o estado fornecido está presente na lista de estados possíveis `__estados`, utilizando o operador
        # `in` para realizar a comparação.
        return estado in self.__estados
