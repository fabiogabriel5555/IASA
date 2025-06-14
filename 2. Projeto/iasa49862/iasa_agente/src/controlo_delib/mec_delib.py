from sae.ambiente.elemento import Elemento

"""
    Classe 'MecDelib' responsável por implementar o mecanismo de deliberação de um agente autónomo.

    Esta classe gerencia o processo de deliberação, que envolve a geração e seleção de objetivos com base no modelo do 
    mundo. Ela identifica estados associados a alvos no ambiente e os ordena por proximidade, suportando o processo de 
    tomada de decisão no controle deliberativo.

    A classe é usada no contexto de uma arquitetura deliberativa, onde a deliberação é uma etapa crítica do ciclo de 
    raciocínio prático, selecionando objetivos que guiam o planeamento e a execução de ações. A ordenação de objetivos 
    por distância alinha-se com estratégias de procura, como as usadas em algoritmos como `ProcuraCustoUnif`. 

    Esta classe encapsula o modelo do mundo como um atributo privado, utilizando métodos internos para gerar e selecionar 
    objetivos de forma eficiente.
"""

class MecDelib:

    # Inicializa uma instância do mecanismo de deliberação com um modelo do mundo.
    def __init__(self, modelo_mundo):

        self.__modelo_mundo = modelo_mundo

        ######################################
        self.__posicao_inicial  = None
        self.__key_guardar_inicio  = True
        self.__key_mover_inicio    = True


    # Metodo que executa o processo de deliberação, gerando e selecionando objetivos.
    # Este metodo coordena a geração de objetivos (estados associados a alvos) e a seleção dos mais relevantes,
    # retornando uma lista ordenada de objetivos. Ele é essencial para a fase de deliberação do ciclo de tomada de
    # decisão, guiando o planeamento subsequente.
    def deliberar(self):

        # Chama o metodo interno `__gerar_objectivos` para criar uma lista de estados associados a alvos no ambiente.
        objectivos = self.__gerar_objectivos()

        if self.__key_guardar_inicio:
            self.__key_guardar_inicio = False
            self.__posicao_inicial = self.__modelo_mundo.obter_estado()

        # Verifica se a lista de objetivos não está vazia, garantindo que a seleção só ocorra quando houver objetivos válidos.
        if objectivos:
            # Chama o metodo interno `__selecionar_objectivos`, passando a lista de objetivos, e retorna a lista ordenada
            # resultante.
            return self.__selecionar_objectivos(objectivos)
        elif self.__key_mover_inicio:
            self.__key_mover_inicio = False
            return [self.__posicao_inicial]
        else:
            return []


    # Metodo interno que gera uma lista de objetivos com base nos estados do ambiente.
    # Este metodo identifica todos os estados cujo elemento associado é um alvo, criando uma lista de possíveis
    # objetivos para o agente. Ele utiliza o modelo do mundo para acessar estados e elementos, alinhando-se com a
    # exploração de opções no raciocínio prático.
    def __gerar_objectivos(self):

        # Cria uma lista por compreensão, iterando sobre os estados retornados por `obter_estados` do modelo do mundo,
        # incluindo apenas aqueles cujo elemento associado é `Elemento.ALVO`, conforme identificado por `obter_elemento`.
        return [estado for estado in self.__modelo_mundo.obter_estados()
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]


    # Metodo interno que seleciona e ordena objetivos com base na distância ao estado atual.
    # Este metodo ordena a lista de objetivos pela distância euclidiana ao estado atual do agente, retornando a lista
    # ordenada para priorizar objetivos mais próximos. Ele suporta a eficiência no planeamento deliberativo,
    # minimizando o custo das ações.
    def __selecionar_objectivos(self, objectivos):

        # Ordena a lista de objetivos in-place, usando o metodo `sort` com a função `distancia` do modelo do mundo como
        # chave, para priorizar estados mais próximos do estado atual do agente.
        objectivos.sort(key = self.__modelo_mundo.distancia)

        # Retorna a lista de objetivos ordenada, pronta para ser usada no planeamento de ações.
        return objectivos