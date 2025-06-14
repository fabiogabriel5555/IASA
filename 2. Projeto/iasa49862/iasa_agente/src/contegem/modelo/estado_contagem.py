from mod.estado import Estado

"""
Classe 'EstadoContagem', que representa um estado específico no contexto de um problema de contagem.

Esta classe herda da classe abstrata 'Estado' e encapsula um valor numérico que define o estado atual, 
servindo como uma representação simples para problemas onde o estado é caracterizado por um contador ou 
valor único (e.g., um número em problemas de contagem ou progressão).

A classe é usada para modelar estados em espaços de procura, permitindo a identificação única de cada 
estado com base no seu valor.
"""

class EstadoContagem(Estado):

    # Inicializa uma instância do estado de contagem com um valor específico.
    # Este metodo define o valor que caracteriza o estado, armazenando-o como um atributo da instância.
    # O valor é a informação principal que representa o estado no contexto do problema, como um número
    # numa sequência de contagem.
    def __init__(self, valor):
        # Armazena o valor fornecido como um atributo público da instância, permitindo acesso direto
        # para verificar ou manipular o estado.
        self.valor = valor


    # Devolve o valor que identifica unicamente o estado.
    # Este metodo é usado para comparar estados ou verificar se um estado é o objetivo, retornando
    # o valor característico do estado (neste caso, o próprio 'valor').
    # ATT: a identificação única de estados é essencial para gerir nós na procura e evitar redundâncias.
    def id_valor(self):
        # Retorna o atributo 'valor', que serve como a identidade única do estado no espaço de procura.
        return self.valor
