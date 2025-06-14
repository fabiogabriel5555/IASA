class Heuristica:
    """
        Classe 'Heuristica', responsável por definir a interface para funções heurísticas usadas em algoritmos de
        procura informada.

        Esta classe fornece a estrutura base para calcular a estimativa heurística h(n), que representa o custo estimado do
        estado atual até o estado objetivo em algoritmos como A* e procura gulosa. A heurística é essencial para
        direcionar a procura em direção a estados promissores, reduzindo o número de nós expandidos em comparação com
        algoritmos não informados, como procura de custo uniforme ou largura.
    """

    def h(self, estado):
        raise NotImplementedError