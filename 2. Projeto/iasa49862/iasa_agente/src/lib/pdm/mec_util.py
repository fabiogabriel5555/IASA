
"""
    Classe 'MecUtil', responsável por calcular as utilidades de estados em um Processo de Decisão de Markov (PDM).

    Esta classe implementa o algoritmo de iteração de valor, para determinar as utilidades de estados (U(s)) em um
    modelo PDM.

    O algoritmo atualiza iterativamente as utilidades com base na equação de Bellman.
"""

class MecUtil:

    # Inicializa uma instância do mecanismo de cálculo de utilidades.
    def __init__(self, modelo, gama, delta_max):

        self.__gama      = gama
        self.__delta_max = delta_max
        self.__modelo    = modelo

    # Calcula as utilidades de todos os estados usando iteração de valor.
    #
    # Implementa o algoritmo de iteração de valor, atualizando as utilidades para cada estado (s) com base na ação
    # que maximiza a utilidade esperada, até que a variação máxima (delta) seja menor ou igual a (delta_{max}).
    #
    # Retorna um dicionário mapeando estados para suas utilidades.
    def utilidade(self):

        # Inicializa um dicionário de utilidades com valor 0.0 para cada estado do modelo, obtido via modelo.S().
        U = { s: 0.0 for s in self.__modelo.S() }

        # Inicia um loop até que a convergência seja alcançada.
        while True:

            # Cria uma cópia do dicionário de utilidades atual para comparar com a próxima iteração.
            Uant = U.copy()

            # Inicializa a variação máxima (delta ) como 0.0 para a iteração atual.
            delta = 0.0

            # Percorre todos os estados do modelo.
            for s in self.__modelo.S():

                # Calcula a utilidade do estado (s) como o máximo da utilidade de cada ação possível, usando util_accao.
                # O parâmetro default=0.0 trata casos em que não há ações válidas.
                U[s] = max( [self.util_accao(s, a, Uant)  for a in self.__modelo.A(s)], default = 0.0)

                # Atualiza (delta) como o máximo entre o valor atual e a diferença absoluta entre a nova utilidade (U[s])
                # e a anterior (Uant[s]).
                delta = max(delta, abs(U[s] - Uant[s]) )

            # Verifica se a variação máxima é menor ou igual ao limiar de convergência, interrompendo o loop se
            # verdadeiro.
            if delta <= self.__delta_max: break

        # Retorna o dicionário de utilidades finais.
        return U

    # Calcula a utilidade esperada de uma ação em um estado, dada uma função de utilidade.
    #
    # Calcula ( U(s, a) = sum_{s' in suc(s, a)} T(s, a, s')[R(s, a, s') + gamma U(s')] ), conforme a equação de Bellman da matéria.
    def util_accao(self, s, a, U):

        T    = self.__modelo.T
        R    = self.__modelo.R
        suc  = self.__modelo.suc
        gama = self.__gama

        # Calcula a utilidade esperada da ação (a) no estado (s), somando, para cada estado sucessor ( s' \), o produto
        # da probabilidade de transição ( T(s, a, s') ) pelo valor ( R(s, a, s') + gamma U(s') ).
        return sum( T(s, a, sn) * ( R(s, a, sn) + gama * U[sn] ) for sn in suc(s, a) )

