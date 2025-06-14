from pee.larg.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
Classe 'ProcuraLargura', que implementa a estratégia de procura em largura (Breadth-First Search).

Esta classe herda da classe abstrata 'MecanismoProcura' e utiliza uma fronteira FIFO (First-In, First-Out) para 
explorar o espaço de estados nível por nível, garantindo que todos os nós de uma dada profundidade sejam processados 
antes de passar para o próximo nível.

A procura em largura é completa (encontra uma solução se ela existir) e ótima em termos de profundidade (encontra a 
solução com o menor número de passos) em grafos sem custos diferenciados.
"""

class ProcuraLargura(MecanismoProcura):

    # Inicializa uma instância da procura em largura, configurando-a com uma fronteira FIFO.
    # Este metodo chama o construtor da classe base 'MecanismoProcura', passando uma instância de 'FronteiraFIFO'
    # como argumento, para garantir que os nós sejam geridos segundo a lógica FIFO, essencial para a procura em largura.
    # ATT: A fronteira FIFO assegura a exploração
    # nível por nível, começando pelos nós mais antigos (menor profundidade).
    def __init__(self):
        # Chama o construtor da classe base 'MecanismoProcura', inicializando o mecanismo de procura com uma
        # instância de 'FronteiraFIFO', que implementa a estratégia de inserção no final e remoção no início
        # da lista de nós.
        super().__init__(FronteiraFIFO())
