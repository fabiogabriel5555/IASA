from .comport_comp import ComportComp

"""

A classe Hierarquia é uma especialização de um comportamento composto, ou seja, é um ComportComp 
que organiza os seus subcomportamentos segundo uma hierarquia de prioridades fixas.

Um comportamento pode ser composto por outros comportamentos. Para isso, é necessário um mecanismo
de seleção de ação que escolha qual ação executar com base nas respostas dos subcomportamentos.

A classe Hierarquia é esse mecanismo: ela implementa uma política de seleção baseada em prioridade.

Tipos de coordenação de comportamentos compostos:
    
    Hierarquia de subsunção: Os comportamentos estão organizados numa hierarquia fixa, onde os de nível superior podem suprimir ou substituir os inferiores.
    Seleção por prioridade fixa: As ações são selecionadas de acordo com a prioridade associada, que pode ser fixa e determinada pela ordem dos subcomportamentos.

"""
class Hierarquia(ComportComp):

    # Este metodo recebe uma lista de ações propostas pelos subcomportamentos internos.
    # Implementa uma política hierárquica, retornando sempre a primeira ação da lista,ou seja, a do comportamento com maior prioridade
    def seleccionar_accao(self, accoes):

        if accoes:
            return accoes[0]
