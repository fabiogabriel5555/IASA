package iasa_jogo.src.ambiente;

// * No diagrama UML, esta interface não 'utiliza' ou 'depende' diretamente de outras entidades.
//   Daí não ter nenhuma dependencia, o que permite que multiplos comandos sejam implmentados de forma independente


// * Conceitualmente, cada comando encapsula uma ação específica.


// * Esta interface serve para representar ações que podem ser realizadas no ambiente.


// * Esta interface serve para:

    // Representar ações que modificam o estado do ambiente.

    // Ser implementada para definir diferentes tipos de comandos


public interface Comando {

    // Este metodo serve para exibir informações sobre o comando
    public void mostrar();

}
