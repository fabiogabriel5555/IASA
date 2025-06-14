package iasa_jogo.src.maqest;

import iasa_jogo.src.agente.Accao;
import iasa_jogo.src.ambiente.Evento;

public class MaquinaEstados {

    private Estado estado;

    public MaquinaEstados(Estado estadoInicial){this.estado = estadoInicial;}

    public Estado getEstado(){return estado;}

    public Accao processar(Evento evento)
    {
        Accao accao = null;
        Transicao transicao = estado.processar(evento);

        if(transicao != null)
        {
            estado = transicao.getEstadoSucessor();
            accao = transicao.getAccao();
        }

        return accao;
    }


}
