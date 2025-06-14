"""
    Esta classe é responsável pelo controlo reactivo de um agente, integrando percepções e comportamentos
    para produzir acções adequadas em tempo real.

    O controlo reactivo atua como o módulo central que processa as percepções vindas do ambiente
    e, com base num comportamento associado, devolve a acção a executar.

    O comportamento pode ser composto, integrando múltiplas reacções, e pode utilizar diferentes estratégias de selecção de acções,
    como hierarquia, prioridade ou combinação.

    A classe encapsula esse processo de forma simples e modular, sendo adequada para uso em agentes
    como o "Prospector" (exploração, aproximação a alvos, desvio de obstáculos).
"""

class ControloReact:

    # Recebe um objeto comportamento e armazena-o para ser utilizado durante o ciclo de perceção–ação.
    def __init__(self, comportamento):
        self.__comportamento = comportamento

    # Chama o metodo activar() do comportamento com a perceção atual e devolve a ação que o comportamento decidiu executar.
    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)
