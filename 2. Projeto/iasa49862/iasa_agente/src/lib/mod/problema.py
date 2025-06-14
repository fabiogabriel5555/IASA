from abc import ABC, abstractmethod

"""
    Classe abstrata Problema, responsºavel por definir a estrutura base para a representação de um problema.

    Um problema é o modelo central que encapsula os elementos necessários para a resolução  automática: o estado 
    inicial, o conjunto de operadores (ações possíveis) e a função objetivo que determina se uma solução foi alcançada. 
    
    Esta classe serve como base para a simulação prospectiva do domínio do problema, permitindo a exploração do espaço 
    de estados até atingir o estado objetivo, como parte integrante do processo de raciocínio automático.
"""

class Problema(ABC):

    # Inicializa uma instância do problema com um estado inicial e um conjunto de operadores.
    #
    # O estado inicial representa a configuração de partida do problema enquanto os operadores definem as ações
    # possíveis para explorar o espaço de estados.
    def __init__(self, estado_inicial, operadores):
        self.__operadores = operadores
        self.__estado_inicial = estado_inicial


    # Propriedade que fornece acesso ao estado inicial do problema.
    #
    # Esta propriedade retorna o estado inicial armazenado, que representa a configuração  de partida do espaço de
    # estados a ser explorado.
    #
    # O estado inicial é um dos elementos definidores do problema, servindo como ponto de partida para os mecanismos
    # de procura
    @property
    def estado_inicial(self):
        return self.__estado_inicial

    # Propriedade que fornece acesso ao conjunto de operadores do problema.
    #
    # Esta propriedade retorna a lista de operadores disponíveis, que representam as ações possíveis para transformar
    # estados no espaço de estados.
    #
    # Esses operadores são usados pelos mecanismos de procura para gerar estados sucessores a partir do estado inicial
    # ou de outros estados intermediários.
    @property
    def operadores(self):
        return self.__operadores

    # Metodo abstrato operadores, responsável por verificar se um dado estado satisfaz a condição de objetivo do
    # problema.
    #
    # Este metodo define a função objetivo do problema, que determina se um estado representa uma solução.
    # O objetivo pode ser representado como uma função `estado → {True, False}`, indicando se o estado atual é o estado
    # objetivo ou satisfaz os critérios de sucesso.
    #
    # Este metodo é essencial para os mecanismos de procura em espaço de estados, pois sinaliza quando a exploração deve
    # terminar.
    @abstractmethod
    def objectivo(self, estado):
        """Abstract Method"""

