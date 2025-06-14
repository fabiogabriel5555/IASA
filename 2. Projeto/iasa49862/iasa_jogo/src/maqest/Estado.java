package iasa_jogo.src.maqest;

import iasa_jogo.src.agente.Accao;
import iasa_jogo.src.ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

public class Estado {

    private Map<Evento, Transicao> transicoes;

    private String nome;

    public Estado(String nome)
    {
        this.nome = nome;

        this.transicoes = new HashMap<Evento, Transicao>();
    }

    public Transicao processar(Evento evento)
    {
        return transicoes.get(evento);
    }

    public String getNome(){return nome;}

    public Estado transicao(Evento evento, Estado estadoSucessor)
    {
        transicoes.put(evento, new Transicao(estadoSucessor, null));
        return this;
    }

    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accaoSucessor)
    {
        transicoes.put(evento, new Transicao(estadoSucessor, accaoSucessor));
        return this;
    }


}
