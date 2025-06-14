package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.*;

// * No diagrama UML, esta classe está 'Associaciada' (seta continua) a Evento. Isto significa que Percepcao esta associado a Evento.
//   Associações (setas continuas) são Relações na qual uma parte está estruturalmente associada a outra parte atravéz de um dos seus atributos, ou seja, um dos ses atributos tem informações acerca da outra parte

     // Associação com Evento (seta continua e {read-only}):
        // Esta associação indica que Percepcao 'utiliza' ou 'interage' com Evento, mas este não pode ser modificado.
        // Esta associação é concretizada no atributo evento 'private Evento evento;' (que é do tipo Evento)


// * A perceção (Percepcao) contém informações sobre o estado atual do ambiente, como a presença de um animal, um ruído ou silênc


// * Esta classe serve para encapsular a informação que o agente recebe do ambiente.


// * Esta classe serve para:

    // Permitir que o agente obtenha eventos do ambiente.

    // Ser estendida para conter múltiplas informações (exemplo: posição do agente, objetos próximos).

public class Percepcao {


    private Evento evento; // Associação: Percepccao interage com o Evento

    // Metodo construtor que recebe evento
    public Percepcao(Evento evento){this.evento = evento;}

    // Este metodo serve para retornar o evento percebido pelo agente. Permite que o agente analise a situação atual do ambiente antes de tomar uma decisão.
    // No diagrama UML, na associação entre Percepcao e Eveno existe a indicação {read-only}, o que significa que evento não pode ser alterado
    // Este foi criado exclusivamente para permitir o acesso a event sem que possa ser modificado
    public Evento getEvento(){return evento;}

}
