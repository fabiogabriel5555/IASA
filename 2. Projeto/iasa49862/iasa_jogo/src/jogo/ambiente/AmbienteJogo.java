package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.*;

import java.util.HashMap;
import java.util.Scanner;

// * No diagrama UML, esta classe tem 'Dependências' (setas tracejadas) e 'Associações' (setas continuas) Ambiente, EventoJogo e ComandoJogo. Isto significa que Ambiente 'utiliza' e 'esta associado' a essas entidades e classes.
//   Dependências (setas tracejadas) são relações nas quais uma parte utiliza ou depende de outra parte, por exemplo, uma classe tem um metodo com um parâmetro que é uma instância de outra classe, ou cria localmente uma instância de outra classe
//   Por outro lado, Associações (setas continuas) são Relações na qual uma parte está estruturalmente associada a outra parte atravéz de um dos seus atributos, ou seja, um dos ses atributos tem informações acerca da outra parte

     // Dependencia ou Herança (seta tracejada) de Ambiente :
        // Esta dependencia ou herança indica que AmbienteJogo é uma especialização ou concretização de Ambiente.
        // É concretizada em 'implements Ambiente'

     // Dependencia de ComandoJogo (seta tracejada):
        // Esta dependencia indica que AmbienteJogo 'usa' comandos especificos do jogo sem armazená-los como atributos.
        // É concretizada no metodo 'public void executar(Comando comando) {...}'

    // Associação com EventoJogo (seta continua e {read-only} ):
        // Esta dependencia indica que AmbienteJogo contém e pode gerar múltiplos eventos do tipo EventoJogo.
        // A marcação `{read-only}` significa que os eventos podem ser lidos pelo ambiente, mas não modificados externamente.
        // É concretizada no metodo 'public EventoJogo getEvento() {...}'

    // Composição com EventoJogo (seta continua com losango preenchido):
        // Esta dependencia indica que um EventoJogo faz parte de AmbienteJogo e não pode existir sem ele.
        // É concretizada no metodo 'private EventoJogo gerarEvento() {...}'


// * Esta classe é uma implementação da interface Ambiente.

// * Representa um ambiente virtual, onde agentes podem interagir e realizar ações.

// * Esta classe serve para:

    // Garantir a evolução do ambiente (evoluir()), permitindo mudanças no estado do jogo.

    // Permitir que agentes percebam eventos (observar()).

    // Executar comandos (executar(Comando comando)), alterando o estado do jogo.

    // Gerar eventos internos (gerarEvento()), criando situações que os agentes podem precisar lidar.


public class AmbienteJogo implements Ambiente {

    private EventoJogo evento;
    private HashMap<String, EventoJogo> eventos;

    private Scanner scanner;

    // Este construtor inicializa um ambiente de jogo.
    // O HashMap 'eventos' foi criado para converter ou mapear a entra de string (por pate do utilizador) em eventos do jogo.
    // Essa abordagem evita o uso de multiplos 'if-else' e facilita a adição de novos eventos
    public AmbienteJogo()
    {
        // Inicializa o Scanner para ler entradas do utilizador no terminal.
        this.scanner = new Scanner(System.in);

        // Cria um HashMap que mapeará strings para eventos do jogo.
        this.eventos = new HashMap<String, EventoJogo>();

        // Associa entradas do utilizador a eventos do jogo.
        eventos.put("s", EventoJogo.SILENCIO);
        eventos.put("r", EventoJogo.RUIDO);
        eventos.put("a", EventoJogo.ANIMAL);
        eventos.put("f", EventoJogo.FUGA);
        eventos.put("o", EventoJogo.FOTOGRAFIA);
        eventos.put("t", EventoJogo.TERMINAR);
    }


    // Representa a evolução do ambiente ao longo do tempo.
    // Implementa 'evoluir()' da interface Ambiente, garantindo que o ambiente possa mudar dinamicamente.
    // Atualiza o evento atual do ambiente através do metodo 'gerarEvento', o que garante que o ambiente reage a mudanças dentro do jogo
    @Override
    public void evoluir()
    {
        this.evento = gerarEvento();
    }


    // Este metodo permite que os agentes percebam eventos no ambiente e tomem decisões baseadas no estado atual do ambiente.
    // Implementa 'observar()' da interface Ambiente, e reflete a associação '{read-only}' entre AmbienteJogo e EventoJogo.
    // Se houver um evento, ele é exibido e retornado; caso contrário, retorna 'null'.
    @Override
    public Evento observar()
    {
        // Verifica se há um evento ativo no ambiente.
        if(evento != null)
        {
            // Exibe o evento atual no ecrã.
            evento.mostrar();

            // Retorna o evento para que o agente possa tomar decisões baseadas nele.
            return evento;
        }
        else
        {
            return null;
        }
    }

    // Este metodo executa ações no ambiente, alterando seu estado.
    // Implementa 'executar()' da interface Ambiente, e reflete a 'dependência' entre AmbienteJogo e ComandoJogo.
    // Exibe o comando que foi executado, permitindo que o jogador visualize as suas ações.
    @Override
    public void executar(Comando comando)
    {
        comando.mostrar();
    }


    // Este metodo privado é usado para criar eventos dentro do jogo.
    // Este metodo reflete a **associação `{read-only}`** entre AmbienteJogo e EventoJogo.
    // Pede ao utilizador que insira um evento (comando) e procura no HashMap o evento correspondente, o que permite que os eventos sejam gerados de maneira dinâmica e controlada.
    private EventoJogo gerarEvento()
    {
        // Exibe a mensagem pedindo uma entrada do utilizador
        System.out.println("Evento ?");

        // Lê a entrada do utilizador no terminal.
        String codigoEvento = scanner.next();

        // // Retorna o evento correspondente ao código digitado.
        return eventos.get(codigoEvento);
    }


    // Este metodo fornece uma forma segura de consultar o evento que ocorreu no ambiente de jogo. Permite que outros componentes do sistema (ex: agentes) possam observar o estado atual do ambiente sem alterar diretamente sua lógica interna.
    // No diagrama, a variável evento está marcada como `{read only}`, o que significa que ela só pode ser lida, mas não modificada externamente.
    // Como Java não tem um modificador específico para {read only}, usa-se um getter sem setter para garantir essa restrição.
    public EventoJogo getEvento() { return this.evento; }

}

