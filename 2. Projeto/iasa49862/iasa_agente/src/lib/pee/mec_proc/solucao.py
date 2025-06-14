"""
    Classe 'Solucao', responsável por representar uma solução completa no contexto de raciocínio automático e procura
    em espaço de estados.

    A solução encapsula as informações sobre o percurso encontrado desde o estado inicial  até o estado objetivo,
    incluindo o nó final da procura, a dimensão (número de passos) e o custo total do caminho. Serve como o resultado
    final do processo de procura, permitindo avaliar a eficiência da solução encontrada.
"""
from pee.mec_proc.passo_solucao import PassoSolucao


class Solucao():

    # Inicializa uma instância de uma solução com base no nó final da procura.
    #
    # Este metodo cria uma solução a partir do nó que representa o estado objetivo, inicializando a lista de passos
    # e reconstruindo o percurso desde o estado inicial até o objetivo.
    #
    # A reconstrução utiliza os antecessores do nó final para formar uma sequência de passos, cada um associado a um
    # estado e operador
    def __init__(self, no_final):

        # Armazena o nó final da procura, que contém o estado objetivo e as informações necessárias para reconstruir o
        # percurso desde o estado inicial.
        self.__no_final = no_final

        # Inicializa a lista de passos como vazia, para armazenar a sequência de passos da solução.
        self.__passos = []

        # Define uma variável temporária para percorrer os antecessores, começando pelo nó final.
        no = no_final

        # Percorre os antecessores do nó final até alcançar o nó inicial (sem antecessor), reconstruindo o
        # percurso ao contrário
        while no.antecessor:

            # Cria um objeto PassoSolucao com o estado do nó antecessor e o operador que gerou o nó atual,
            # representando uma transição no percurso.
            passo = PassoSolucao(no.antecessor.estado, no.operador)

            # Insere o passo no início da lista de passos, garantindo que a sequência esteja na ordem correta
            # (do estado inicial ao objetivo).
            self.__passos.insert(0, passo)

            # Move para o nó antecessor, continuando a reconstrução do percurso até o estado inicial.
            no = no.antecessor


    # Metodo que torna a solução "percorrivel", permitindo percorrer os passos da solução.
    # Este metodo devolve um iterador para a lista de passos, possibilitando o uso da solução em ciclos
    # `for`, como para visualizar o percurso passo a passo.
    def __iter__(self):
        # Devolve um iterador para a lista interna de passos, permitindo acesso sequencial aos passos.
        return iter(self.__passos)


    # Metodo que permite acesso aos passos da solução por índice.
    # Este metodo suporta indexação direta (e.g., solucao[0]), devolvendo o passo correspondente ao índice
    # fornecido, útil para inspecionar passos específicos do percurso.
    def __getitem__(self, index):
        # Devolve o passo armazenado na lista de passos no índice fornecido, permitindo acesso direto.
        return self.__passos[index]


    # Propriedade que devolve a dimensão da solução.
    # A dimensão corresponde ao número de passos no percurso (profundidade do nó final), indicando a
    # quantidade de transições necessárias para alcançar o objetivo.
    @property
    def dimensao(self):
        # Devolve a profundidade do nó final, que indica o número de passos desde o estado inicial até o
        # objetivo.
        return self.__no_final.profundidade


    # Propriedade que devolve o custo total da solução.
    # O custo total é o custo acumulado do caminho desde o estado inicial até o estado objetivo,
    # refletindo a soma dos custos das transições, como em procura de custo uniforme.
    @property
    def custo(self):
        # Devolve o custo do nó final, que representa o custo total do percurso até o estado objetivo.
        return self.__no_final.custo