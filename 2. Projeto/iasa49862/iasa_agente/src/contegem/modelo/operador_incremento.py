from contegem.modelo.estado_contagem import EstadoContagem
from mod.operador import Operador

"""
Classe 'OperadorIncremento', que representa um operador de incremento no contexto de um problema de contagem.

Esta classe herda da classe abstrata 'Operador' e define uma operação que incrementa o valor de um estado 
de contagem por um montante específico, gerando um novo estado. É usada para modelar transições em problemas 
onde o estado é um valor numérico que progride através de incrementos.

O operador também calcula o custo da transição, que é proporcional ao quadrado do incremento, permitindo 
a integração com estratégias de procura como a procura de custo uniforme.
"""

class OperadorIncremento(Operador):

    # Inicializa uma instância do operador de incremento com um valor de incremento específico.
    # Este metodo define o montante pelo qual o valor de um estado será aumentado quando o operador for aplicado.
    def __init__(self, incremento):
        # Armazena o valor de incremento como um atributo público da instância, permitindo
        # acesso para aplicar a transição e calcular o custo.
        self.incremento = incremento


    # Aplica o operador a um estado, gerando um novo estado com o valor incrementado.
    # Este metodo adiciona o valor de incremento ao valor do estado atual, criando uma nova
    # instância de 'EstadoContagem' com o resultado.
    # ATT: o operador define como um estado é transformado
    # em um estado sucessor no espaço de procura.
    def aplicar(self, estado):
        return EstadoContagem( estado.valor + self.incremento )

    # Calcula o custo de transição entre dois estados.
    # Este metodo retorna o custo associado à aplicação do operador, definido como o
    # quadrado do valor de incremento, que pode refletir uma penalidade proporcional à
    # magnitude da transição.
    # ATT: o custo é usado em estratégias como a
    # procura de custo uniforme para priorizar caminhos com menor custo acumulado.
    def custo(self, estado, estado_suc):
        # Retorna o quadrado do valor de incremento, representando o custo da transição
        # independentemente dos estados fornecidos, já que o custo depende apenas do operador.
        return self.incremento ** 2