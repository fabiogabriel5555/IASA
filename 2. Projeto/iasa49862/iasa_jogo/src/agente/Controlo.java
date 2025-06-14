package iasa_jogo.src.agente;

// * No diagrama UML, esta interface tem 'Dependências' (setas tracejadas) com Percepcao e Accao. Isto significa que Controlo 'utiliza' ou 'depende' dessas entidades.
//   Dependências são relações nas quais uma parte utiliza ou depende de outra parte.
//   Por exemplo, uma classe tem um metodo com um parâmetro que é uma instância de outra classe, ou cria localmente uma instância de outra classe

     // Dependencia de Percepcao (seta tracejada): Esta dependencia é concretizada no metodo processar 'public Accao processar(Percepcao percepcao);', que recebe Percepcao como parametro

     // Dependencia de Accao (seta tracejada): Esta dependencia é concretizada no metodo processar 'public Accao processar(Percepcao percepcao);', que é do tipo Accao


// Em um agente reativo, a decisão é imediata. Em um agente deliberativo, a decisão pode envolver planejamento.


// * Esta interface define o mecanismo de decisão do agente


// * Esta interface serve para:

    // Implementar a lógica de tomada de decisão.

    // Em um agente reativo, podera retornar ações imediatas.

    // Em um agente deliberativo, poderia calcular um plano antes de agir.

public interface Controlo {

    // Este metodo recebe uma perceção (Percepcao) e decide qual ação (Accao) deve ser tomada.
    public Accao processar(Percepcao percepcao);
}
