"""
Esta classe (Resposta) encapsula a ação concreta que será devolvida ao agente quando uma reação for ativada.

Esta classe:

    Define a prioridade da ação com base na intensidade do estímulo detetado.

    Devolve essa ação para ser executada.

Resposta: representa a geração de uma resposta a um estímulo. É ativada com a perceção e intensidade, e pode influenciar a prioridade da ação.
"""


class Resposta:
    def __init__(self, accao = None):
        self._accao = accao

    # Este metodo ativa a resposta associada, atribuindo à ação uma prioridade correspondente à intensidade do estímulo detetado.
    # Retorna a ação que deverá ser executada.
    def activar(self, percepcao, intensidade = 0):

        if percepcao is not None:

            self._accao.prioridade = intensidade

        return self._accao



