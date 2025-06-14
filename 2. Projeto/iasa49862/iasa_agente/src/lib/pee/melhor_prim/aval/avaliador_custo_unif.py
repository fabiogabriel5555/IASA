from pee.melhor_prim.aval.avaliador import Avaliador

"""
    Classe 'AvaliadorCustoUnif', derivada de 'Avaliador', responsável por calcular a prioridade de nós para o algoritmo
    de procura de custo uniforme.

    Esta classe implementa a função de avaliação característica da procura de custo uniforme, onde a prioridade de um
    nó é dada pelo custo acumulado g(n), que representa o custo total do percurso desde o estado inicial até o nó.
    
    Diferentemente da procura A*, que combina g(n) com uma heurística h(n), a procura de custo uniforme é um algoritmo 
    não informado que considera apenas o custo real do percurso, garantindo a optimalidade em problemas com custos 
    positivos.

    A classe é usada em conjunto com uma fronteira de prioridade (PriorityQueue) para ordenar nós com base no custo
    acumulado g(n), onde nós com menor custo são expandidos primeiro. É aplicável a problemas como navegação em mapas 
    ou o puzzle de 8 peças, onde o custo pode representar distâncias ou número de movimentos.
"""

class AvaliadorCustoUnif(Avaliador):

    # Metodo 'prioridade', responsável por calcular a prioridade de um nó para o algoritmo de procura de custo uniforme.
    #
    # Este metodo implementa a função de avaliação g(n), que é o custo acumulado do percurso desde o estado inicial até
    # o nó, obtido diretamente via 'no.custo'. A prioridade determina a ordem de expansão dos nós na fronteira, com nós
    # de menor g(n) sendo expandidos primeiro, conforme o funcionamento da procura de custo uniforme.
    #
    # A procura de custo uniforme garante a optimalidade quando os custos das transições são positivos, explorando o
    # espaço de estados de forma a encontrar o caminho de menor custo até o objetivo.
    def prioridade(self, no):

        return no.custo