package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Evento;

// * No diagrama UML, este Enum 'Depende' (seta tracejada) de Evento. Isto significa que ComandoJogo 'utiliza' ou 'Depende' de Evento
//   Dependências são relações nas quais uma parte utiliza ou depende de outra parte, por exemplo, uma classe tem um metodo com um parâmetro que é uma instância de outra classe, ou cria localmente uma instância de outra classe

     // Dependencia ou Herança (seta tracejada) de Evento :
        // Esta dependencia ou herança indica que EventoJogo é uma especialização ou concretização de Evento.
        // É concretizada em 'implements Evento'


// * Este Enum representa os eventos disponíveis.


// * Este Enum define os eventos possíveis que ocorrem no ambiente permitindo que o jogo funcione com uma lógica estruturada de estados


public enum EventoJogo implements Evento {


    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;

    // Este metodo é responsável por exibir ou mostrar o evento ocorrido.
    // Implementa 'mostrar()' da interface Evento.
    @Override
    public void mostrar()
    {
        System.out.printf("\nEvento: %s\n", this);
    }
}
