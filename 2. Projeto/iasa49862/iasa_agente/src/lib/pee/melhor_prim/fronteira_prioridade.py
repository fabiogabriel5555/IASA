from pee.mec_proc.fronteira import Fronteira
import heapq

"""
    Classe 'FronteiraPrioridade', derivada de 'Fronteira', responsável por gerir uma fronteira de exploração baseada em
    prioridade para algoritmos de procura.

    Esta classe implementa uma fronteira que ordena nós com base em uma prioridade calculada por um avaliador, utilizando
    uma estrutura de dados de heap (PriorityQueue) para garantir que o nó com menor prioridade seja removido primeiro.
    É usada em algoritmos como procura de custo uniforme (prioridade baseada em g(n)), A* (prioridade baseada em
    f(n) = g(n) + h(n)), e procura gulosa (prioridade baseada em h(n)).

    A classe depende de um avaliador (instância de 'Avaliador' ou suas subclasses) para calcular a prioridade de cada nó,
    que é armazenada no atributo 'prioridade' do nó. A estrutura de heap, fornecida pelo módulo 'heapq', assegura operações
    eficientes de inserção e remoção, com complexidade O(log n).

    A fronteira é essencial para controlar a ordem de expansão dos nós no espaço de estados, impactando a eficiência e a
    direção da procura em problemas como o puzzle de 8 peças ou navegação autónoma.
"""

class FronteiraPrioridade(Fronteira):

    # Inicializa uma instância de 'FronteiraPrioridade' com um avaliador específico.
    def __init__(self, avaliador):

        # Chama o construtor da classe base 'Fronteira' para inicializar a lista de nós (_nos) como vazia.
        super().__init__()

        # Armazena o avaliador como um atributo privado, que será usado para calcular a prioridade dos nós inseridos.
        self.__avaliador = avaliador



    # Insere um nó na fronteira, atribuindo-lhe uma prioridade calculada pelo avaliador.
    #
    # Este metodo calcula a prioridade do nó usando o avaliador fornecido, armazena-a no atributo 'prioridade' do nó e
    # insere o nó na estrutura de heap, que mantém os nós ordenados por prioridade (menor prioridade primeiro).
    #
    # A inserção é realizada com a função 'heappush' do módulo 'heapq', garantindo complexidade O(log n), onde n é o
    # número de nós na fronteira. A prioridade determina a ordem de expansão, essencial para algoritmos como A* ou custo
    # uniforme.
    def inserir(self, no):

        # Calcula a prioridade do nó usando o metodo 'prioridade' do avaliador, que pode retornar g(n) (custo uniforme),
        # f(n) = g(n) + h(n) (A*), ou h(n) (gulosa).
        no.prioridade = self.__avaliador.prioridade(no)

        # Insere o nó na lista '_nos' usando 'heappush', que mantém a propriedade de heap (nó com menor prioridade no
        # topo), garantindo que o próximo nó removido será o de menor prioridade.
        heapq.heappush(self._nos, no)



    # Remove e devolve o nó com a menor prioridade da fronteira.
    #
    # Este metodo extrai o nó com a menor prioridade da estrutura de heap usando 'heappop', garantindo que o nó mais
    # prioritário (com menor valor de prioridade) seja retornado para expansão.
    #
    # A remoção tem complexidade O(log n), onde n é o número de nós na fronteira, e é essencial para algoritmos que
    # exploram nós na ordem de prioridade, como procura de custo uniforme, A*, ou gulosa.
    def remover(self):

        # Remove e devolve o nó no topo do heap (menor prioridade) usando 'heappop', que mantém a propriedade de heap
        # após a remoção.
        return heapq.heappop(self._nos)