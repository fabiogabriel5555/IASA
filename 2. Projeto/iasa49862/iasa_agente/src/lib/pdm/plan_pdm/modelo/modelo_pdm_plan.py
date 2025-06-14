from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

"""
    Classe 'ModeloPDMPlan', derivada de 'ModeloPDM' e 'ModeloPlan', que integra um modelo de planeamento com um 
    Processo de Decisão de Markov (PDM).

    Esta classe combina a estrutura de um PDM. 
    
    Representa um ambiente onde um agente toma decisões sequenciais com base em estados, ações (operadores), transições 
    determinísticas e recompensas. 
    
    O modelo suporta algoritmos de iteração de valor para calcular utilidades ( U(s) = max_a U(s, a) ) e políticas 
    ótimas ( pi^*(s) = argmax_a U(s, a) ).

    Os estados e ações são obtidos do modelo de planeamento ('modelo_plan'), enquanto as transições são construídas 
    dinamicamente aplicando operadores aos estados, e as recompensas atribuem 'rmax' para alcançar estados objetivo, 
    com 0 para outras transições válidas. 
"""

class ModeloPDMPlan(ModeloPDM, ModeloPlan):

    # Inicializa uma instância do modelo PDM-plan com um modelo de planeamento, objetivos e recompensa máxima.
    def __init__(self, modelo_plan, objectivos, rmax = 1000):

        self.__rmax       = rmax           # Armazena a recompensa máxima como atributo privado.
        self.__objectivos = objectivos     # Armazena os estados objetivo como atributo privado.
        self.__modelo_plan  = modelo_plan  # Armazena o modelo de planeamento como atributo privado.

        # Inicializa um dicionário vazio para armazenar transições válidas, mapeando (estado, ação) para estado sucessor.
        self.__transicoes = { }

        # Percorre todos os estados obtidos do modelo de planeamento.
        for s in self.obter_estados():

            # Itera sobre todos os operadores (ações) disponíveis no modelo de planeamento.
            for a in self.obter_operadores():

                # Aplica o operador ao estado atual, obtendo o estado sucessor, se válido.
                sn = a.aplicar(s)

                # Se o estado sucessor existir, armazena a transição no dicionário de transições.
                if sn:
                    self.__transicoes[(s, a)] = sn


    # Delega ao modelo de planeamento o ( obter_estado ).
    def obter_estado(self):
        # Chama o metodo 'obter_estado' do modelo de planeamento para devolver o estado atual.
        return self.__modelo_plan.obter_estado()


    # Delega ao modelo de planeamento o ( obter_estados ).
    def obter_estados(self):
        # Chama o metodo 'obter_estados' do modelo de planeamento para devolver todos os estados.
        return self.__modelo_plan.obter_estados()


    # Delega ao modelo de planeamento o ( obter_operadores ).
    def obter_operadores(self):
        # Chama o metodo 'obter_operadores' do modelo de planeamento para devolver todos os operadores.
        return self.__modelo_plan.obter_operadores()


    # Retorna o conjunto de estados, obtido via 'obter_estados' do modelo de planeamento.
    def S(self):
        # Retorna o conjunto de estados delegando para 'obter_estados'.
        return self.obter_estados()


    # Retorna o conjunto de ações disponíveis num dado estado.
    #
    # Devolve todos os operadores (ações) disponíveis, independentemente do estado, assumindo que todas as ações
    # são aplicáveis em todos os estados, conforme definido pelo modelo de planeamento.
    #
    # - s: Estado para o qual se deseja o conjunto de ações (não utilizado, pois as ações são independentes do estado).
    def A(self, s):
        # Retorna o conjunto de operadores delegando para 'obter_operadores'.
        return self.obter_operadores()


    # Retorna a probabilidade de transição entre estados.
    #
    # Devolve ( T(s, a, sn) ), a probabilidade de transitar do estado ( s ) para ( sn ) ao executar a ação ( a ). As
    # transições são determinísticas (0 ou 1).
    #
    # Consulta o dicionário de transições para verificar se ( sn ) é o sucessor esperado.
    #
    # - s: Estado atual.
    # - a: Ação (operador) executada.
    # - sn: Estado sucessor.
    def T(self, s, a, sn):

        # Obtém o estado sucessor armazenado no dicionário de transições para a tupla (s, a), se existir.
        sn = self.__transicoes.get( (s, a) )

        # Retorna 1.0 se o estado sucessor especificado for igual ao esperado, 0.0 caso contrário, refletindo
        # transições determinísticas.
        return 1.0 if sn else 0.0


    # Retorna a recompensa associada a uma transição.
    #
    # Devolve ( R(s, a, sn) ), a recompensa esperada ao transitar do estado ( s ) para ( sn ) via ação ( a ).
    # Atribui 'rmax' se o estado sucessor for um objetivo, 0 para qualquer outra transição válida, simplificando a
    # estrutura de recompensas.
    #
    # - s: Estado atual.
    # - a: Ação (operador) executada.
    # - sn: Estado sucessor.
    def R(self, s, a, sn):

        # Retorna 'rmax' se o estado sucessor for um objetivo, 0 caso contrário.
        return self.__rmax if sn in self.__objectivos else 0.0


    # Retorna o conjunto de estados sucessores para uma ação num estado.
    #
    # Devolve ( suc(s, a) ), a lista de estados ( sn ) alcançáveis a partir do estado ( s ) ao executar a ação ( a ).
    #
    # Como as transições são determinísticas, retorna uma lista com um único estado sucessor, se válido, ou uma lista
    # vazia caso contrário.
    #
    # - s: Estado atual.
    # - a: Ação (operador) executada.
    def suc(self, s, a):

        # Obtém o estado sucessor para a tupla (s, a) no dicionário de transições, se existir.
        sn = self.__transicoes.get((s, a))

        # Retorna uma lista contendo o estado sucessor se ele existir; caso contrário, retorna uma lista vazia.
        return [sn] if sn else []