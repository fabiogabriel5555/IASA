from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo

"""
    Classe 'ControloDelib' responsável por implementar o controle deliberativo de um agente autónomo.

    Esta classe coordena o processo cíclico de tomada de decisão de um agente, integrando assimilação de percepções, 
    reconsideração, deliberação, planeamento e execução de ações. Ela utiliza um modelo do mundo para representar o 
    ambiente, um mecanismo de deliberação para selecionar objetivos e um planeador para gerar planos de ação.

    A classe suporta a arquitetura deliberativa, onde o agente observa o ambiente, atualiza seu modelo interno, delibera 
    sobre objetivos, planeja ações e executa movimentos, alinhando-se com o processo de raciocínio prático

    Esta classe encapsula o modelo do mundo, o mecanismo de deliberação, o planeador, os objetivos e o plano como 
    atributos privados, gerenciando o ciclo de controle deliberativo através de métodos específicos.
"""

class ControloDelib:

    # Inicializa uma instância do controle deliberativo com um planeador específico.
    def __init__(self, planeador):

        # Cria uma nova instância de `ModeloMundo` e armazena-a no atributo privado `__modelo_mundo`, que representará o
        # ambiente do agente.
        self.__modelo_mundo = ModeloMundo()

        # Cria uma nova instância de `MecDelib`, passando o modelo do mundo, e armazena-a no atributo privado
        # `__mec_delib`, que será responsável pela deliberação de objetivos.
        self.__mec_delib = MecDelib(self.__modelo_mundo)

        # Armazena o planeador fornecido no atributo privado `__planeador`, que será usado para gerar planos de ação
        # baseados nos objetivos.
        self.__planeador = planeador

        # Define o atributo privado `__objectivos` como None, indicando que nenhum objetivo foi selecionado inicialmente.
        self.__objectivos = None

        # Define o atributo privado `__plano` como None, indicando que nenhum plano foi gerado inicialmente.
        self.__plano = None


    # Metodo que processa uma percepção do ambiente e retorna a ação a ser executada.
    # Este metodo implementa o ciclo principal do controle deliberativo, assimilando a percepção, reconsiderando
    # objetivos e planos, deliberando, planejando e executando ações. Ele coordena o processo de tomada de decisão,
    # garantindo que o agente responda adequadamente ao ambiente.
    def processar(self, percepcao):

        # Chama o metodo `__assimilar` para atualizar o modelo do mundo com a percepção fornecida, integrando novas
        # informações do ambiente.
        self.__assimilar(percepcao)

        # Verifica se é necessário reconsiderar objetivos ou planos, chamando o metodo `__reconsiderar` para avaliar o
        # estado do modelo e do plano.
        if self.__reconsiderar():

            # Se a reconsideração for necessária, chama o metodo `__deliberar` para selecionar novos objetivos.
            self.__deliberar()

            # Após a deliberação, chama o metodo `__planear` para gerar um novo plano com base nos objetivos
            # selecionados.a
            self.__planear()

        # Chama o metodo `__executar` para obter e retornar a ação a ser executada com base no plano atual, concluindo o
        # ciclo de controle.
        return self.__executar()


    # Metodo que assimila uma percepção, atualizando o modelo do mundo.
    # Este metodo atualiza o modelo interno do agente com base nas informações fornecidas pela percepção, refletindo
    # mudanças no ambiente. Ele é essencial para a fase de observação do processo cíclico de tomada de decisão.
    def __assimilar(self, percepcao):

        # Chama o metodo `actualizar` do modelo do mundo, passando a percepção para atualizar o estado atual, os
        # elementos e os estados possíveis.
        self.__modelo_mundo.actualizar(percepcao)


    # Metodo que determina se é necessário reconsiderar objetivos ou planos.
    # Este metodo verifica se o modelo do mundo foi alterado ou se não há um plano válido, indicando a necessidade de
    # deliberação e planeamento. Ele suporta a reconsideração dinâmica no controle deliberativo.
    def __reconsiderar(self):

        # Retorna True se o modelo do mundo foi alterado (indicado por `__modelo_mundo.alterado`) ou se não há um plano
        # válido (`__plano` é None), caso contrário retorna False.
        return self.__modelo_mundo.alterado or not self.__plano


    # Metodo que delibera sobre os objetivos do agente.
    # Este metodo utiliza o mecanismo de deliberação para selecionar objetivos com base no estado atual do modelo do
    # mundo, definindo os objetivos a serem alcançados no planeamento.
    def __deliberar(self):

        # Chama o metodo `deliberar` do mecanismo de deliberação e armazena o resultado no atributo privado
        # `__objectivos`, definindo os objetivos do agente.
        self.__objectivos = self.__mec_delib.deliberar()


    # Metodo que gera um plano de ação com base nos objetivos selecionados.
    # Este metodo utiliza o planeador para criar um plano que conecte o estado atual aos objetivos, ou define o plano
    # como nulo se não houver objetivos. Ele é essencial para a fase de planeamento do controle deliberativo .
    def __planear(self):

        # Verifica se há objetivos definidos, garantindo que o planeamento só ocorra quando houver objetivos válidos.
        if self.__objectivos is not None:
            # Chama o metodo `planear` do planeador, passando o modelo do mundo e os objetivos, e armazena o plano
            # resultante no atributo privado `__plano`.
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objectivos)

        # Caso não haja objetivos, define o atributo privado `__plano` como None, indicando que nenhum plano pode ser
        # gerado.
        else:
            self.__plano = None


    # Metodo que executa a próxima ação do plano atual.
    # Este metodo verifica se há um plano válido, obtém o estado atual e seleciona a próxima ação do plano, retornando-a
    # para execução. Se nenhuma ação estiver disponível, o plano é invalidado. Ele conclui o ciclo de controle
    # deliberativo com a execução de ações.
    def __executar(self):

        # Verifica se há um plano válido, prosseguindo apenas se `__plano` não for None.
        if self.__plano is not None:

            # Obtém o estado atual do agente chamando o metodo `obter_estado` do modelo do mundo, que será usado para
            # consultar o plano.
            estado   = self.__modelo_mundo.obter_estado()

            # Obtém a próxima ação do plano chamando o metodo `obter_accao` do plano, passando o estado atual para
            # determinar a ação apropriada.
            operador = self.__plano.obter_accao(estado)

            # Verifica se uma ação foi retornada, indicando que o plano ainda tem ações a executar.
            if operador is not None:

                # Retorna a propriedade `accao` do operador, que contém a ação específica a ser executada no ambiente.
                return operador.accao

            # Caso nenhuma ação seja retornada, define o atributo privado `__plano` como None, invalidando o plano
            # atual.
            else:
                self.__plano = None


    # Metodo que exibe o estado do controle deliberativo em uma interface visual.
    # Este metodo limpa a interface visual, exibe o modelo do mundo, o plano atual (se existente) e marca os objetivos
    # (se definidos), permitindo a visualização do estado do agente e seu plano
    def mostrar(self, vista):

        # Chama o metodo `limpar` da interface visual para remover qualquer conteúdo anterior, preparando a visualização.
        vista.limpar()

        # Chama o metodo `mostrar` do modelo do mundo, passando a interface visual para exibir os elementos e a posição
        # do agente.
        self.__modelo_mundo.mostrar(vista)

        # Verifica se há um plano válido, garantindo que a visualização do plano só ocorra quando apropriado.
        if self.__plano:

            # Chama o metodo `mostrar` do plano, passando a interface visual para exibir a sequência de ações planejadas.
            self.__plano.mostrar(vista)

        # Verifica se há objetivos definidos, garantindo que a marcação de objetivos só ocorra quando apropriado.
        if self.__objectivos:

            # Itera sobre cada objetivo na lista de objetivos, processando cada um para visualização.
            for objectivo in self.__objectivos:

                # Chama o metodo `marcar_posicao` da interface visual, passando a posição do objetivo para marcá-lo no
                # ambiente.
                vista.marcar_posicao(objectivo.posicao)