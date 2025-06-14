from random import random, choice

from ecr.comportamento import Comportamento
from sae import Avancar, Rodar, Direccao

"""
Esta classe (Explorar) representa um comportamento reativo simples dentro
da arquitetura de agentes reativos.

Ela deriva da classe Comportamento, e a sua principal função é permitir que o agente se mova de 
forma aleatória no ambiente, ou seja, sem ter objetivos explícitos, apenas reagindo ao ambiente 
com base numa probabilidade de rotação.

O comportamento Explorar entra em ação quando não há alvos nem obstáculos detetados. 
Ele permite que o agente continue a movimentar-se e a "descobrir" o ambiente, aumentando 
a chance de encontrar novos alvos no futuro.
"""

class Explorar(Comportamento):

    # Recebeb e armazena como atributo a probabilidade de rotação, que controla o grau de aleatoriedade no movimento do agente.
    def __init__(self, prob_rotacao):
        self.__prob_rotacao = prob_rotacao

    # Decide se o agente deve avançar ou rodar, com base num valor aleatório e na probabilidade de rotação.
    def activar(self, percepcao):

        # Guarda o valor aleatorio que será usado para comparar com a prob_rotacao
        valor_aleatorio = random()

        # Caso o valor aleatorio não ultrapasse a probabilidade de rotação
        if valor_aleatorio < self.__prob_rotacao:

            # Como a direção é um enum, e o choice precisa de uma lista, trnasforma um enum em uma lista das suas atributos
            direccoes = list(Direccao)

            # Aqui usa-se o metodo chice do random para escolher uma direção na lista de direções
            direccao_aleatoria = choice(direccoes)

            # Retorna-se a ação Rodar com uma direção aleatoria
            return Rodar(direccao_aleatoria)

        # Caso contrario
        else:

            # Retorna-se a ação Avançar
            return Avancar()






