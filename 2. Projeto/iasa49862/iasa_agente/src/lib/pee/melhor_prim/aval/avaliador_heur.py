from pee.melhor_prim.aval.avaliador import Avaliador

"""
    Classe abstrata 'AvaliadorHeur', derivada de 'Avaliador', responsável por gerir uma heurística para algoritmos de
    procura informada.

    Esta classe estende 'Avaliador' para incorporar uma heurística, que é usada para estimar o custo restante de um nó
    até o estado objetivo (h(n)) em algoritmos como A* A heurística é essencial para direcionar a procura em direção a 
    estados promissores, reduzindo o número de nós expandidos em comparação com algoritmos não informados, como procura 
    de custo uniforme ou largura.

    A classe fornece uma propriedade 'heuristica' para armazenar e acessar uma instância de uma classe de heurística,
    que deve implementar um método 'h(estado)' para calcular h(n). A heurística deve ser admissível (não superestimar
    o custo real) para garantir a optimalidade em A*.

    Esta classe serve como base para avaliadores específicos, como 'AvaliadorAA', que combinam a heurística com o custo
    acumulado g(n) para formar a função de avaliação f(n) = g(n) + h(n). É usada em
    problemas como o puzzle de 8 peças, onde heurísticas como a distância de Manhattan são comuns, ou navegação
    autónoma, onde a distância euclidiana pode ser usada.
"""

class AvaliadorHeur(Avaliador):

    def __init__(self):

        self._heuristica = None


    @property
    def heuristica(self):
        return self._heuristica


    @heuristica.setter
    def heuristica(self, value):
        self._heuristica = value