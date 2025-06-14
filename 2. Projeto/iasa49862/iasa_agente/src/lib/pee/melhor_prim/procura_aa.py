from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA

"""
    Classe 'ProcuraAA', derivada de 'ProcuraMelhorPrim', responsável por implementar o algoritmo de procura A*.

    Esta classe configura a procura A*, um algoritmo informado que explora o espaço de estados ordenando os nós na
    fronteira com base na função de avaliação f(n) = g(n) + h(n), onde g(n) é o custo acumulado desde o estado inicial
    e h(n) é a estimativa heurística do custo restante até o objetivo. A procura A* é
    completa e ótima quando a heurística é admissível (h(n) ≤ custo real), e idealmente monotónica para maior eficiência
    em procura em grafos.

    A classe herda de 'ProcuraMelhorPrim', que fornece a lógica de procura em grafos com uma fronteira de prioridade
    ('FronteiraPrioridade') e gestão de estados repetidos. 'ProcuraAA' especifica o avaliador 'AvaliadorAA', que calcula
    a prioridade com base em f(n) = g(n) + h(n). É adequada para problemas como o puzzle
    de 8 peças, onde a distância de Manhattan é uma heurística comum, ou navegação autónoma, onde a distância euclidiana
    pode guiar a procura.
"""

class ProcuraAA(ProcuraInformada):

    # Inicializa uma instância de 'ProcuraAA' com um avaliador específico para A*.
    #
    # Este metodo configura a procura A* passando um avaliador ('AvaliadorAA') para o construtor da classe base
    # 'ProcuraMelhorPrim'. O avaliador calcula a prioridade dos nós com base em f(n) = g(n) + h(n), garantindo que a
    # fronteira priorize nós com menor valor estimado de custo total.
    #
    # A classe base 'ProcuraMelhorPrim' inicializa a 'FronteiraPrioridade' e gerencia a lógica de procura em grafos,
    # incluindo a gestão de estados repetidos, enquanto 'ProcuraAA' define a estratégia de avaliação específica para A*.
    def __init__(self):

        # Incializa o AvaliadorAA
        avaliador_aa = AvaliadorAA()

        # Chama o construtor da classe base 'ProcuraMelhorPrim', passando o avaliador para configurar a fronteira e a
        # lógica de procura com base em A*.
        super().__init__(avaliador_aa)