from contegem.modelo.problema_contagem import ProblemaContagem
from pee.larg.procura_largura import ProcuraLargura
from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.prof.procura_prof_iter import ProcuraProfIter
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_profundidade import ProcuraProfundidade

"""
    Script para testar a resolução de um problema de contagem utilizando diferentes estratégias de procura,
    incluindo procura em largura, profundidade limitada, profundidade iterativa, e custo uniforme.

    O problema é definido como alcançar ou ultrapassar um valor final (9) a partir de um valor inicial (0),
    aplicando operadores de incremento (1, 2, ou -1). Cada estratégia de procura é testada para encontrar uma
    solução, explorando o espaço de estados de acordo com sua abordagem específica (página 5 de "10-pee-1.pdf").

    O script demonstra:
    - A configuração de um problema de contagem usando a classe 'ProblemaContagem'.
    - A execução de diferentes mecanismos de procura ('ProcuraLargura', 'ProcuraProfLim', 'ProcuraProfIter',
      'ProcuraCustoUnif') para resolver o problema.
    - A apresentação dos resultados, incluindo a sequência de incrementos, dimensão da solução, custo total,
      número de nós processados, e máximo de nós em memória.

    A função 'sol' é usada para exibir os resultados de cada procura, detalhando os passos da solução (se encontrada)
    e métricas de desempenho, como complexidade temporal e espacial (página 9 de "11-pee-2.pdf").
"""


# Função auxiliar para exibir os resultados de uma procura, incluindo a solução encontrada (se houver)
# e métricas de desempenho.
def sol(mec_proc, solucao):

    # Verifica se uma solução foi encontrada e exibe os resultados.
    # Se 'solucao' não for None, percorre sobre os passos da solução para mostrar o valor do estado
    # e o incremento aplicado em cada transição; caso contrário, indica que nenhuma solução foi
    # encontrada.
    if solucao:

        # Extrai a lista de incrementos aplicados nos passos da solução, onde cada passo contém um
        # operador ('OperadorIncremento') com um atributo 'incremento'.
        passos = [passo.operador.incremento for passo in solucao]

        # Exibe a sequência de incrementos, a dimensão (número de passos), o custo total da solução,
        # o número de nós processados, e o máximo de nós em memória.
        print(f"Solução:  {passos}")
        print(f"Dimensão: {solucao.dimensao}")
        print(f"Custo:    {solucao.custo}")
        print(f"Nós processadaos:         {mec_proc.nos_processados}")
        print(f"Maximo de nós em memória: {mec_proc.nos_em_memoria}")

        if isinstance(mec_proc, ProcuraCustoUnif):
            print(f"Número de estados não repetidos: {len(mec_proc._explorados)}")

        # Código para exibir uma descrição detalhada dos passos da solução.
        # Percorre os passos da solução, que são instâncias de 'PassoSolucao' contendo um estado ('EstadoContagem') e
        # um operador ('OperadorIncremento').
        # A solução é iterável, permitindo acesso aos passos em ordem (página 30 de "10-pee-1.pdf").
        """
        print("------ ------ ------ ------ ------ ------ ------ ------")
        print(" Inicio Descrição completa dos passos" )
        for passo in solucao:
            print(" Passos:")
            print("  valor: " + str(passo.estado.valor))
            print("  incremento: " + str(passo.operador.incremento))
        print(" Fim Descrição completa dos passos")
        print("------ ------ ------ ------ ------ ------ ------ ------")
        """

    # Imprime uma mensagem indicando que nenhuma solução foi encontrada dentro do limite
    # de profundidade especificado.
    else:
        print("Solução não encontrada")



# Define o valor inicial do estado, que representa o ponto de partida do problema de contagem.
# Neste caso, o valor inicial é 0, indicando que a contagem começa do zero.
VALOR_INICIAL = 0


# Define o valor final que o estado deve alcançar ou ultrapassar para ser considerado uma solução.
# O valor final é 9, significando que o objetivo é atingir ou superar 9 através de incrementos.
VALOR_FINAL = 9


# Define a lista de incrementos possíveis que podem ser aplicados ao estado atual.
# Os valores [1, 2, -1] indicam que o estado pode ser incrementado em 1, 2, ou decrementado em 1
# unidade em cada transição, permitindo maior flexibilidade no espaço de estados.
INCREMENTOS = [1, 2, -1]


# Cria uma instância do problema de contagem, configurando-o com o estado inicial, o valor final
# e os operadores de incremento.
# A classe 'ProblemaContagem' modela o problema, definindo:
# - O estado inicial como 'EstadoContagem(0)'.
# - Os operadores como instâncias de 'OperadorIncremento' para cada incremento (1, 2, -1).
# - O objetivo como alcançar ou ultrapassar o valor 9.
# O problema encapsula o espaço de estados e as transições possíveis (página 29 de "10-pee-1.pdf").
problema = ProblemaContagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS)


# Testa a procura em largura, que explora nós por níveis de profundidade, garantindo a solução com
# menor número de passos (página 21 de "10-pee-1.pdf").
print("PROCURA EM LARGURA: ")
mec_proc = ProcuraLargura()
solucao = mec_proc.procurar(problema)
sol(mec_proc, solucao)
print("")


# Testa a procura em profundidade limitada, que explora até um limite de profundidade (5 neste caso),
# podendo falhar se o objetivo estiver além do limite (página 9 de "10-pee-1.pdf").
print("PROCURA EM PROFUNDIDADE LIMITADA: ")
mec_proc = ProcuraProfLim(5)
solucao = mec_proc.procurar(problema)
sol(mec_proc, solucao)
print("")


# Testa a procura em profundidade iterativa, que incrementa o limite de profundidade (de 1 até 10)
# até encontrar uma solução ou atingir o limite máximo, combinando a eficiência da profundidade
# com a completude da largura (página 9 de "10-pee-1.pdf").
print("PROCURA EM PROFUNDIDADE ITERATIVA: ")
mec_proc = ProcuraProfIter(5)
solucao = mec_proc.procurar(problema, 1, 10)
sol(mec_proc, solucao)
print("")


# Testa a procura de custo uniforme, que ordena nós pelo custo acumulado g(n), garantindo a solução
# com menor custo total, assumindo custos positivos para os operadores (página 19 de "11-pee-2.pdf").
print("PROCURA CUSTO UNIFORME: ")
mec_proc = ProcuraCustoUnif()
solucao = mec_proc.procurar(problema)
sol(mec_proc, solucao)
print("")







