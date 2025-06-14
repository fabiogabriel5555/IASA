from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim):

    def procurar(self, problema, heuristica):

        self._avaliador.heuristica = heuristica

        return super().procurar(problema)
