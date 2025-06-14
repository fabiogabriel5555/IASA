from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

"""
    Classe 'PassoSolucao', responsável por representar um passo individual numa solução.

    Um passo de solução encapsula um estado do problema e o operador que foi aplicado para chegar a esse estado,
    servindo como um elemento básico na construção de uma sequência de ações que leva do estado inicial ao estado
    objetivo.

    Esta classe é usada para descrever cada transição na solução final, permitindo rastrear o percurso resolvido.
"""

@dataclass
class PassoSolucao():

    # Atributo que armazena o estado associado ao passo da solução.
    # Representa uma configuração específica do problema atingida após a aplicação do operador.
    estado: Estado

    # Atributo que armazena o operador que gerou o estado atual.
    # Representa a ação ou transição que foi aplicada para alcançar o estado.
    operador: Operador