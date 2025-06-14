from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof

"""
    Classe 'ProcuraSofraga', derivada de 'ProcuraMelhorPrim', responsável por implementar o algoritmo de procura gulosa
    (ou 'só heurística').

    Esta classe configura a procura gulosa, um algoritmo informado que explora o espaço de estados ordenando os nós na
    fronteira com base exclusivamente na estimativa heurística h(n), que representa o custo estimado do estado atual até
    o objetivo. Diferentemente de A*, que combina g(n) (custo acumulado) com h(n), a procura gulosa ignora o custo 
    acumulado, priorizando nós que parecem mais próximos do objetivo, mas não garante optimalidade, mesmo com uma 
    heurística admissível.

    A classe herda de 'ProcuraMelhorPrim', que fornece a lógica de procura em grafos com uma fronteira de prioridade
    ('FronteiraPrioridade') e gestão de estados repetidos. 'ProcuraSofraga' especifica o avaliador 'AvaliadorSof', que
    calcula a prioridade com base em h(n). É adequada para problemas onde a heurística é altamente informativa.
"""

class ProcuraSofraga(ProcuraInformada):

    # Inicializa uma instância de 'ProcuraSofraga' com um avaliador específico para procura gulosa.
    def __init__(self):

        # Incializa o AvaliadorSof
        avaliador_sof = AvaliadorSof()

        # Chama o construtor da classe base 'ProcuraMelhorPrim', passando o avaliador para configurar a fronteira e a
        # lógica de procura com base na procura gulosa.
        super().__init__(avaliador_sof)