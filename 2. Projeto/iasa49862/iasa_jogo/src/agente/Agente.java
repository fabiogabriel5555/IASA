package iasa_jogo.src.agente;

import iasa_jogo.src.ambiente.*;

// * No diagrama UML, esta classe tem 'Associações' (setas continuas) com ambiente e controlo. Isto significa que Agente esta associado a ambiente e controlo
//   Associações (setas continuas) são Relações na qual uma parte está estruturalmente associada a outra parte atravéz de um dos seus atributos, ou seja, um dos ses atributos tem informações acerca da outra parte
//   Composições (seta contínua com losango preenchido) são casos paarticulares de associações que indicam que uma parte é composta por outras partes que só existem no contexto da parte composta. Por exemplo, a relação entre apartamento e divisão (o apartamento é composto por várias divisões que não existem separadas do todo).

     // Associação com Ambiente (seta continua):
         // Esta associação indica que Agente 'utiliza' ou 'interage' com Ambiente
         // Esta associação é concretizada no atributo ambiente 'private Ambiente ambiente;' (que é do tipo Ambiente)

     // Composição com Controlo (seta contínua com losango preenchido):
         // Esta composição é indica que Agente 'é composto' por um Controlo. Controlo não pode existir sem Agente
         // Esta composição é concretizada no atributo controlo 'private Controlo controlo;' (que é do tipo Controlo)


// * Conceitualmente, um Agente é a implementação do modelo de agente inteligente. Um agente:

    // Percebe o ambiente (percepcionar()).

    // Processa a perceção e decide o que fazer (Controlo).

    // Atua no ambiente (actuar(Accao accao)).


// * Esta classe serve para:

    // Atuar como um personagem/jogador em um jogo.

    // Pode ser controlado por IA para tomar decisões.


public class Agente {

    private Ambiente ambiente; // Associação: Agente interage com o ambiente
    private Controlo controlo; // Composição: Agente contém controlo

    // Metodo construtor que recebe um ambiente e um controlo, associando-os ao agente.
    public Agente(Ambiente ambiente, Controlo controlo)
    {
        // Representa o ambiente onde o agente opera.
        this.ambiente = ambiente;

        // Responsável por processar percepções e decidir ações.
        this.controlo = controlo;
    }

    // Metodo principal do agente, que executa o ciclo percepção-processamento-ação.
    // Este metodo implementa o ciclo de vida do agente seguindo a estrutura:
       // Perceber (percepcionar()) → O agente observa o ambiente e coleta informações.
       // Decidir (controlo.processar(percepcao)) → O agente usa sua lógica de controle para determinar uma ação apropriada.
       // Agir (actuar(accao)) → A ação escolhida é executada no ambiente.
    public void executar()
    {
        // Obtém uma perceção do ambiente
        Percepcao percepcao = percepcionar();

        // Processa a perceção para decidir a ação
        Accao accao = controlo.processar(percepcao);

        // Executa a ação no ambiente
        actuar(accao);
    }

    // Metodo que retorna uma perceção do ambiente.
    // Tem como objetivo observar o ambiente e criar uma percepção para o agente.
    protected Percepcao percepcionar()
    {
        // Obtém um evento do ambiente
        Evento evento = this.ambiente.observar();

        // Cria uma perceção baseada no evento
        return new Percepcao(evento);
    }

    // Metodo responsável por executar uma ação no ambiente.
    // Temo como objetivo executar a ação escolhida pelo controle no ambiente.
    protected void actuar(Accao accao)
    {
        if(accao != null)
        {
            // Obtém o comando associado à ação
            Comando comando = accao.getComando();

            // Envia o comando para o ambiente
            this.ambiente.executar( comando );
        }
    }


}
