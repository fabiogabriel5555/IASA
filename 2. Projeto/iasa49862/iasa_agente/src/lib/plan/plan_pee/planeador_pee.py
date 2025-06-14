from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.planeador import Planeador
from plan.plano_pee import PlanoPEE

"""
    Classe 'PlaneadorPEE', derivada de 'Planeador', que implementa um planeador baseado em procura em espaços de estados 
    (PEE) para gerar planos de ação.

    Esta classe utiliza um mecanismo de procura informado, especificamente 'ProcuraAA' (A*), para resolver problemas de 
    planeamento. O planeador recebe um modelo de planeamento ('modelo_plan') e objetivos, formulando um problema de 
    planeamento ('ProblemaPlan') e utilizando uma heurística de distância ('HeurDist') para guiar a procura. 
    
    O resultado é um plano ('PlanoPEE') que especifica a sequência de ações para alcançar o objetivo.

    A classe é projetada para integrar-se com agentes deliberativos e simuladores, suportando planeamento automático 
    em cenários de tomada de decisão sequencial.  
"""

class PlaneadorPEE(Planeador):

    # Inicializa uma instância do planeador PEE.
    def __init__(self):
        # Define o mecanismo de procura como uma instância de 'ProcuraAA'
        self.__mec_pee  = ProcuraAA()


    # Gera um plano para alcançar um objetivo num modelo de planeamento.
    #
    # Formula um problema de planeamento com base no modelo e no primeiro objetivo fornecido, utilizando uma heurística
    # de distância para guiar a procura A*.
    #
    # Retorna um plano ('PlanoPEE') se a solução for encontrada, ou None caso contrário.
    #
    # - modelo_plan: Modelo de planeamento que fornece estados e operadores.
    # - objectivos: Lista de estados objetivo, onde o primeiro é usado como estado final.
    def planear(self, modelo_plan, objectivos):

        # Seleciona o primeiro estado objetivo da lista como o estado final para o problema de planeamento.
        estado_final = objectivos[0]

        # Instancia um problema de planeamento com o modelo de planeamento e o estado final, definindo o espaço
        # de estados e o objetivo a alcançar.
        problema = ProblemaPlan(modelo_plan, estado_final)

        # Instancia uma heurística de distância baseada no estado final, que estima o custo restante para alcançar
        # o objetivo, guiando a procura A*.
        heuristica = HeurDist(estado_final)

        # Executa a procura A* no problema usando o mecanismo de procura ('ProcuraAA') e a heurística, retornando
        # uma solução (sequência de ações) se encontrada.
        solucao = self.__mec_pee.procurar(problema, heuristica)

        # Verifica se uma solução foi encontrada; se sim, retorna um plano PEE baseado na solução.
        if solucao:
            # Cria e retorna uma instância de 'PlanoPEE' com a solução, encapsulando a sequência de ações para
            # alcançar o estado final.
            return PlanoPEE(solucao)
