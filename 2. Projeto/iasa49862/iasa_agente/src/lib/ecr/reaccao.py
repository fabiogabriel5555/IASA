from .comportamento import Comportamento

"""
Esta classe (Reaccao) herda de Comportamento e representa uma reação simples entre: 

    Um estímulo, que verifica a presença de uma condição no ambiente;

    Uma resposta, que define a ação a executar caso o estímulo seja detetado com alguma intensidade.
"""
class Reaccao(Comportamento):

    # Construtor responsável por inicializar os atributos privados "estimulo" e "resposta"
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    # Ativa a reação com base na perceção atual.
    # Utiliza o estímulo associado para detetar se a perceção contém uma condição relevante.
    # O metodo 'detectar' devolve uma intensidade .
    # Se a intensidade for superior a zero, a resposta associada é ativada, passando a perceção e a intensidade. Caso contrário, nada é feito.
    # Esta classe representa a estrutura básica de uma reação estímulo–resposta.
    def activar(self, percepcao):

        # Esta variavel é responsável detectar a intensidade do estimulo
        # Essa detecção é feita atravéz do metodo 'detectar' do atributo estimulo
        # O atributo detectar do estimulo recebe a percepção e devolve a intensidade
        intensidade = self.__estimulo.detectar(percepcao)

        # Caso a intensidade seja maior que 0
        if intensidade > 0:

            # Ativa e devolve a resposta a intesidade e a percepção
            return self.__resposta.activar(percepcao, intensidade)