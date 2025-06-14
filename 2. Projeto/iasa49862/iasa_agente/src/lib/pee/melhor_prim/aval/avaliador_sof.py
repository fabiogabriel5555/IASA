from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
    Classe 'AvaliadorSof', derivada de 'AvaliadorHeur', responsável por calcular a prioridade de nós para o algoritmo de
    procura gulosa (ou 'só heurística').

    Esta classe implementa a função de avaliação característica da procura gulosa, onde a prioridade de um nó é dada
    exclusivamente pela estimativa heurística h(n), que representa o custo estimado do estado atual até o estado 
    objetivo. 
    
    Diferentemente da procura A*, que combina g(n) (custo acumulado) com h(n), ou da procura de custo uniforme, que usa 
    apenas g(n), a procura gulosa ignora o custo acumulado e foca apenas na heurística, priorizando nós que parecem mais 
    próximos do objetivo.

    A classe utiliza uma heurística fornecida pela classe base 'AvaliadorHeur', que deve implementar o método 
    'h(estado)'.
    No entanto, a procura gulosa não garante optimalidade, mesmo com uma heurística admissível, pois não considera o 
    custo real do percurso. É útil em problemas onde a heurística é altamente informativa, como no puzzle de 8 peças 
    com a distância de Manhattan, ou em navegação autónoma com a distância euclidiana.

    A classe é usada com uma fronteira de prioridade (PriorityQueue) para ordenar nós com base em h(n), onde nós com menor
    h(n) são expandidos primeiro.
"""

class AvaliadorSof(AvaliadorHeur):

    # Metodo 'prioridade', responsável por calcular a prioridade de um nó para o algoritmo de procura gulosa.
    #
    # Este metodo implementa a função de avaliação h(n), que é a estimativa heurística do custo restante do estado atual
    # até o objetivo, calculada pela heurística fornecida pela classe base 'AvaliadorHeur'. A prioridade determina a
    # ordem de expansão dos nós na fronteira, com nós de menor h(n) sendo expandidos primeiro, conforme o funcionamento
    # da procura gulosa.
    #
    # A procura gulosa é rápida, mas não garante optimalidade, pois ignora o custo acumulado g(n), podendo levar a
    # soluções subótimas ou até falhar em encontrar uma solução em certos casos.
    def prioridade(self, no):
        return self.heuristica.h(no.estado)