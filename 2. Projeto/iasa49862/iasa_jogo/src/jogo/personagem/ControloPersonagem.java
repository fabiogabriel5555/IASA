package iasa_jogo.src.jogo.personagem;

import iasa_jogo.src.agente.Accao;
import iasa_jogo.src.agente.Controlo;
import iasa_jogo.src.agente.Percepcao;
import iasa_jogo.src.ambiente.Evento;
import iasa_jogo.src.jogo.ambiente.EventoJogo;
import iasa_jogo.src.maqest.Estado;
import iasa_jogo.src.maqest.MaquinaEstados;

import static iasa_jogo.src.jogo.ambiente.ComandoJogo.*;
import static iasa_jogo.src.jogo.ambiente.EventoJogo.*;




// * No diagrama UML, esta classe 'Depende' (seta tracejada) de Controlo. Isto significa que ControloPersonagem 'utiliza' ou 'depende' de Controlo.
//   Dependências são relações nas quais uma parte utiliza ou depende de outra parte.

     // Implementação da interface Controlo (seta tracejada com ponta de seta vazada):
        // Indica que ControloPersonagem é uma especialização ou implementação de Controlo.
        // Esta associação é concretizada através de 'implements Controlo'

     // Dependencia de Percepcao (seta tracejada):
        // Esta dependencia é concretizada no metodo 'processar(Percepcao percepcao){...}' que recebe como parametro Percepcao

    // Dependencia de Accao (seta tracejada):
        // Esta dependencia é concretizada no metodo 'processar(Percepcao percepcao){...}' que é do tipo Accao e retorna, obviamente, uma Accao


// * Esta classe implementa a interface Controlo e fornece um mecanismo para que o Personagem processe informações percebodas no ambiente e tome decisôes apropriadas.


// Maquina de estados:

   // Uma Máquina de Estados é um modelo matemático que descreve a evolução de um sistema ao longo do tempo em resposta a eventos

   // Um sistema pode ser descrito em termos de dinâmica e comportamento:
      // Dinâmica: Representa a evolução dos estados do sistema ao longo do tempo.
      // Comportamento: Define como o sistema age com base nas suas entradas e no estado interno.

    // A Maquina de Estados pode definida por:
       // Conjunto de Estados (Q): Representa todas as condições possíveis em que o sistema pode estar.
       // Conjunto de Eventos (Σ): São os estímulos externos que causam mudanças no estado do sistema.
       // Função de Transição (δ: Q × Σ → Q): Define para qual estado o sistema deve transitar ao receber um evento.
       // Função de Saída (λ: Q × Σ → Z): Define qual ação o sistema executa ao processar um evento.

    // A Maquina de estado pode ser de dois tipos:
       // Máquina de Mealy: A saída depende tanto do estado atual quanto do evento recebido.
       // Máquina de Moore: A saída depende apenas do estado atual.

// Estados:

    // Os estados representam as diferentes situações que um sistema pode assumir durante a sua operação. No nosso caso, os estados da personagem são:
       // Procura: A personagem está procurando animais no ambiente.
       // Inspecção: A personagem ouviu um ruído e está investigando a origem.
       // Observação: A personagem encontrou um animal e está observando seu comportamento.
       // Registo: A personagem está tirando uma foto do animal.

    // Um estado pode mudar para outro com base em eventos do ambiente

// Transições:

// As transições definem as mudanças entre os estados. Elas ocorrem quando um evento do ambiente é detectado.
// No jogo, a personagem muda de estado conforme os seguintes eventos ocorrem:
    // Procura → Observação quando detecta um animal.
    // Procura → Inspecção quando detecta um ruído.
    // Observação → Registo quando o animal permanece.
    // Registo → Procura quando a foto é tirada ou o animal foge.

// Cada transição pode estar associada a uma ação específica

// Ações:

    // Uma ação é o comportamento executado pela personagem durante ou após uma transição de estado.
    // No jogo, as ações são:
        // Procurar (PROCURA)
        // Aproximar-se (APROXIMAR)
        // Observar (OBSERVAR)
        // Fotografar (FOTOGRAFAR)

// Cada ação pode ser associada a uma transição. Por exemplo, quando a personagem detecta um animal, a transição Procura → Observação executa a ação Aproximar

public class ControloPersonagem implements Controlo {

    // Este atributo representa a Máquina de Estados que controlará a personagem. Essa máquina de estados será responsável por gerenciar os estados, transições e ações da personagem.
    private MaquinaEstados estados;

    // Construtor de ControloPersonagem.
    public ControloPersonagem()
    {

        // Aqui são criados objetos do tipo Estado, representando os diferentes estados possíveis da FSM da personagem.
           // Cada estado armazena um nome, que identifica a fase do jogo em que a personagem se encontra.
           // Esses estados serão utilizados para definir as transições.
        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspecção");
        Estado observacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        // Cada objeto da classe Accao representa uma ação que a personagem pode executar.
           // Essas ações estão diretamente relacionadas com os estados e transições.
           // Ex: Quando a personagem detecta um animal, ela transita para Observação e executa a ação Aproximar.
        Accao procurar = new Accao(PROCURAR);
        Accao aproximar = new Accao(APROXIMAR);
        Accao observar = new Accao(OBSERVAR);
        Accao fotografar = new Accao(FOTOGRAFAR);


        // Cada estado recebe transições que definem para qual estado a personagem deve ir ao detectar um evento.

        // Se a personagem encontra um animal (ANIMAL), transita de Procura para Observação e executa Aproximar.
        // Se a personagem detecta um ruído (RUIDO), muda para Inspecção e também executa Aproximar.
        // Se o ambiente está silencioso (SILENCIO), continua em Procura e repete a ação Procurar.
        procura
                .transicao(ANIMAL, observacao, aproximar)
                .transicao(RUIDO,  inspeccao,  aproximar)
                .transicao(SILENCIO, procura,    procurar);

        // Se o ambiente ficar silencioso (SILENCIO), a personagem volta para Procura.
        // Se encontra um animal (ANIMAL), transita para Observação e executa Aproximar.
        // Se ainda há ruído (RUIDO), continua investigando (Inspecção) e executa Procurar.
        inspeccao
                .transicao(SILENCIO, procura, null)
                .transicao(ANIMAL,   observacao,  aproximar)
                .transicao(RUIDO,  inspeccao,  procurar);

        // Se o animal continua presente, muda para Registo e executa Observar.
        // Se o animal foge, volta para Inspecção para investigar.
        observacao
                .transicao(ANIMAL, registo, observar)
                .transicao(FUGA,   inspeccao,  null);

        // Se o animal fugir, a personagem volta para Procura.
        // Se a personagem tirar uma foto, retorna para Procura.
        // Se o animal continuar lá, ela continua no estado Registo e tira a fotografia.
        registo
                .transicao(FUGA, procura, null)
                .transicao(FOTOGRAFIA,  procura,  null)
                .transicao(ANIMAL, registo,    fotografar);

        // Aqui, a Maquina de Estados é criada e inicializada com o estado inicial Procura.
        estados = new MaquinaEstados(procura);
    }

    // Metodo responsável por processar uma perceção e decidir qual ação tomar.
    // Implementa 'processar()' da interface Controlo.
    @Override
    public Accao processar(Percepcao percepcao)
    {
        // Obtém o evento percebido pelo agente no ambiente.
        Evento evento = percepcao.getEvento();

        // Processa o evento através da Máquina de Estados e obtem assim a ação
        Accao accao = estados.processar(evento);

        // Imprime no console o estado atual da personagem.
        mostrar();

        // Retorna a ação escolhida pela Máquina de Estados, que será executada pela personagem no jogo.
        return accao;
    }

    // Metodo responsável por exibir informações sobre a decisão tomada pelo controlo do personagem.
    private void mostrar()
    {
        System.out.println( "Estado: " + getEstado().getNome() );
    }

    // Metodo responsável por retornar o estado atual da maquina de estados
    public Estado getEstado()
    {
        return this.estados.getEstado();
    }
}
