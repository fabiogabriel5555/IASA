from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
    Classe 'AvaliadorAA', derivada de 'AvaliadorHeur', responsável por calcular a prioridade de nós para o algoritmo de
    procura A*.

    Esta classe implementa a função de avaliação característica do algoritmo A*, onde a prioridade de um nó é dada por
    f(n) = g(n) + h(n), sendo g(n) o custo acumulado do percurso desde o estado inicial até o nó e h(n) a estimativa
    heurística do custo restante até o estado objetivo.

    A classe utiliza uma heurística fornecida pela classe base 'AvaliadorHeur', que é assumida como admissível (não
    superestima o custo real) para garantir a optimalidade da procura A*. Esta abordagem é essencial em problemas de 
    planeamento, como o puzzle de 8 peças ou navegação autónoma, onde a heurística reduz o número de nós expandidos ao 
    direcionar a procura para estados promissores.

    A classe é usada em conjunto com uma fronteira de prioridade (PriorityQueue) para ordenar nós com base na função
    de avaliação f(n).
"""

class AvaliadorAA(AvaliadorHeur):

    # Metodo 'prioridade', responsável por calcular a prioridade de um nó para o algoritmo A*.
    #
    # Este metodo implementa a função de avaliação f(n) = g(n) + h(n), onde:
    # - g(n) é o custo acumulado até o nó, obtido via 'no.custo'.
    # - h(n) é a estimativa heurística do custo restante até o objetivo, calculada pela heurística fornecida pela
    #   classe base 'AvaliadorHeur'.
    #
    # A prioridade determina a ordem de expansão dos nós na fronteira, com nós de menor f(n) sendo expandidos primeiro.
    # A heurística deve ser admissível para garantir que
    # A* encontre a solução ótima, e idealmente monotónica para maior eficiência (página 18 de "12-pee-3.pdf").
    def prioridade(self, no):
        return no.custo + self.heuristica.h(no.estado)