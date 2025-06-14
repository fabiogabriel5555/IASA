from pdm.mec_util import MecUtil

"""
    Classe 'PDM', responsável por resolver um Processo de Decisão de Markov (PDM) calculando utilidades de estados e a 
    política ótima associada.

    Esta classe encapsula a lógica para resolver um PDM, utilizando o algoritmo de iteração de valor implementado por 
    'MecUtil' para calcular as utilidades de estados (U(s)) e determinar a política ótima.
    
    Ela opera sobre um modelo PDM, como 'ModeloPDM' ou 'ModeloAmbiente7x1', e utiliza um fator de desconto (gamma) e um 
    limiar de convergência (delta_{max}) para controlar a iteração de valor.
"""


class PDM:

    # Inicializa uma instância de PDM.
    def __init__(self, modelo, gama, delta_max):

        # Armazena o modelo PDM como um atributo privado
        self.__modelo = modelo

        # Cria uma instância de 'MecUtil' com o modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)


    # Calcula a política ótima com base nas utilidades fornecidas.
    #
    # Determina a política ótima para cada estado, selecionando a ação que maximiza a utilidade esperada ( U(s, a) ),
    # calculada por 'MecUtil.util_accao'.
    #
    # Retorna um dicionário mapeando estados para suas ações ótimas.
    def politica(self, U):

        # Obtém a função que retorna o conjunto de estados do modelo.
        S = self.__modelo.S

        # Obtém a função que retorna o conjunto de ações possíveis para um estado.
        A = self.__modelo.A

        # Obtém o metodo 'util_accao' de 'MecUtil' para calcular a utilidade esperada de uma ação.
        util_accao = self.__mec_util.util_accao

        # Cria um dicionário de política, mapeando cada estado ( s ) para a ação que maximiza ( U(s, a) ).
        #
        # A função 'max' usa 'key = lambda a: util_accao(s, a, U)' para selecionar a ação com maior utilidade esperada.
        #
        # A condição 'if A(s)' exclui estados sem ações válidas.
        pol = {s      : max( A(s), key = lambda a: util_accao(s, a, U) ) for s in S() if A(s) }

        # Retorna o dicionário de política ótima.
        return pol


    # Metodo resolver, responsável por calcular utilidades e a política ótima.
    #
    # Retorna um tuplo que contem o dicionário de utilidades e o dicionário de política.
    def resolver(self):

        # Calcula as utilidades dos estados usando o metodo 'utilidade' de 'MecUtil', baseado na iteração de valor.
        U = self.__mec_util.utilidade()

        # Calcula a política ótima com base nas utilidades obtidas, usando o metodo 'politica'.
        pol = self.politica(U)

        # Retorna um tuplo que contem o dicionário de utilidades e o dicionário de política.
        return U, pol