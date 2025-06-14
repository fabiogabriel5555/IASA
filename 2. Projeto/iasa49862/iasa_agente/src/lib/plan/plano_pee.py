from plan.plano import Plano

class PlanoPEE(Plano):

    def __init__(self, solucao):

        self.__passos = [passo for passo in solucao]


    def obter_accao(self, estado):

        if self.__passos:
            passo = self.__passos.pop(0)

            if passo.estado == estado:
                return passo.operador


    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)

    @property
    def dimensao(self):
        return len(self.__passos)
