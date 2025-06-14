from ecr.estimulo import Estimulo

"""
    Esta classe representa um estímulo para detectar a presença de um obstáculo em uma direção 
    específica.
    
    Herda da classe `Estimulo` 
    
    Implementa a lógica de detecção de contato com obstáculos no ambiente do agente, 
    retornando uma intensidade fixa se um obstáculo for detectado.
    
    A intensidade é configurável e retornada apenas quando há contato direto com um obstáculo na 
    direção especificada; caso contrário, retorna zero.

    Esta classe é utilizada no 'Agente Prospector' para identificar obstáculos em direções 
    discretas (NORTE, SUL, ESTE, OESTE), como parte do sub-objetivo de evitar obstáculos. 
"""

class EstimuloObst(Estimulo):

    """
        Este construtor defenie a direção de detecção e a intensidade fixa a ser retornada quando
        um obstáculo é detectado.

        A inicialização da classe mãe `Estimulo` é chamada sem parâmetros adicionais.
    """
    def __init__(self, direccao, intensidade = 1):

        # Define a direção na qual a detecção será realizada
        self.__direccao = direccao

        # Define a intensidade fixa que será retornada se um obstáculo for detectado
        self.__intensidade = intensidade

        # Chama o construtor da classe mãe (Estimulo)
        super().__init__()

    """
        Método responsável por detectar a presença de um obstáculo na direção especificada e 
        retorna a intensidade configurada.

        Verifica se há contato com um obstáculo na direção configurada usando o método 
        `contacto_obst` do objeto `percepcao`. Retorna o valor de `__intensidade` se um 
        obstáculo for detectado, ou 0 caso contrário.
    """
    def detectar(self, percepcao):

        # Se houver um obstáculo na direção configurada, retorna a intensidade; caso contrário, retorna 0
        return self.__intensidade if percepcao.contacto_obst(self.__direccao) else 0
