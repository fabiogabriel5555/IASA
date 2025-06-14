from abc import ABC, abstractmethod
from .comportamento import Comportamento

"""
Esta classe (ComportComp) é uma classe abstrata que representa um comportamento composto,
isto é, um conjunto de subcomportamentos que podem ser ativados em conjunto.

Herda da classe base Comportamento e define a estrutura necessária para agregação e coordenação
de múltiplos comportamentos.

Um comportamento composto realiza de forma modular e coesa o encapsulamento das reações internas.

É necessário um mecanismo de seleção de ação para determinar qual ação será executada com base nas
respostas dos comportamentos internos.

Ecistem 3 mecanismos de coordenação:

    Hierarquia  
    
    Prioridade
    
    Combinação
"""

class ComportComp(Comportamento):

    # Inicializa o comportamento composto com a lista de subcomportamentos fornecida.
    def __init__(self, comportamentos):

        self.__comportamentos = comportamentos

    # Ativa todos os subcomportamentos com base na perceção recebida.
    # Para cada subcomportamento, chama o m3todo activar().
    # Se o subcomportamento devolver uma ação (diferente de None), a ação é armazenada.
    # Após recolher todas as ações possíveis, a função seleccionar_accao é chamada para escolher qual ação executar.
    def activar(self, percepcao):

        accoes = []
        for comportamento in self.__comportamentos:

            accao = comportamento.activar(percepcao)

            # Aqui, não pudemos usar 'if accão != None' porque ação não é um valor, mas sim uma marca,
            # então, pra isso usa-se o 'is', que foi criado explicitamente para marcas
            if accao is not None:
                accoes.append(accao)

            # Aqui, o python por omissão converte uma lista vazia para false, o que permite ter um if simples como este
            if accoes:
                return self.seleccionar_accao(accoes)

    # Metodo abstrato que define a política de seleção de ação entre várias ações propostas
    # pelos subcomportamentos internos.
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """Metodo abstrato 'seleccionar_accao' """
