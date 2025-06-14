from pdm.modelo.modelo_pdm import ModeloPDM
from pdm.pdm import PDM

"""
    Classe 'ModeloAmbiente7x1', derivada de 'ModeloPDM', que define um modelo de ambiente unidimensional para um Processo 
    de Decisão de Markov (PDM) com 7 estados.

    Esta classe representa um ambiente de grade linear 7x1, onde um agente pode mover-se para a esquerda ('←') ou para 
    a direita ('→') entre estados numerados de 1 a 7. 
    
    O modelo especifica os estados, ações, probabilidades de transição determinísticas e recompensas, conforme a 
    estrutura de um PDM. O ambiente é projetado para tomada 
    de decisão sequencial sob incerteza, com transições determinísticas (probabilidade 0 ou 1) e recompensas que 
    incentivam alcançar o estado 7 (+1) enquanto penalizam certas transições (e.g., -1 de 2 para 1).

    O modelo suporta algoritmos de iteração de valor para calcular utilidades, onde a utilidade de um estado é definida 
    como ( U(s) = max_a U(s, a) ), e a utilidade de uma ação é ( U(s, a) = sum_{s' in suc(s)} T(s, a, s')
    [R(s, a, s') + gamma U(s')] ). 

"""

class ModeloAmbiente7x1(ModeloPDM):

    # Inicializa uma instância do modelo de ambiente 7x1 com estados, ações, transições e recompensas.
    def __init__(self):

        # Define o conjunto de estados como uma lista de inteiros de 1 a 7, representando as posições na grade linear
        self.__S = [1, 2, 3, 4, 5, 6, 7]

        # Define o conjunto de ações como uma lista de strings, onde '←' representa movimento para a esquerda e '→'
        # representa movimento para a direita.
        self.__A = ['<', '>']

        # Define o modelo de transição como um dicionário, onde cada chave é uma tupla (estado, ação, estado_sucessor)
        # e o valor é a probabilidade de transição. As transições são determinísticas (0 ou 1), conforme a tabela de
        # transição, onde cada ação leva a um único estado sucessor com probabilidade 1.
        self.__T = {
            (1, '<', 1): 0, (1, '>', 2): 0, # Estado 1: não move para esquerda (inválido), pode mover para direita.
            (2, '<', 1): 1, (2, '>', 3): 1, # Estado 2: move para esquerda (1) ou direita (3) com probabilidade 1.
            (3, '<', 2): 1, (3, '>', 4): 1, # Estado 3: move para esquerda (2) ou direita (4) com probabilidade 1.
            (4, '<', 3): 1, (4, '>', 5): 1, # Estado 4: move para esquerda (3) ou direita (5) com probabilidade 1.
            (5, '<', 4): 1, (5, '>', 6): 1, # Estado 5: move para esquerda (4) ou direita (6) com probabilidade 1.
            (6, '<', 5): 1, (6, '>', 7): 1, # Estado 6: move para esquerda (5) ou direita (7) com probabilidade 1.
            (7, '<', 6): 0, (7, '>', 7): 0, # Estado 7: não move para direita (inválido), pode mover para esquerda.
        }

        # Define o modelo de recompensa como um dicionário, onde cada chave é uma tupla (estado, ação, estado_sucessor)
        # e o valor é a recompensa associada. As recompensas seguem a tabela de transição , com penalidade (-1)
        # para mover de 2 para 1, recompensa (+1) para mover de 6 para 7, e 0 para outras transições válidas.
        self.__R = {
            (1, '<', 1):  0, (1, '>', 2): 0, # Estado 1: sem recompensa para transições válidas ou inválidas.
            (2, '<', 1): -1, (2, '>', 3): 0, # Estado 2: penalidade (-1) para esquerda, sem recompensa para direita.
            (3, '<', 2):  0, (3, '>', 4): 0, # Estado 3: sem recompensa para transições válidas.
            (4, '<', 3):  0, (4, '>', 5): 0, # Estado 4: sem recompensa para transições válidas.
            (5, '<', 4):  0, (5, '>', 6): 0, # Estado 5: sem recompensa para transições válidas.
            (6, '<', 5):  0, (6, '>', 7): 1, # Estado 6: recompensa (+1) para alcançar o estado 7.
            (7, '<', 6):  0, (7, '>', 7): 0, # Estado 7: sem recompensa para transições válidas ou inválidas.
        }

        # Define um dicionário de transições válidas, mapeando (estado, ação) para o estado sucessor, apenas para estados
        # não terminais (excluindo 1 e 7), com base nas transições com probabilidade 1.
        self.__transicoes = {(s, a): sn for (s, a, sn) in self.__T if s not in [1, 7]}


    # Retorna o conjunto de estados do modelo.
    def S(self):
        # Retorna o conjunto de estados armazenado.
        return self.__S


    # Retorna o conjunto de ações possíveis num dado estado.
    def A(self, s):
        # Devolve a lista de ações disponíveis no estado s. Para os estados 1 e 7 (bordas), retorna uma lista vazia,
        # indicando que não há ações válidas; para outros estados, retorna todas as ações.
            # - s: Estado para o qual se deseja o conjunto de ações.
        return self.__A if s not in [1, 7] else []


    # Retorna a probabilidade de transição entre estados.
    def T(self, s, a, sn):
        # Devolve ( T(s, a, s')), a probabilidade de transitar do estado ( s ) para ( s' ) ao executar a ação ( a ),
        # conforme o dicionário de transições __T.
            # - s: Estado atual.
            # - a: Ação executada.
            # - sn: Estado sucessor.
        return self.__T[(s, a, sn)]


    # Retorna a recompensa associada a uma transição.
    def R(self, s, a, sn):
        # Devolve ( R(s, a, s') ), a recompensa esperada ao transitar do estado ( s ) para ( s' ) via ação ( a ).
            # - s: Estado atual.
            # - a: Ação executada.
            # - sn: Estado sucessor.
        return self.__R[(s, a, sn)]


    # Retorna o conjunto de estados sucessores para uma ação num estado.
    #
    # Devolve ( suc(s, a) ), a lista de estados ( s' ) alcançáveis a partir do estado ( s ) ao executar a ação ( a ),
    # com base no dicionário de transições válidas __transicoes.
        # - s: Estado atual.
        # - a: Ação executada.
    def suc(self, s, a):

        # Obtém o estado sucessor para o tuplo (s, a) no dicionário de transições, se existir.
        sn = self.__transicoes.get((s, a))

        # Retorna uma lista com o estado sucessor se ele existir; caso contrário, retorna uma lista vazia.
        return [sn] if sn else []



# Bloco para testar a resolução do ambiente 7x1 usando a classe 'PDM'.
if __name__ == "__main__":

    # Instancia o modelo do ambiente 7x1
    modelo = ModeloAmbiente7x1()

    # Instancia um resolvedor de PDM com o modelo, fator de desconto (gamma = 0.5) e limiar de convergência (delta_{max}
    # = 0.1 ), que controla a precisão da iteração de valor.
    pdm = PDM(modelo, 0.5, 0.1)

    # Resolve o PDM, calculando as utilidades dos estados ( U ) e a política ótima usando o metodo 'resolver' da classe
    # 'PDM', que invoca 'MecUtil' para iteração de valor.
    U, pol = pdm.resolver()

    # PRINTES
    print("Utilidade: ")
    print(U)
    print("Politica: ")
    print(pol)

