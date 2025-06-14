from abc import ABC, abstractmethod

"""
    Classe abstrata Fronteira, responsável por defenir a estrutura base para uma fronteira de exploração.

    A fronteira é uma estrutura de dados essencial no mecanismo de procura, responsável por armazenar e gerir os nós 
    abertos (nós gerados mas ainda não expandidos) durante a exploração do espaço de estados. 
    
    A forma como os nós são inseridos e removidos define a estratégia de controlo da procura, como procura em 
    profundidade (Depth-First Search) ou procura em largura (Breadth-First Search). 
    
    Esta classe abstrai as operações básicas de inicialização, inserção e remoção de nós, permitindo diferentes 
    implementações (e.g.,FIFO, LIFO) conforme o tipo de procura.
"""
class Fronteira(ABC):

    # Inicializa uma instância da fronteira, definindo-a como vazia.
    def __init__(self):
        # Chama o metodo iniciar para configurar a lista de nós como vazia.
        self.iniciar()


    # Propriedade 'vazia', responsável por indicar se a fronteira está vazia.
    #
    # Esta propriedade fornece acesso ao estado interno da fronteira, retornando `True` se
    # não houver nós para explorar e `False` caso contrário.
    #
    # É um elemento crítico no controlo do processo de procura, como visto em 'Procura em Espaços de Estados', onde
    # o ciclo de exploração termina quando a fronteira fica vazia e não foi encontrada solução.
    @property
    def vazia(self):
        # Retorna True se a lista de nós estiver vazia, False caso contrário.
        return len(self._nos) == 0

    # Metodo que inicializa ou reinicializa a fronteira, configurando-a como vazia.
    def iniciar(self):
        # Define a lista interna de nós como uma lista vazia.
        self._nos = []


    # Metodo abstrato que insere um nó na fronteira de exploração.
    #
    # Este metodo adiciona um nó à fronteira, respetando a estratégia de controlo da procura definida pela subclasse.
    #
    # A fronteira permite inserir e remover nós de forma ordenada', e a ordem de inserção determina se a procura é em
    # profundidade ou em largura.
    #
    # É usado para adicionar estados sucessores gerados pela expansão de um nó, como no ciclo de procura.
    @abstractmethod
    def inserir(self, no):
        """ Abstract Method"""

    # Metodo que remove e retorna um nó da fronteira.
    def remover(self):
        # Remove e retorna o primeiro nó da lista interna de nós, seguindo uma lógica FIFO.
        return self._nos.pop(0)