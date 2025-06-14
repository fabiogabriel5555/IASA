from plan.plano import Plano

"""
    Classe 'PlanoPDM', derivada de 'Plano', que define um plano baseado numa política ótima para um Processo de Decisão 
    de Markov (PDM).

    Esta classe implementa um plano que utiliza a política ótima ( pi^*(s) ) e as utilidades dos estados ( U(s) ) 
    calculadas por um resolvedor de PDM. 
    
    A política mapeia estados para ações ótimas, permitindo que um agente tome decisões sequenciais num ambiente PDM.
    
    O plano é projetado para ser usado em arquiteturas deliberativas e planeamento automático com 'PlaneadorPEE'.

    A classe armazena as utilidades e a política fornecidas, permitindo obter a ação ótima para um dado estado e, 
    potencialmente, visualizar o plano.
"""

class PlanoPDM(Plano):

    # Inicializa uma instância do plano PDM com utilidades e política.
    # Armazena o dicionário de utilidades como um atributo privado.
    # Armazena o dicionário de política como um atributo privado.
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica  = politica


    # Obtém a ação ótima para um dado estado.
    #
    # Retorna a ação associada ao estado na política ótima ( pi^*(s) ), se existir. Caso o estado não esteja mapeado na
    # política, retorna None.
    #
    # Este metodo suporta a execução do plano por um agente deliberativo.
    #
    # - estado: Estado atual para o qual se deseja a ação.
    def obter_accao(self, estado):
        # Verifica se o estado está presente no dicionário de política e retorna a ação correspondente, se
        # existir; caso contrário, retorna None.
        if self.__politica.get(estado) :
            return self.__politica.get(estado)


    # Deve exibir o plano numa interface de visualização.
    def mostrar(self, vista):

        if self.__politica:
            # Mostrar Utilidade
            for (estado, valor) in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
            # Mostrar política
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang)
