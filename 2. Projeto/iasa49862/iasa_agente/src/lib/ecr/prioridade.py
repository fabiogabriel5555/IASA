from .comport_comp import ComportComp

"""
Esta classe (Prioridade) herda de ComportComp, o que significa que é um comportamento composto.

Implementa a política de seleção de ação com base na maior prioridade entre as ações retornadas 
pelos subcomportamentos.

Cada ação deve ter um atributo "prioridade" que representa a sua importância relativa no momento da execução.

Um comportamento composto requer um mecanismo de seleção de ação.
A classe Prioridade concretiza isso com um critério que avalia valores de prioridade associados às ações
"""

class Prioridade(ComportComp):

    # Seleciona a ação a executar com base na maior prioridade.
    # Percorre todas as ações propostas pelos subcomportamentos ativos e retorna aquela que tiver o valor de prioridade mais elevado.
    def seleccionar_accao(self, accoes):

        if accoes:
            return max(accoes, key = lambda a:a.prioridade)

