from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

"""
    Esta classe representa um estímulo para detectar um alvo em uma direção específica.
    Herda da classe `Estimulo`.
    
    Implementa a lógica de detecção de alvos no ambiente do agente, que retorna uma intensidade 
    baseada na distância do alvo detectado.
    
    A intensidade do estímulo diminui exponencialmente com a distância, usando um fator de decaimento `gama`.
    Se o elemento detectado não for um alvo, a intensidade retornada é zero.

    Esta classe é utilizada no 'Agente Prospector' para identificar alvos em direções discretas (NORTE, SUL, ESTE, OESTE).
"""

class EstimuloAlvo(Estimulo):

    """
        Este construtor define a direção de detecção e o fator de decaimento `gama`, que controla
        a redução da intensidade do estímulo em função da distância do alvo.
    """
    def __init__(self, direccao, gama = 0.9):

        # Define a direção na qual a detecção será realizada
        self.__direccao = direccao

        # Define o fator de decaimento que controla a redução da intensidade com a distância
        self.__gama = gama

    """
        Metodo responsáel por detectar a presença de um alvo na direção especificada e calcular a
        sua intensidade.

        Extrai da percepção o elemento, a distância e outra informação que neste caso é irrelevante.
        
        Se o elemento for um alvo (`Elemento.ALVO`), calcula a intensidade como `gama ** distancia`,
        onde `gama` é o fator de decaimento e `distancia` é a distância do alvo. Caso contrário,
        retorna intensidade zero.
    """
    def detectar(self, percepcao):

        # Obtém o elemento, a distância e ignora o terceiro valor retornado pela percepção
        # ATT1: Em python, mesmo sem usarmos a notação de tuplos (), o compilador percebe que se trata de um tuplo por causa das virgulas.
        # ATT2: Em python, _ significa uma variavel que não será usada. Ela é importante porque neste caso concreto n|ao se precisa do terceiro elemento retornado do tuplo da percepção
        elemento, distancia, _ = percepcao[self.__direccao]

        # Se o elemento for um alvo, calcula e define a intensidade usando a fórmula `gama ** distancia`
        # Caso contrário, define a intensidade como 0 (sem estímulo detectado)
        intensidade = self.__gama ** distancia if (elemento == Elemento.ALVO) else 0

        # Retorna a intensidade
        return intensidade

