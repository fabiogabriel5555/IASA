from pee.mec_proc.fronteira import Fronteira

"""
Classe 'FronteiraFIFO', que implementa uma fronteira do tipo FIFO (First-In, First-Out).

Esta classe herda da classe abstrata 'Fronteira' e é usada na procura em largura (Breadth-First Search), onde os nós 
mais antigos, situados em menor profundidade, são explorados primeiro. Isso garante que a solução encontrada seja a 
de menor profundidade.

A estratégia FIFO insere novos nós no final da lista e remove nós do início, funcionando como uma fila, o que assegura 
a exploração nível por nível da árvore de procura.
"""

class FronteiraFIFO(Fronteira):

    # Inicializa uma instância da fronteira FIFO, configurando-a como vazia.
    # Este metodo chama o construtor da classe base 'Fronteira' para inicializar a lista interna de nós, garantindo
    # que a fronteira esteja pronta para uso na procura em largura.
    def __init__(self):
        # Chama o construtor da classe base 'Fronteira' para executar a inicialização padrão, que define a lista
        # '_nos' como vazia.
        super().__init__()


    # Insere um nó no final da fronteira, seguindo a lógica FIFO.
    # Este metodo adiciona o nó ao final da lista interna de nós, garantindo que os nós mais recentes sejam
    # explorados após os nós mais antigos, característica essencial da procura em largura.
    # ATT: A inserção no final da lista assegura que os nós de menor profundidade sejam processados primeiro.
    def inserir(self, no):
        # Adiciona o nó ao final da lista interna '_nos', implementando a lógica de uma fila onde o último nó
        # inserido será o último a ser removido.
        self._nos.append(no)