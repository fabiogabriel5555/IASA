package iasa_jogo.src.ambiente;

// * No diagrama UML, esta interface tem 'Dependências' (setas tracejadas) com Evento e Comando. Isto significa que Ambiente 'utiliza' ou 'depende' dessas entidades.
//   Dependências são relações nas quais uma parte utiliza ou depende de outra parte, por exemplo, uma classe tem um metodo com um parâmetro que é uma instância de outra classe, ou cria localmente uma instância de outra classe
//   Essa dependendia é concretizada através dos métodos 'observar()' e 'executar(Comando comando)', os quais utilizam intencias de Evento e Comando respectivamente.


// * Conceitualmente, o ambiente pode ter as seguintes características:

    // Discreto ou Contínuo: O ambiente pode ser composto por estados bem definidos ou valores contínuos.

    // Determinístico ou Estocástico: O estado futuro pode ser previsível ou conter elementos de incerteza.

    // Estático ou Dinâmico: O ambiente pode mudar independentemente do agente.

    // Totalmente ou Parcialmente observável: O agente pode ter acesso completo ou parcial ao estado do ambiente.

    // Multiagente: O ambiente pode ser compartilhado por múltiplos agentes.


// * Esta interface representa o mundo onde os agentes operam.


// * Esta interface serve para:

    // Defenir a interface que o agente usa para interagir com o ambiente.

    // Evoluir com o tempo, garantindo que o ambiente não seja estático (evolulir()).

    // Fornecer perceções ao agente, permitindo que ele reaja (observar()).

    // Permitir modificar o ambiente, aplicando comandos (executar(Comando comando)).

public interface Ambiente {

    // Este metodo representa a evolução do ambiente com o tempo.
    public void evoluir();

    // Este metodo permite que um agente obtenha informações do ambiente.
    // Retorna um objeto Evento, que representa uma mudança observável no ambiente.
    public Evento observar();

    // Este metodo aplica um comando no ambiente, alterando seu estado.
    public void executar(Comando comando);
}
