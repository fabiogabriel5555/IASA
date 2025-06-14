from pdm.pdm import PDM
from pdm.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from pdm.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

"""
    Classe 'PlaneadorPDM', derivada de 'Planeador', que implementa um planeador baseado em Processos de Decisão de 
    Markov (PDM) para gerar planos de ação.

    Esta classe utiliza a resolução de um PDM, através da classe 'PDM' e do algoritmo de iteração de valor, para 
    calcular utilidades ( U(s) ) e uma política ótima ( pi^*(s) ), que são encapsuladas num plano ('PlanoPDM'). 
    
    O planeador opera sobre um modelo de planeamento ('modelo_plan') adaptado para um PDM via 'ModeloPDMPlan', 
    considerando objetivos e utilizando um fator de desconto ( gamma ) e um limiar de convergência ( delta_{max} ) 
    para controlar a iteração de valor. 
    
    O planeador é projetado para integrar-se com agentes deliberativos e simuladores, suportando tomada de decisão 
    sequencial sob incerteza. 
"""

class PlaneadorPDM(Planeador):

    # Inicializa uma instância do planeador PDM com parâmetros de iteração de valor.
    def __init__(self, gama = 0.95, delta_max = 1):
        self.__gama = gama           # Armazena o fator de desconto como um atributo privado.
        self.__delta_max = delta_max # Armazena o limiar de convergência como um atributo privado.


    # Gera um plano baseado na resolução de um PDM.
    #
    # Cria um modelo PDM a partir do modelo de planeamento e objetivos, resolve o PDM para obter utilidades e
    # política ótima, e retorna um plano ('PlanoPDM') que encapsula esses resultados.
    #
    # - modelo_plan: Modelo de planeamento que fornece estados e operadores.
    # - objectivos: Conjunto ou lista de estados objetivo.
    def planear(self, modelo_plan, objectivos):

        # Cria um modelo PDM adaptado a partir do modelo de planeamento e objetivos, utilizando 'ModeloPDMPlan'
        # para integrar a estrutura de PDM.
        modelo_pdm_plan = ModeloPDMPlan(modelo_plan, objectivos)

        # Instancia um resolvedor de PDM com o modelo adaptado, o fator de desconto e o limiar de convergência,
        # para calcular utilidades e política.
        pdm = PDM(modelo_pdm_plan, self.__gama, self.__delta_max)

        # Resolve o PDM, obtendo as utilidades dos estados ( U(s) ) e a política ótima ( pi^*(s) ) através do metodo
        # 'resolver', que utiliza iteração de valor.
        U, pol = pdm.resolver()

        # Cria um plano PDM com as utilidades e a política obtidas, encapsulando a solução do PDM para uso por agentes
        # ou simuladores.
        plan_pdm = PlanoPDM(U, pol)

        # Retorna o plano PDM gerado.
        return plan_pdm