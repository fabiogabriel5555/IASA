from mod.estado import Estado

"""
    Classe 'EstadoAgente' responsável por representar o estado de um agente autónomo num ambiente, derivada da classe 
    base 'Estado'.

    A classe é usada no contexto de uma arquitetura deliberativa, onde o estado do agente é integrado ao modelo do mundo, 
    atualizado com base em percepções e utilizado para simular transições através de operadores, como o `OperadorMover` 
    
    A unicidade do estado, garantida pelo hash da posição, alinha-se com a exploração de opções no raciocínio 
    automático, essencial para o processo de tomada de decisão 

    Esta classe encapsula a posição do agente como um atributo privado, acessível via propriedade, e calcula um 
    identificador único para suportar a gestão eficiente de estados em algoritmos de procura.
"""

class EstadoAgente(Estado):


    # Inicializa um estado do agente com uma posição específica.
    def __init__(self, posicao):

        # Armazena a posição fornecida no atributo privado `__posicao`
        self.__posicao = posicao

        # Calcula o hash da posição e armazena-o no atributo privado `__id_valor`, criando um identificador único para
        # o estado, conforme.
        self.__id_valor = hash(self.__posicao)


    # Propriedade que devolve a posição atual do agente no ambiente.
    @property
    def posicao(self):
        return self.__posicao

    # Propriedade que devolve o identificador único do estado.
    def id_valor(self):
        return self.__id_valor