package iasa_jogo.src.jogo.personagem;

import iasa_jogo.src.agente.Agente;
import iasa_jogo.src.jogo.ambiente.AmbienteJogo;

// * Esta classe representa um personagem dentro do jogo.

// * No diarama UML, esta classe Herda (seta contínua com ponta de seta vazada) Agente e Depende (setra tracejada) de ControloPersonagem
//   Dependências são relações nas quais uma parte utiliza ou depende de outra parte.

     // Herança de Agente (seta contínua com ponta de seta vazada):
        // Indica que Personagem é uma especialização de Agente.
        // É concretizada através de 'extends Agente' e de 'super(ambiente, new ControloPersonagem() );'

     // Dependência de AmbienteJogo (seta tracejada):
        // Esta dependencia é concretizada através do parâmetro 'AmbienteJogo ambiente' no construtor


public class Personagem extends Agente {

    // Construtor que inicializa um personagem dentro do ambiente de jogo.
    // O construtor chama `super()` para passar o ambiente e instanciar um ControloPersonagem.
    // Este metodo reflete a relação de dependência entre Personagem e AmbienteJogo.
    public Personagem(AmbienteJogo ambiente)
    {
        super(ambiente, new ControloPersonagem() );
    }
}
