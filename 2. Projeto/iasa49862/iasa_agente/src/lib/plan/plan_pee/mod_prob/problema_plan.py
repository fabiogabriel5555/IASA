from mod.problema import Problema

"""
    Classe 'ProblemaPlan', derivada de 'Problema', responsável por definir um problema de planeamento para um agente 
    autónomo.

    Esta classe representa um problema de planeamento no contexto de uma arquitetura deliberativa, especificando um 
    estado inicial, operadores de transição e um estado final (objetivo). Ela é usada para integrar o modelo do mundo 
    com algoritmos de procura, como `ProcuraCustoUnif`, permitindo a geração de planos que alcançam o estado final.

    A classe suporta o raciocínio prático ao definir a condição de objetivo, que verifica se um estado corresponde ao 
    estado final desejado, essencial para o processo cíclico de tomada de decisão (páginas 9 e 13 de 
    "13-arq-delib.pdf"). Ela é projetada para trabalhar com o `PlaneadorPEE`, que utiliza a estrutura do problema para 
    explorar o espaço de estados.
"""

class ProblemaPlan(Problema):

    # Inicializa uma instância do problema de planeamento com um modelo do mundo e um estado final.
    def __init__(self, modelo_plan, estado_final):

        # Chama o construtor da classe base `Problema`, passando o estado inicial obtido de `modelo_plan.obter_estado()`
        # e os operadores obtidos de `modelo_plan.obter_operadores()`, inicializando a estrutura do problema.
        super().__init__(modelo_plan.obter_estado(),  modelo_plan.obter_operadores())

        # Armazena o estado final fornecido no atributo privado `__estado_final`, que será usado para verificar a
        # condição de objetivo.
        self.__estado_final = estado_final

    # Metodo que verifica se um estado é o estado objetivo do problema.
    # Este metodo compara o estado fornecido com o estado final, retornando verdadeiro se forem iguais, indicando que o
    # objetivo foi alcançado.
    def objectivo(self, estado):

        # Compara o estado fornecido com o atributo privado `__estado_final` usando o operador de igualdade,
        # retornando True se forem idênticos, indicando que o objetivo foi alcançado.
        return estado == self.__estado_final