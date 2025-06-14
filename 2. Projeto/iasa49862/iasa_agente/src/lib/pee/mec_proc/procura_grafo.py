from abc import ABC, abstractmethod
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe abstrata 'ProcuraGrafo', derivada de 'MecanismoProcura', responsável por implementar um mecanismo de procura
    em grafos que lida com estados repetidos.

    Esta classe estende o comportamento da classe base 'MecanismoProcura' para suportar a eliminação de nós correspondentes
    a estados já explorados, evitando redundâncias em espaços de estados com ciclos. Isso é essencial em problemas onde 
    múltiplas transições podem levar ao mesmo estado, onde a expansão de estados repetidos pode desperdiçar recursos 
    (tempo e memória).

    A classe mantém uma memória de nós explorados (abertos e fechados) indexada por estado, permitindo acesso eficiente
    para verificar se um estado já foi processado. A decisão de manter ou descartar um nó sucessor é delegada ao método 
    abstrato '_manter'.
"""

class ProcuraGrafo( MecanismoProcura):

    # Metodo protegido '_iniciar_memoria', responsável por inicializar a memória de nós explorados.
    #
    # Este metodo sobrescreve o metodo homónimo da classe base 'MecanismoProcura' para inicializar, além da fronteira,
    # um dicionário '_explorados' que armazena os nós já processados, indexados por estado.
    #
    # A inicialização da memória é essencial para começar a procura sem estados residuais e para suportar a verificação
    # de estados repetidos. O dicionário '_explorados' permite acesso eficiente para verificar se um estado já foi
    # explorado, evitando desperdício de recursos em grafos com ciclos.
    def _iniciar_memoria(self):
        # Chama o metodo '_iniciar_memoria' da classe base para inicializar a fronteira como vazia, removendo quaisquer
        # nós residuais.
        super()._iniciar_memoria()

        # Inicializa o dicionário '_explorados' como vazio, preparando a memória para armazenar os nós explorados
        # (abertos e fechados) durante a procura.
        self._explorados = {}


    # Metodo protegido '_memorizar', responsável por memorizar um nó sucessor na estrutura de procura.
    #
    # Este metodo sobrescreve o metodo da classe base 'MecanismoProcura' para incorporar a verificação de estados
    # repetidos antes de memorizar um nó. Um nó sucessor só é memorizado se o metodo '_manter' determinar que ele deve
    # ser mantido, com base em critérios definidos pela subclasse (e.g., menor custo ou função de avaliação).
    #
    # Se o nó é mantido, ele é inserido na fronteira (via metodo da classe base) e registrado no dicionário '_explorados',
    # associando o estado do nó ao próprio nó. Isso garante que estados repetidos sejam geridos eficientemente.
    def _memorizar(self, no):

        # Verifica se o nó deve ser mantido, chamando o metodo abstrato '_manter', que será implementado por subclasses
        # para definir a lógica específica.
        if self._manter(no):

            # Se o nó for mantido, insere-o na fronteira usando o metodo '_memorizar' da classe base, respeitando a
            # estratégia de ordenação da fronteira.
            super()._memorizar(no)

            # Registra o nó no dicionário '_explorados', mapeando o estado do nó ao próprio nó, para permitir a
            # verificação futura de estados repetidos.
            self._explorados[no.estado] = no


    # Metodo abstrato '_manter', responsável por determinar se um nó sucessor deve ser mantido na procura.
    #
    # Este metodo deve ser implementado por subclasses para definir os critérios de manutenção de um nó, como comparar
    # o custo acumulado ou a função de avaliação f(n) com nós já explorados.
    #
    # A lógica de '_manter' é crucial para evitar a reexpansão de estados repetidos, especialmente em grafos com ciclos,
    # onde o mesmo estado pode ser alcançado por múltiplos percursos.
    @abstractmethod
    def _manter(self, no):
        """Abstract Method"""