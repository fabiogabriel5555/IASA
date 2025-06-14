
"""
    Classe "No", responsável por representar um nó na árvore de procura no contexto de raciocínio automático e procura
    em espaço de estados.

    Um nó encapsula um estado do problema, o operador que o gerou, o seu antecessor na árvore de procura, a profundidade
    na árvore e o custo acumulado desde o estado inicial.

    É uma estrutura fundamental para construir e navegar a árvore de procura, permitindo rastrear o percurso até um
    estado objetivo e avaliar o custo ou profundidade da solução.
"""

class No:
    # Contador de nós criados, usado para monitorizar a criação de nós durante a procura.
    nos_criados    = 0

    # Contador de nós eliminados, usado para acompanhar a libertação de memória.
    nos_eleminados = 0

    # Máximo número de nós em memória ao mesmo tempo, útil para avaliar a complexidade espacial.
    nos_max_mem    = 0

    # Propriedade que devolve o estado associado ao nó.
    @property
    def estado(self):
        return self.__estado

    # Propriedade que devolve o operador que gerou o nó.
    @property
    def operador(self):
        return self.__operador

    # Propriedade que devolve o nó antecessor na árvore de procura.
    @property
    def antecessor(self):
        return self.__antecessor

    # Propriedade que devolve a profundidade do nó na árvore de procura.
    @property
    def profundidade(self):
        return self.__profundidade

    # Propriedade que devolve o custo acumulado até o nó.
    @property
    def custo(self):
        return self.__custo

    # Propriedade que devolve a prioridade do nó.
    @property
    def prioridade(self):
        return self.__prioridade

    # Setter para a propriedade prioridade, permitindo atualizar o valor de prioridade do nó.
    @prioridade.setter
    def prioridade(self, value):
        self.__prioridade = value

    # Metodo destrutor, chamado quando o nó é eliminado da memória.
    # Incrementa o contador de nós eliminados para monitorizar a libertação de memória.
    def __del__(self):
        No.nos_eleminados += 1


    # Metodo de comparação para ordenação de nós com base na prioridade.
    # Retorna True se a prioridade do nó atual for menor que a do outro nó.
    def __lt__(self, other):
        return self.prioridade < other.prioridade


    # Inicializa uma instância de um nó com o estado, operador, antecessor e custo.
    #
    # Este metodo cria um nó com os atributos necessários para representar um estado na árvore de procura, definindo
    # relações com o antecessor e calculando a profundidade automaticamente.
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):

        # Inicializa a prioridade do nó como 0.
        self.__prioridade = 0

        # Guarda o estado do problema neste nó, como uma configuração específica do espaço de estados.
        self.__estado = estado

        # Regista o operador que foi aplicado para chegar a este estado, permitindo reconstruir o percurso.
        # None se for o nó inicial.
        self.__operador = operador

        # Define o nó antecessor (pai) na árvore de procura, criando a ligação para trás;
        # None se este for o nó raiz (estado inicial).
        self.__antecessor = antecessor

        # Calcula a profundidade do nó: 0 se não houver antecessor (nó inicial), ou a profundidade do antecessor mais 1,
        # refletindo o número de passos desde o início.
        if antecessor is None:
            self.__profundidade = 0

            # Reinicia os contadores quando o nó inicial é criado, indicando o início de uma nova procura.
            No.nos_criados      = 0
            No.nos_eleminados   = 0
            No.nos_max_mem      = 0
        else:
            self.__profundidade = antecessor.profundidade + 1

        # Armazena o custo acumulado até este nó, útil para estratégias como custo uniforme;
        # pode ser None se não for fornecido ou calculado ainda.
        self.__custo = custo

        # Incrementa o contador de nós criados, refletindo a criação de um novo nó.
        No.nos_criados += 1

        # Calcula o número de nós atualmente em memória (criados menos eliminados).
        nos_memoria = No.nos_criados - No.nos_eleminados

        # Atualiza o máximo número de nós em memória, usado para avaliar o pico de uso de memória.
        No.nos_max_mem = max(No.nos_max_mem, nos_memoria)


