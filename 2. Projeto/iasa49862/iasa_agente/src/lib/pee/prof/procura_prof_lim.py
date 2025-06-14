from pee.prof.fronteira_lifo import FronteiraLIFO
from pee.prof.procura_profundidade import ProcuraProfundidade

"""
Classe 'ProcuraProfLim', que implementa a estratégia de procura em profundidade limitada 
(Depth-Limited Search).

Esta classe herda da classe 'ProcuraProfundidade' e modifica a expansão de nós para respeitar um limite 
máximo de profundidade, evitando a exploração de ramificações muito profundas que podem ocorrer na procura 
em profundidade padrão.

A procura em profundidade limitada é útil para controlar o consumo de recursos em espaços de estados 
potencialmente infinitos ou muito profundos, mas não é completa nem ótima, pois pode falhar em encontrar 
uma solução se o limite for insuficiente.
"""

class ProcuraProfLim(ProcuraProfundidade):

    # Inicializa uma instância da procura em profundidade limitada com um limite máximo de profundidade.
    # Este metodo chama o construtor da classe base 'ProcuraProfundidade' para configurar a fronteira
    # LIFO e define o limite de profundidade que restringirá a expansão de nós.
    # O limite de profundidade é usado para evitar que a procura explore ramificações além de um certo
    # nível.
    def __init__(self, prof_max):

        # Chama o construtor da classe base 'ProcuraProfundidade', que inicializa o mecanismo de
        # procura com uma fronteira LIFO, garantindo a exploração em profundidade.
        super().__init__()

        # Armazena o limite máximo de profundidade como um atributo protegido, que será usado
        # para restringir a expansão de nós durante a procura.
        self._prof_max = prof_max


    # Expande um nó, gerando seus sucessores, mas apenas se a profundidade do nó não exceder o
    # limite máximo.
    # Este metodo sobrescreve o '_expandir' da classe base para adicionar a restrição de
    # profundidade, retornando uma lista vazia se o limite for ultrapassado, evitando a
    # exploração de nós mais profundos.
    # ATT: a verificação de profundidade é essencial para limitar a procura e prevenir ramificações infinitas.
    def _expandir(self, problema, no):

        # Verifica se a profundidade do nó atual é menor que o limite máximo definido (porque o 0 conta),
        # permitindo a expansão apenas dentro do limite estabelecido.
        if no.profundidade < self._prof_max:

            # Chama o metodo '_expandir' da classe base 'ProcuraProfundidade', que aplica os
            # operadores do problema ao estado do nó para gerar seus sucessores, retornando a
            # lista de novos nós.
            return super()._expandir(problema, no)

        else:
            # Retorna uma lista vazia se a profundidade do nó exceder o limite, indicando que
            # este nó não deve ser expandido, interrompendo a exploração dessa ramificação.
            return []