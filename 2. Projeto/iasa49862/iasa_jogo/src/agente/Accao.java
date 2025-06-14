package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.Comando;

// * No diagrama UML, esta classe está 'Associaciada' (seta continua) a Comando. Isto significa que Accao esta associado a Comando.
//   Associações (setas continuas) são Relações na qual uma parte está estruturalmente associada a outra parte atravéz de um dos seus atributos, ou seja, um dos ses atributos tem informações acerca da outra parte

     // Associação com Comando (seta continua e {read-only}):
        // Esta associação indica que Accao 'utiliza' ou 'interage' com Comando, mas este não pode ser modificado.
        // Esta associação é concretizada no atributo accao 'private Accao accao;' (que é do tipo Accao)


// * Ações são a última etapa do ciclo percepção-processamento-ação.


// * Esta classe representa ações que o agente pode executar.


// * Esta classe serve para:

    // Definir comandos que alteram o ambiente.

    // Relacionar-se com sistemas baseados em planejamento.


public class Accao {

    private Comando comando; // Associação: Accao interage com o Comando

    // Metodo construtor que recebe comando
    public Accao(Comando comando){this.comando = comando;}

    // Este metodo serve para retornar o comando associado a ação.
    // No diagrama UML, na  associação entre Accao e Comando, existe a indicação `{read-only}`, o que significa que o comando não pode ser alterado.
    // Este metodo foi criado exclusivamente para permitir o acesso ao comando sem que ele possa ser modificado.
    public Comando getComando(){return this.comando;}

}
