from contegem.modelo.estado_contagem import EstadoContagem
from contegem.modelo.operador_incremento import OperadorIncremento
from mod.problema import Problema

"""
Classe 'ProblemaContagem', que define um problema de contagem no contexto de procura em espaços de estados.

Esta classe herda da classe abstrata 'Problema' e modela um problema onde o objetivo é alcançar ou ultrapassar 
um valor final a partir de um valor inicial, aplicando operadores de incremento. Cada operador adiciona um 
montante específico ao valor atual, e o estado é representado por uma instância de 'EstadoContagem'.

O problema é configurado com um estado inicial, uma lista de operadores de incremento e um valor final que 
define o objetivo.
"""

class ProblemaContagem(Problema):

    # Inicializa uma instância do problema de contagem com um valor inicial, um valor final e uma lista de incrementos.
    # Este metodo configura o estado inicial e os operadores do problema, chamando o construtor da classe base
    # 'Problema', e armazena o valor final que define o objetivo.
    def __init__(self, valor_inicial, valor_final, incrementos):
        # Chama o construtor da classe base 'Problema', passando um estado inicial (instância de
        # 'EstadoContagem' com 'valor_inicial') e uma lista de operadores (instâncias de
        # 'OperadorIncremento' criadas para cada incremento na lista 'incrementos').
        super().__init__( EstadoContagem(valor_inicial), [OperadorIncremento(incremento) for incremento in incrementos])

        # Armazena o valor final como um atributo privado, que será usado para verificar se um estado
        # satisfaz o objetivo do problema.
        self.__valor_final = valor_final


    # Verifica se um estado satisfaz o objetivo do problema.
    # Este metodo testa se o valor do estado é maior ou igual ao valor final definido, indicando
    # que o objetivo foi alcançado.
    # ATT: a função objetivo determina se um estado é uma
    # solução, terminando a procura quando satisfeita.
    def objectivo(self, estado):
        # Compara o valor do estado (obtido via 'id_valor') com o valor final do problema,
        # retornando True se o estado satisfizer ou ultrapassar o objetivo.
        if estado.id_valor() >= self.__valor_final:
            return True
        # Retorna False se o valor do estado for inferior ao valor final, indicando que o
        # objetivo ainda não foi alcançado.
        else:
            return False