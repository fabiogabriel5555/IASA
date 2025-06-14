package iasa_jogo.src.ambiente;

// * No diagrama UML, esta interface não 'utiliza' ou 'depende' diretamente de outras entidades.
//   Daí não ter nenhuma dependencia, o que permite que multiplos eventos sejam implmentados de forma independente


// * Esta interface representa uma mudança de estado no ambiente. Eventos podem ser:

    // Um objeto a mover-se

    // Um inimigo aparecer

    // O clima mudar


// * Esta interface representa uma mudança de estado no ambiente.


// * Esta interface serve para:

    // Permitir que os agentes percebam mudanças no ambiente.

    // Possibilitar a modelação de eventos complexos (como sequências de ações interligadas).

    // Facilitar a programação de sistemas baseados em eventos.

public interface Evento {

    // Este metodo serve para exibir informações sobre o evento
    public void mostrar();
}
