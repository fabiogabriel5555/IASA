package iasa_jogo.src.jogo;

import iasa_jogo.src.jogo.ambiente.AmbienteJogo;
import iasa_jogo.src.jogo.personagem.Personagem;

import static iasa_jogo.src.jogo.ambiente.EventoJogo.*;

// * No diagrama UML, esta classe é Composta (seta continua com losangulo preenchido) pelo AmbienteJogo e Personagem
//   Composição é um caso  particular de associação que indica que uma parte é composta por outras partes que só existem no contexto da parte composta, por exemplo, a relação entre apartamento e divisão (o apartamento é composto por várias divisões que não existem separadas do todo)

     // Composição pelo Personagem (seta continua com losangulo preenchido):
        // Indica que Jogo contém um Personagem.
        // É concretizada pelo atributo 'private static Personagem personagem;' e pela inicialização desse mesmo atributo no construtor 'personagem = new Personagem(ambiente);'

     // Composição pelo AmbienteJogo (seta continua com losangulo preenchido):
        // Indica que Jogo contém um AmbienteJogo.
        // É concretizada pelo atributo 'private static AmbienteJogo ambiente;' e pela inicialização desse mesmo atributo no construtor 'ambiente = new AmbienteJogo();'


// * Esta classe gerencia a execussão do jogo, garantindo que o personagem interaja continuamente com o ambiente até a finalização do jogo

public class Jogo {

    // Esses dois atributos são estáticos, pois o jogo tem apenas um ambiente e um personagem durante toda a execução.

    // Representa o agente principal que interage com o ambiente.
    private static Personagem personagem;

    // Representa o ambiente onde o jogo acontece\.
    private static AmbienteJogo ambiente;

    // Metodo principal que inicia o jogo e os seus componentes.
    // Cria o ambiente e o personagem antes de iniciar o loop de execução.
    public static void main(String[] args)
    {
        // Inicializa o ambiente do jogo
        ambiente = new AmbienteJogo();

        // Inicializa o personagem e o associa ao ambiente
        personagem = new Personagem(ambiente);

        // Inicia o loop principal do jogo
        executar();
    }

    // Metodo responsavel por controlar a execução contínua do jogo.
    // No UML, essa operação é modelada no 'diagrama de sequência'.
    // O loop continua até que o evento atual do ambiente seja TERMINAR.
    // Em cada iteração:
    //     *   1. O ambiente evolui ('ambiente.evoluir()').
    //     *   2. O personagem executa uma ação ('personagem.executar()').
    // Fluxo do jogo:
       // O ambiente evolui (ambiente.evoluir();): Isso pode gerar novos eventos, como um animal aparecer ou um ruído ser detectado.
       // O personagem executa uma ação (personagem.executar();): O personagem percebe o ambiente, decide o que fazer e executa a ação correspondente.
       // O loop continua enquanto o evento do ambiente for diferente de TERMINAR.
    private static void executar()
    {
        do
        {
            // O ambiente muda seu estado
            ambiente.evoluir();

            // O personagem age no novo estado do ambiente
            personagem.executar();
        }

        // Continua enquanto o evento não for TERMINAR
        while(ambiente.getEvento() != TERMINAR);
    }

}
