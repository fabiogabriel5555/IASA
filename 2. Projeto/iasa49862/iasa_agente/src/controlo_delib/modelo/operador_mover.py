import math

from controlo_delib.modelo.estado_agente import EstadoAgente
from sae.agente.accao import Accao

"""
    Classe 'OperadorMover' responsável por implementar operadores de movimento de um agente autónomo no ambiente.

    Esta classe define operadores que permitem ao agente transitar entre estados no espaço de estados, movendo-se em uma 
    direção específica. Cada operador está associado a um modelo do mundo e a uma direção, suportando a aplicação de 
    movimentos, o cálculo de deslocamentos e a avaliação de custos para planeamento deliberativo.

    A classe é usada no contexto de uma arquitetura deliberativa, onde operadores são aplicados a estados para gerar 
    sucessores durante a procura, como em algoritmos como `ProcuraCustoUnif`. Ela facilita o raciocínio prático ao 
    simular ações no modelo do mundo, essencial para o processo cíclico de tomada de decisão.
"""

class OperadorMover:

    # Inicializa uma instância do operador de movimento com um modelo do mundo e uma direção.
    def __init__(self, modelo_mundo, direccao):

        # Armazena o modelo do mundo fornecido no atributo privado `__modelo_mundo`, que será usado para validar
        # estados sucessores e calcular custos.
        self.__modelo_mundo = modelo_mundo

        # Armazena a direção fornecida no atributo privado `__direccao`, definindo a orientação do movimento do
        # operador.
        self.__direccao     = direccao

        # Define o atributo privado `__ang` com o valor numérico da direção (em radianos), obtido de `direccao.value`,
        # usado para cálculos de deslocamento.
        self.__ang   = direccao.value

        # Cria uma nova instância de `Accao` com a direção fornecida e armazena-a no atributo privado `__accao`, que
        # representa a ação executável no ambiente.
        self.__accao = Accao(direccao)


    # Propriedade que devolve o ângulo associado à direção do movimento.
    @property
    def ang(self):
        return self.__ang


    # Propriedade que devolve a ação associada ao operador de movimento.
    @property
    def accao(self):
        return self.__accao

    # Este metodo realiza a translação geométrica com base na posição atual, na distância do passo e no ângulo da
    # direção, retornando a nova posição como uma tupla de coordenadas. Ele é usado para determinar o estado sucessor
    # após a aplicação do operador.
    def __translacao(self, posicao, distancia, angulo):

        # Desempacota a tupla de posição em coordenadas x e y, facilitando os cálculos de deslocamento.
        x, y = posicao

        # Calcula o deslocamento na direção x usando a fórmula dx = distância * cos(ângulo), arredondando o resultado
        # para garantir coordenadas inteiras.
        dx = round( distancia * math.cos(angulo) )

        # Calcula o deslocamento na direção y usando a fórmula dy = -distância * sin(ângulo), com sinal negativo para
        # alinhar com a convenção de coordenadas, arredondando o resultado.
        dy = round( -distancia * math.sin(angulo) )

        # Combina os deslocamentos com a posição inicial para criar uma nova posição (x + dx, y + dy), representando
        # o resultado da translação.
        nova_posicao = (x + dx, y + dy)

        # Retorna a nova posição como uma tupla, pronta para ser usada na criação de um estado sucessor.
        return nova_posicao

    # Este metodo calcula a nova posição com base na direção e no passo da ação, cria um novo estado com essa posição e
    # verifica sua validade no modelo do mundo, retornando o estado sucessor se válido. Ele é usado por algoritmos de
    # procura para expandir nós durante a exploração do espaço de estados.
    def aplicar(self, estado):

        # Calcula a nova posição chamando o metodo interno `__translacao`, passando a posição atual do estado, o passo
        # da ação (obtido de `accao.passo`) e o ângulo da direção (obtido de `ang`).
        nova_posicao = self.__translacao(estado.posicao, self.accao.passo, self.ang)

        # Cria uma nova instância de `EstadoAgente` com a nova posição calculada, representando o estado sucessor
        # potencial.
        novo_estado = EstadoAgente(nova_posicao)

        # Verifica se o novo estado está contido no modelo do mundo (usando o metodo `__contains__`), garantindo que
        # apenas estados válidos sejam retornados.
        if novo_estado in self.__modelo_mundo:

            # Retorna o novo estado se for válido, permitindo sua inclusão na procura ou no plano.
            return novo_estado

    # Este metodo determina o custo da transição com base na distância euclidiana entre as posições dos estados,
    # garantindo um custo mínimo de 1 para evitar custos nulos. Ele é essencial para algoritmos de procura como
    # `ProcuraCustoUnif`, que ordenam nós com base no custo acumulado.
    def custo(self, estado, estado_suc):

        # Calcula a distância euclidiana entre as posições do estado atual e do estado sucessor usando a função
        # `math.dist`, representando o custo base da transição.
        custo = math.dist(estado.posicao, estado_suc.posicao)

        # Retorna o maior valor entre 1 e o custo calculado, garantindo que o custo da transição seja sempre positivo
        # e nunca zero, conforme exigido por algoritmos de procura.
        return max(1, custo)

