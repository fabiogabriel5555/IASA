package iasa_jogo.src.maqest;

import iasa_jogo.src.agente.Accao;

public class Transicao {

    private Estado estadoSucessor;
    private Accao accao;

    public Transicao(Estado estadoSucessor, Accao accao)
    {
        this.estadoSucessor = estadoSucessor;
        this.accao = accao;
    }

    public Estado getEstadoSucessor() {return estadoSucessor;}

    public Accao getAccao() {return this.accao;}
}
