from controlo_delib.controlo_delib import ControloDelib
from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.estado_agente import EstadoAgente
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.ambiente.ambiente import Ambiente
from sae.agente.transdutor import Transdutor
from sae.defamb import DEF_AMB
from sae import Elemento, Direccao

"""
    Este script realiza uma sequência de testes unitários para verificar o funcionamento correto das classes 
    `ModeloMundo`, `MecDelib`, `PlaneadorPEE` e `ControloDelib` no contexto de uma arquitetura deliberativa. Ele 
    inicializa um ambiente específico, obtém uma percepção inicial e testa cada componente, verificando suas saídas 
    contra valores esperados.
"""

# Esta função cria uma instância de `ModeloMundo`, atualiza-a com a percepção fornecida e verifica se o estado, os
# estados possíveis, os operadores e os elementos estão corretos, conforme esperado para o ambiente testado.
def teste_modelo_mundo(percepcao):

    # Cria uma nova instância de `ModeloMundo`, inicializando-a com atributos vazios e operadores predefinidos para
    # todas as direções.
    modelo_mundo = ModeloMundo()

    # Atualiza o modelo do mundo com a percepção fornecida, configurando o estado atual, os elementos e os estados
    # possíveis do ambiente.
    modelo_mundo.actualizar(percepcao)

    # Verifica se o atributo `alterado` do modelo é True, confirmando que o modelo foi modificado pela percepção
    # inicial.
    assert modelo_mundo.alterado == True

    # Obtém o estado atual do agente chamando `obter_estado` e verifica se sua posição é (0, 0), conforme esperado
    # para a configuração inicial do ambiente.
    estado = modelo_mundo.obter_estado()
    assert estado.posicao == (0, 0)

    # Obtém a lista de estados possíveis chamando `obter_estados` e verifica se contém 671 estados, refletindo o
    # número de posições válidas no ambiente testado.
    estados = modelo_mundo.obter_estados()
    assert len(estados) == 671

    # Obtém a lista de operadores chamando `obter_operadores` e verifica se contém 4 operadores, correspondendo às
    # quatro direções definidas em `Direccao`.
    operadores = modelo_mundo.obter_operadores()
    assert len(operadores) == 4

    # Cria uma instância de `EstadoAgente` com a posição (28, 9), representando uma posição específica no ambiente.
    estado = EstadoAgente((28, 9))

    # Obtém o elemento associado à posição do estado chamando `obter_elemento` e verifica se é um `Elemento.ALVO`,
    # conforme esperado para a posição (28, 9) no ambiente.
    elemento = modelo_mundo.obter_elemento(estado)
    assert elemento == Elemento.ALVO

    # Retorna a instância do modelo do mundo atualizada, para ser usada em testes subsequentes.
    return modelo_mundo



# Função que testa o funcionamento do `MecDelib` com um modelo do mundo.
#
# Esta função cria uma instância de `MecDelib`, executa a deliberação para gerar objetivos e verifica se o número de
# objetivos gerados é correto, conforme esperado para o ambiente testado.
def teste_mec_delib(modelo_mundo):

    # Cria uma nova instância de `MecDelib`, passando o modelo do mundo para gerenciar a deliberação de objetivos.
    mec_delib = MecDelib(modelo_mundo)

    # Executa o metodo `deliberar` para gerar uma lista de objetivos, que são estados associados a alvos no ambiente.
    objectivos = mec_delib.deliberar()

    # Verifica se a lista de objetivos contém 3 elementos, conforme esperado para o ambiente testado, refletindo o
    # número de alvos presentes.
    assert len(objectivos) == 3

    # Retorna a instância de `MecDelib` e a lista de objetivos, para serem usados em testes subsequentes.
    return mec_delib, objectivos



# Função que testa o funcionamento do `PlaneadorPEE` com um modelo do mundo e objetivos.
#
# Esta função cria uma instância de `PlaneadorPEE`, gera um plano com base nos objetivos fornecidos e verifica se a
# dimensão do plano é correta, conforme esperado para o ambiente testado.
def teste_planeador_pee(modelo_mundo, objectivos):

    # Cria uma nova instância de `PlaneadorPEE`, que será usada para gerar planos de ação.
    planeador = PlaneadorPEE()

    # Gera um plano chamando o metodo `planear`, passando o modelo do mundo e a lista de objetivos, para criar uma
    # sequência de ações que alcança os objetivos.
    plano = planeador.planear(modelo_mundo, objectivos)

    # Verifica se a dimensão do plano é 37, conforme esperado para o ambiente testado, refletindo o número de passos
    # necessários para alcançar os objetivos.
    assert plano.dimensao == 37

    # Retorna a instância do planeador, para ser usada em testes subsequentes.
    return planeador



# Função que testa o funcionamento do `ControloDelib` com um planeador e uma percepção.
#
# Esta função cria uma instância de `ControloDelib`, processa a percepção para gerar uma ação e verifica se a ação
# retornada tem a direção correta, conforme esperado para o ambiente testado.
def teste_controlo_delib(planeador, percepcao):

    # Cria uma nova instância de `ControloDelib`, passando o planeador para coordenar o ciclo deliberativo.
    controlo = ControloDelib(planeador)

    # Processa a percepção chamando o mEtodo `processar`, que atualiza o modelo, delibera, planeia e retorna a próxima
    # ação a ser executada.
    accao    = controlo.processar(percepcao)

    # Verifica se a direção da ação retornada é `Direccao.SUL`, conforme esperado para o plano gerado no ambiente
    # testado.
    assert accao.direccao == Direccao.SUL



# Bloco principal que executa a sequência de testes.
#
# Este bloco inicializa o ambiente, obtém uma percepção inicial e executa os testes para cada componente, imprimindo uma
# mensagem de sucesso se todos os testes forem concluídos sem falhas.
if __name__ == "__main__":

    # Define o índice do ambiente a ser usado (4), selecionando uma configuração específica de `DEF_AMB`.
    num_amb = 4

    # Cria uma nova instância de `Ambiente`, passando a configuração correspondente de `DEF_AMB` para simular o
    # ambiente do agente.
    ambiente = Ambiente(DEF_AMB[num_amb])

    # Cria uma nova instância de `Transdutor`, que será usada para obter percepções do ambiente.
    transdutor = Transdutor()

    # Inicializa o transdutor com o ambiente, preparando-o para gerar percepções baseadas nas condições do ambiente.
    transdutor.iniciar(ambiente)

    # Obtém a percepção inicial do ambiente chamando o metodo `percepcionar` do transdutor, que fornece a posição do
    # agente e os elementos do ambiente.
    percepcao = transdutor.percepcionar()

    # Teste Modelo do Mundo
    modelo_mundo = teste_modelo_mundo(percepcao)

    # Teste de mecanismo delibertivo
    mec_delib, objectivos = teste_mec_delib(modelo_mundo)

    #Teste do Planeador
    planeador = teste_planeador_pee(modelo_mundo, objectivos)

    # Teste do controlo delibrativo
    teste_controlo_delib(planeador, percepcao)

    print("\nTeste concluido com sucesso")