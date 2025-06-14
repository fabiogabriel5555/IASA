from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade

"""
    Classe abstrata 'ProcuraMelhorPrim', derivada de 'ProcuraGrafo', responsável por implementar algoritmos de procura
    baseados em prioridade, como procura de custo uniforme, A*, e procura gulosa.

    Esta classe estende 'ProcuraGrafo' para suportar procura em grafos com uma fronteira de prioridade, onde os nós são
    ordenados com base em uma prioridade calculada por um avaliador. A prioridade pode ser o custo acumulado g(n) (procura
    de custo uniforme), a função de avaliação f(n) = g(n) + h(n) (A*), ou a estimativa heurística h(n) (procura gulosa).

    A classe utiliza uma 'FronteiraPrioridade' para gerir os nós abertos, ordenando-os por prioridade, e sobrescreve o
    método '_manter' para decidir se um nó sucessor deve ser mantido, considerando estados repetidos e comparando custos. 
    É adequada para problemas como o puzzle de 8 peças, onde estados repetidos são comuns,
    ou navegação autónoma, onde o custo ou a heurística guia a procura.
"""

class ProcuraMelhorPrim(ProcuraGrafo):

    # Inicializa uma instância de 'ProcuraMelhorPrim' com um avaliador específico.
    #
    # Este metodo configura a procura baseada em prioridade, inicializando a classe base 'ProcuraGrafo' com uma
    # 'FronteiraPrioridade' que usa o avaliador fornecido para calcular prioridades. O avaliador determina a estratégia
    # de ordenação da fronteira, como g(n) para custo uniforme, f(n) = g(n) + h(n) para A*, ou h(n) para procura gulosa.
    #
    # O avaliador é armazenado como atributo para uso no metodo '_manter', que compara prioridades de nós com estados
    # repetidos.
    def __init__(self, avaliador):

        # Chama o construtor da classe base 'ProcuraGrafo', passando uma 'FronteiraPrioridade' inicializada com o
        # avaliador, que ordenará os nós com base na prioridade calculada.
        super().__init__( FronteiraPrioridade(avaliador) )

        # Armazena o avaliador como atributo para uso em '_manter', permitindo comparar prioridades de nós com estados
        # repetidos.
        self._avaliador = avaliador



    # Metodo protegido '_manter', responsável por determinar se um nó sucessor deve ser mantido na procura.
    #
    # Este metodo sobrescreve o metodo abstrato de 'ProcuraGrafo' para decidir se um nó sucessor deve ser inserido na
    # fronteira, considerando estados repetidos. Um nó é mantido se:
    # - O estado do nó não está no dicionário '_explorados' (ou seja, é um estado novo).
    # - O estado já foi explorado, mas o novo nó tem um custo acumulado menor que o nó previamente explorado para o
    #   mesmo estado.
    #
    # Esta lógica é essencial para evitar a reexpansão de estados redundantes em grafos com ciclos, mantendo apenas o nó
    # com o menor custo para cada estado.
    def _manter(self, no):

        return no.estado not in self._explorados or no.custo < self._explorados[no.estado].custo