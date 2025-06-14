import math

"""
    Classe 'HeurDistad' que implementa uma função heurística baseada na distância euclidiana para problemas de planeamento.

    Esta classe calcula uma estimativa heurística do custo para alcançar um estado final a partir de um estado atual, 
    utilizando a distância euclidiana entre as posições dos estados. A heurística é projetada para ser usada em 
    algoritmos de procura informada, como A* ou heurística gulosa, garantindo que a estimativa seja consistente 
    (monotônica) e admissível, ou seja, nunca superestima o custo real do caminho até o objetivo (página 23 de 
    "12-pee-3.pdf").

    A classe é usada no contexto de uma arquitetura deliberativa, onde a heurística auxilia o planeador (e.g., 
    `PlaneadorPEE`) a priorizar a exploração de estados mais próximos do objetivo, otimizando o processo de planeamento.
     Ela suporta o raciocínio prático ao fornecer uma métrica para avaliar estados no espaço de estados, essencial para 
     o ciclo de tomada de decisão.
"""

class HeurDist:

    # Inicializa uma instância da heurística com um estado final.
    def __init__(self, estado_final):

        # Armazena o estado final fornecido no atributo privado `__estado_final`, que será usado para calcular a
        # distância heurística em relação a outros estados.
        self.__estado_final = estado_final


    # MEtodo que calcula a estimativa heurística para um estado.
    #
    # Este mEtodo retorna a distância euclidiana entre a posição do estado fornecido e a posição do estado final,
    # servindo como uma estimativa do custo restante para alcançar o objetivo. A heurística é admissível, pois a
    # distância euclidiana é sempre menor ou igual ao custo real do caminho, e consistente, pois satisfaz a condição de
    # monotonicidade para algoritmos como A*.
    def h(self, estado):

        # Calcula a distância euclidiana entre a posição do estado fornecido (`estado.posicao`) e a posição do estado
        # final (`self.__estado_final.posicao`) usando a função `math.dist`, retornando o valor como a estimativa
        # heurística.
        return math.dist(estado.posicao, self.__estado_final.posicao)
