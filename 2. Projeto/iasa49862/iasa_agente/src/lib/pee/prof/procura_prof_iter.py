from pee.prof.procura_prof_lim import ProcuraProfLim

"""
Classe 'ProcuraProfIter', que implementa a estratégia de procura em profundidade iterativa 
(Iterative Deepening Depth-First Search).

Esta classe herda da classe 'ProcuraProfLim' e realiza múltiplas procuras em profundidade limitada, 
incrementando o limite de profundidade em cada iteração até encontrar uma solução ou atingir um limite máximo.

A procura em profundidade iterativa combina a eficiência espacial da procura em profundidade 
(complexidade espacial O(b·d)) com a completitude e optimalidade da procura em largura, garantindo 
que a solução encontrada seja a de menor profundidade em grafos sem custos diferenciados.
"""

class ProcuraProfIter(ProcuraProfLim):

    # Inicializa uma instância da procura em profundidade iterativa com um limite de profundidade inicial.
    # Este metodo chama o construtor da classe base 'ProcuraProfLim', passando o limite de profundidade
    # máximo inicial, que será ajustado dinamicamente durante a procura iterativa.
    # O valor padrão de 'prof_max_inicial' é 99, mas pode ser personalizado para adaptar a procura a
    # diferentes problemas.
    # att: A inicialização define a base para as iterações com limites crescentes.
    def __init__(self, prof_max_inicial = 10):
        # Chama o construtor da classe base 'ProcuraProfLim', inicializando o mecanismo de procura com
        # o limite de profundidade especificado, que será atualizado nas iterações subsequentes.
        super().__init__(prof_max_inicial)


    # Executa a procura em profundidade iterativa para encontrar uma solução ao problema fornecido.
    # Este metodo percorre os limites de profundidade crescentes, começando de 0 até um limite máximo
    # especificado, com incrementos definidos, chamando a procura em profundidade limitada da classe
    # base para cada limite.
    # Retorna a solução encontrada na primeira iteração bem-sucedida ou None se nenhuma solução for
    # encontrada até o limite máximo.
    # ATT: A procura iterativa garante completitude e optimalidade ao combinar múltiplas procuras com
    # limites crescentes.
    def procurar(self, problema, inc_prof, limite_prof):
        # Percorre uma sequência de limites de profundidade, começando de 0 e incrementando por
        # 'inc_prof' até atingir ou exceder 'limite_prof', para realizar procuras sucessivas.
        for profundidade in range(0, limite_prof + 1, inc_prof):

            # Atualiza o limite de profundidade máximo da classe base ('_prof_max') para a iteração
            # atual, definindo o novo limite para a procura em profundidade limitada.
            self._prof_max = profundidade

            # Chama o metodo 'procurar' da classe base 'ProcuraProfLim', que executa uma procura em
            # profundidade limitada com o limite atual, retornando uma solução ou None.
            solucao = super().procurar(problema)

            # Verifica se uma solução foi encontrada na iteração atual; se sim, a procura termina.
            if solucao:

                # Devolve a solução encontrada, que representa o percurso até o estado objetivo,
                # garantindo que seja a de menor profundidade devido à ordem crescente dos limites.
                return solucao
