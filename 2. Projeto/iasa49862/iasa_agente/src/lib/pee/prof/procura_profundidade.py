from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteira_lifo import FronteiraLIFO

"""
Classe 'ProcuraProfundidade', que implementa a estratégia de procura em profundidade (Depth-First Search).

Esta classe herda da classe abstrata 'MecanismoProcura' e utiliza uma fronteira LIFO (Last-In, First-Out) para 
explorar o espaço de estados, priorizando os nós mais recentes, o que resulta numa exploração que avança ao longo 
de uma ramificação até atingir um limite ou encontrar a solução.

A procura em profundidade é eficiente em termos de memória, mas não é completa em espaços infinitos ou com ciclos, 
nem garante a solução de menor profundidade.
"""

class ProcuraProfundidade(MecanismoProcura):

    # Inicializa uma instância da procura em profundidade, configurando-a com uma fronteira LIFO.
    # Este metodo chama o construtor da classe base 'MecanismoProcura', passando uma instância de
    # 'FronteiraLIFO' como argumento, para garantir que os nós sejam geridos segundo a lógica LIFO,
    # essencial para a procura em profundidade.
    # ATT: a fronteira LIFO assegura que
    # os nós mais recentes (de maior profundidade) sejam processados primeiro.
    def __init__(self):
        # Chama o construtor da classe base 'MecanismoProcura', inicializando o mecanismo de
        # procura com uma instância de 'FronteiraLIFO', que implementa a estratégia de inserção
        # e remoção no início da lista de nós, funcionando como uma pilha.
        super().__init__(FronteiraLIFO())

