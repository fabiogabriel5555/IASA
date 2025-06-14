from ecr.resposta import Resposta
from sae.agente.rodar import Rodar

"""
    Esta classe representa a resposta 'RespostaEvitar' de um agente reativo.
    
    Herda da classe `Resposta` e implementa a lógica para gerar uma ação evitar quando um obstáculo
    é detectado na direção atual do agente, rotacionando a direção do agente para uma nova 
    orientação.
    
    Se um obstáculo é detectado na direção atual do agente, a resposta define uma ação de rotação
    para uma nova direção, delegando a execução à classe mãe Resposta.

    Esta classe é utilizada no 'Agente Prospector' como parte do sub-comportamento 'EvitarDir',
    para concretizar o sub-objetivo de evitar obstáculos em um espaço discreto com direções 
    NORTE, SUL, ESTE e OESTE.
"""

class RespostaEvitar(Resposta):

    """
        Este metodo gera uma ação evitar com base na percepção e na intensidade do estímulo.

        Verifica se há contato com um obstáculo na direção atual do agente (`dir_agente`). Se
        houver, calcula uma nova direção rotacionando a direção atual usando o metodo `rodar()`
        e define uma ação de rotação (`Rodar`) para essa nova direção. Em seguida, delega a
        ativação da ação à mãe Resposta.
    """
    def activar(self, percepcao, intensidade):

        # Obtém a direção atual do agente a partir do objeto de percepção
        dir_agente = percepcao.direccao

        # Verifica se há um obstáculo na direção atual do agente, e se ouver:
        if percepcao.contacto_obst(dir_agente):

            # Calcula uma nova direção rotacionada
            dir_resposta = dir_agente.rodar()

            # Define a ação de rotação para a nova direção calculada
            self._accao = Rodar(dir_resposta)

            # Chama o mEtodo activar da mãe Resposta para delegar a ativação da ação
            return super().activar(percepcao, intensidade)