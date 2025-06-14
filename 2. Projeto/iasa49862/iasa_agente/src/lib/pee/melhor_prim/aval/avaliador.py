"""
    Classe 'Avaliador', responsável por definir a interface para avaliação da prioridade de nós na árvore de
    procura.

    Esta classe serve como base para implementações que calculam a prioridade de um nó, usada para ordenar nós em
    algoritmos de procura baseados em prioridade, como procura de custo uniforme e A*. A prioridade determina a
    ordem de expansão dos nós na fronteira, influenciando a eficiência e a direção da procura no espaço de estados.
"""

class Avaliador:

    def prioridade(self, no):
        raise NotImplementedError