from abc import ABC, abstractmethod

"""
    A classe abstrata Estado é responsável por definir a estrutura base para a representação de 
    um estado.
    
    Um estado representa uma configuração ou situação específica de um sistema ou problema 
    durante o processo de resolução, sendo um elemento fundamental do modelo do problema. 
    
    Esta classe é projetada para suportar o domínio do problema, permitindo a exploração de 
    opções possíveis através de operadores de transição de estado.

    Cada estado deve ter uma identificação única para distinguir configurações no espaço de
    estados. 
"""

class Estado(ABC):

    # Metodo abstrato id_valor responsável por retornar um valor inteiro único representando a identificação do estado.
    # Este metodo é essencial para assegurar que cada estado no espaço de estados tenha uma identificação distinta,
    # permitindo a distinção entre diferentes configurações durante o processo de procura.
    @abstractmethod
    def id_valor(self):
        """Abstract Method"""


    # Sobrecarga do metodo `__hash__, que define o valor de hash de um objeto para utilização em estruturas de dados
    # baseadas em hash, como conjuntos (`set`) e dicionários (`dict`).
    #
    # Este metodo é sobrecarregado para implementar o estereótipo `<<hashable>>` garantindo que instâncias de `Estado`
    # possam ser usadas em estruturas que requerem unicidade de objetos.
    #
    # O valor de hash é calculado diretamente a partir do metodo `id_valor()`, que fornece um identificador único para
    # cada estado, conforme a necessidade de identificação única.
    #
    # A sobrecarga é necessária porque o  comportamento padrão de `__hash__` (baseado no endereço de memória do objeto)
    # não refletiria a semântica de unicidade do estado no contexto do espaço de estados, onde configurações idênticas
    # devem ter o mesmo hash, independentemente da instância.
    #
    # Este metodo retorna o valor de hash do estado, correspondente ao resultado de `id_valor()`.
    def __hash__(self):
        return self.id_valor()

    # Sobrecarga do metodo `__eq__`, que define o comportamento de comparação de igualdade entre dois objetos usando o
    # operador `==`.
    #
    # Este metodo é sobrecarregado para permitir a comparação semântica entre instâncias de `Estado`, considerando dois
    # estados iguais se tiverem o mesmo valor de hash, derivado de `id_valor()`.
    #
    # A sobrecarga é necessária porque o comportamento padrão de `__eq__` (comparação de identidade de objetos pelo
    # endereço de memória) não refletiria a igualdade de configurações no espaço de estados, onde estados com a mesma
    # configuração devem ser considerados equivalentes, independentemente de serem instâncias distintas.
    #
    # Este metodo verifica se `other` é uma instância de `Estado` para evitar comparações inválidas.
    # Retorna `True` se os estados forem iguais (mesmo valor de hash), `False` caso contrário ou se `other` não for
    # uma instância de `Estado`.
    def __eq__(self, other):
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()
