from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
    Classe 'ProcuraCustoUnif', derivada de 'ProcuraMelhorPrim', responsável por implementar o algoritmo de procura de
    custo uniforme.

    Esta classe configura a procura de custo uniforme, um algoritmo que explora o espaço de estados ordenando os nós na 
    fronteira com base no custo acumulado g(n), garantindo que o caminho de menor custo até o estado objetivo seja 
    encontrado primeiro. A procura de custo uniforme é ótima quando os custos das transições são positivos, sendo 
    adequada para problemas onde o custo do percurso é a métrica principal. 
"""

class ProcuraCustoUnif(ProcuraMelhorPrim):

    # Inicializa uma instância do algoritmo de procura de custo uniforme.
    def __init__(self):

        # Cria uma nova instância de `AvaliadorCustoUnif`, que será usada para avaliar nós com base no custo acumulado
        # g(n)
        avaliador_custo_unif = AvaliadorCustoUnif()

        # Chama o construtor da classe base `ProcuraMelhorPrim`, passando o avaliador de custo uniforme para configurar
        # a estratégia de ordenação da fronteira.
        super().__init__(avaliador_custo_unif)

