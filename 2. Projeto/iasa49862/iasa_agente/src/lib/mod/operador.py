from abc import ABC, abstractmethod

"""
    A classe abstrata Operador é responsável por definir a estrutura base para um operador.

    Um operador representa uma ação ou transformação que pode ser aplicada a um estado, gerando um novo estado (estado 
    sucessor) no espaço de estados. 
    
    É um componente essencial do modelo do problema, permitindo a simulação prospectiva das transições de estado 
    necessárias para explorar opções e atingir o estado objetivo. Além disso, o operador inclui a capacidade de avaliar 
    o custo associado a cada transição, o que é crucial para estratégias de procura informadas, como a procura de custo 
    uniforme.
"""

class Operador(ABC):

    # Metodo abstrato aplicar responsável por aplicar o operador a um estado, gerando um novo estado sucessor.
    #
    # Este metodo reflete a definição de operador como uma ação que transforma um estado em outro. A aplicação do
    # operador é o mecanismo pelo qual o sistema simula as transições no espaço de estados, permitindo a exploração
    # de opções possíveis para alcançar o estado objetivo.
    #
    # Este metodo tem como argumento o estado atual ao qual o operador será aplicado, e tem como retorno o estado
    # sucessor resultante da aplicação do operador.
    @abstractmethod
    def aplicar(self, estado):
        """Abstract Method"""

    # Metodo abstrato custo responsável por calcular o custo de transição entre um estado e o seu estado sucessor após
    # a aplicação do operador.
    #
    # Este metodo é essencial para avaliar o custo associado à execução de uma ação. O custo pode representar recursos
    # necessários, distância, tempo ou outra métrica relevante, dependendo do domínio do problema.
    @abstractmethod
    def custo(self, estado, estado_suc):
        """Abstract Method"""
