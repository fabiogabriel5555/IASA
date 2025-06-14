from pee.mec_proc.fronteira import Fronteira

"""
Classe 'FronteiraLIFO', que implementa uma fronteira do tipo LIFO (Last-In, First-Out).

Esta classe herda da classe abstrata 'Fronteira' e é usada na procura em profundidade (Depth-First Search), onde os nós 
mais recentes, situados em maior profundidade, são explorados primeiro. Isso resulta numa exploração que prioriza 
avançar ao longo de uma ramificação até atingir um limite ou encontrar a solução.

A estratégia LIFO insere novos nós no início da lista e remove nós do início, funcionando como uma pilha, o que 
assegura a exploração em profundidade da árvore de procura.
"""

class FronteiraLIFO(Fronteira):

    # Inicializa uma instância da fronteira LIFO, configurando-a como vazia.
    # Este metodo chama o construtor da classe base 'Fronteira' para inicializar a lista interna de nós, garantindo
    # que a fronteira esteja pronta para uso na procura em profundidade.
    def __init__(self):
        # Chama o construtor da classe base 'Fronteira' para executar a inicialização padrão, que define a lista
        # '_nos' como vazia.
        super().__init__()


    # Insere um nó no início da fronteira, seguindo a lógica LIFO.
    # Este metodo adiciona o nó ao início da lista interna de nós, garantindo que os nós mais recentes sejam
    # explorados primeiro, característica essencial da procura em profundidade.
    # ATT: A inserção no início da lista assegura que os sucessores recém-gerados sejam priorizados, levando a uma
    # exploração em profundidade.
    def inserir(self, no):
        # Insere o nó na posição inicial (índice 0) da lista interna '_nos', implementando a lógica de uma pilha
        # onde o último nó inserido será o primeiro a ser removido.
        self._nos.insert(0, no)