from abc import ABC

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
    Classe abstrata 'MecanismoProcura' responsável por definir a estrutura base para um mecanismo de procura. 

    O mecanismo de procura é responsável por explorar o espaço de estados de um problema, utilizando uma fronteira de 
    exploração para gerir os nós a serem processados e encontrar uma solução que conecte o estado inicial ao estado 
    objetivo. 
    
    O mecanismo de procura utiliza uma fronteira para 'memorizar e gerir nós explorados', sendo responsável por procurar 
    uma solução para um problema.
    
    O mecanismo suporta a exploração do espaço de estados através da aplicação de operadores e teste de objetivos.
    
    Esta classe abstrai o processo genérico de procura, deixando a cargo das subclasses a definição de como a memória 
    de nós explorados é iniciada e gerida, bem como a estratégia específica de exploração (e.g., profundidade, largura).
"""

class MecanismoProcura(ABC):

    # Inicializa uma instância do mecanismo de procura com uma fronteira específica.
    #
    # Este metodo associa uma fronteira ao mecanismo, que será usada para gerir os nós durante a exploração do espaço
    # de estados.
    #
    # A escolha da fronteira (e.g., FIFO para largura, LIFO para profundidade) determina a estratégia de controlo,
    # conforme
    #
    # O atributo `_fronteira` é protegido (com `_`) para permitir acesso controlado por subclasses, mas desencorajar
    # modificações externas.
    def __init__(self, fronteira):
        self._fronteira = fronteira


    # Propriedade que devolve o número total de nós processados (criados) durante a procura.
    #
    # Acessa o contador `nos_criados` da classe `No`, que monitoriza a criação de nós, permitindo avaliar a complexidade
    # temporal da procura.
    @property
    def nos_processados(self):
        return No.nos_criados


    # Propriedade que devolve o número máximo de nós simultaneamente em memória durante a procura.
    #
    # Acessa o contador `nos_max_mem` da classe `No`, que reflete o pico de uso de memória, útil para avaliar a
    # complexidade espacial
    @property
    def nos_em_memoria(self):
        return No.nos_max_mem


    # Metodo protegido '_iniciar_memoria', responsável por inicializar a memória de nós explorados.
    #
    # Este metodo prepara a estrutura de memória que armazena os nós já processados ou abertos, essencial para evitar
    # redundâncias em grafos com ciclos.
    #
    # É chamado antes do início da procura para garantir que a exploração comece sem estados previamente memorizados.
    def _iniciar_memoria(self):

        # Chama o metodo `iniciar` da fronteira para configurá-la como vazia, removendo quaisquer nós residuais.
        self._fronteira.iniciar()


    # Metodo protegido '_iniciar_memoria', responsável por memorizar um nó sucessor na estrutura de procura.
    #
    # Este metodo é responsável por decidir como um nó sucessor gerado durante a expansão é armazenado, seja na
    # fronteira, na memória de explorados, ou ambos, dependendo da estratégia de procura.
    def _memorizar(self, no):

        # Insere o nó na fronteira usando o metodo `inserir`, respeitando a estratégia da fronteira (e.g., FIFO, LIFO).
        self._fronteira.inserir(no)


    # Metodo "procurar", responsável por executar a procura de uma solução para o problema fornecido.
    #
    # Este metodo implementa o ciclo principal de procura em espaço de estados, começando pelo estado inicial,
    # expandindo nós e testando o objetivo até encontrar uma solução ou esgotar a fronteira.
    #
    # Baseia-se no algoritmo genérico de procura descrito em 'Procura em Espaços de Estados', adaptado para usar os
    # métodos abstratos desta classe, permitindo diferentes estratégias (e.g., largura, profundidade).
    #
    # Tem como argumento problema a ser resolvido, uma instância da classe `Problema` contendo estado inicial,
    # operadores e função objetivo.
    #
    # Retornna uma solução ou None.Uma instância de `Solucao` representando o percurso até o estado objetivo, ou `None`
    # se nenhuma solução for encontrada.
    def procurar(self, problema):

        # Inicializa a memória de nós explorados, garantindo que a procura comece sem estados residuais.
        self._iniciar_memoria()

        # Cria um nó inicial com o estado inicial do problema, que será o ponto de partida da procura, como no início
        # de uma navegação por mapa.
        no = No(problema.estado_inicial)

        # Memoriza o nó inicial na fronteira, adicionando-o à estrutura para ser processado primeiro.
        self._memorizar(no)

        # Inicia um ciclo que continua enquanto houver nós na fronteira para explorar, verificando se ainda há trabalho
        # a fazer, como no ciclo principal de procura.
        while not self._fronteira.vazia:

            # Retira o próximo nó da fronteira para ser analisado, dependendo da estratégia.
            no = self._fronteira.remover()

            # Verifica se o estado do nó atual é o objetivo do problema; se for, a procura termina com sucesso.
            if problema.objectivo(no.estado):

                # Devolve uma solução construída a partir do nó objetivo, representando o percurso desde o início até
                # ele, como retornar o caminho final em largura.
                return Solucao(no)

            # Expande o nó atual, gerando todos os seus sucessores, e perccore-os para os processar.
            for no_sucessor in self._expandir(problema, no):

                # Passa cada sucessor para o metodo `_memorizar()`, que decide como lidar com ele.
                self._memorizar(no_sucessor)

        # Se a fronteira ficar vazia sem encontrar o objetivo, devolve `None`, indicando que não há solução, como o fim
        # sem sucesso em 'Procura em Espaços de Estados'
        return None


    # Metodo protegido "_expandir", responsável por expandir um nó, gerando seus sucessores com base nos operadores
    # do problema.
    #
    # Este metodo aplica todos os operadores disponíveis a um estado, gerando novos nós sucessores com custos
    # atualizados.
    #
    # Calcula o custo acumulado (`no.custo + operador.custo`) para cada sucessor
    #
    # Retorna apenas sucessores válidos (`estado_suc is not None`), refletindo a verificação de aplicabilidade dos
    # operadores.
    def _expandir(self, problema, no):

        # Cria uma lista vazia para guardar os nós sucessores que serão gerados, começando do zero para acumular os
        # resultados da expansão.
        sucessores = []

        # Obtém o estado atual do nó que está a ser expandido.
        estado = no.estado

        # Percorre todos os operadores disponíveis no problema, para os aplicar um a um ao estado atual.
        for operador in problema.operadores:

            # Aplica o operador ao estado atual, gerando um novo estado sucessor, como mover o espaço vazio e obter um
            # novo tabuleiro
            estado_suc = operador.aplicar(estado)

            # Verifica se o estado sucessor é válido (não é `None`), garantindo que só se criam nós para transições
            # possíveis.
            if estado_suc is not None:

                # Calcula o custo total do novo nó somando o custo acumulado do nó atual com o custo da transição.
                custo = no.custo + operador.custo(estado, estado_suc)

                # Cria um novo nó com o estado sucessor, o operador que o gerou, o nó atual como antecessor e o custo
                # total, formando assim a estrutura da árvore de procura.
                no_sucessor = No(estado_suc, operador, no, custo)

                # Adiciona o novo nó à lista de sucessores, guardando-o para ser devolvido e usado no processo de
                # procura.
                sucessores.append(no_sucessor)

        # Devolve a lista completa de sucessores gerados, pronta para ser processada em `procurar()`, como `[nó1, nó2]`
        # com novos estados do puzzle.
        return sucessores