package iasa_jogo.src.jogo.ambiente;

import iasa_jogo.src.ambiente.Comando;

// * No diagrama UML, este Enum 'Depende' (seta tracejada) de Comando. Isto significa que ComandoJogo 'utiliza' ou 'Depende' de Comando
//   Dependências são relações nas quais uma parte utiliza ou depende de outra parte, por exemplo, uma classe tem um metodo com um parâmetro que é uma instância de outra classe, ou cria localmente uma instância de outra classe

     // Dependencia ou Herança (seta tracejada) de Comando :
        // Esta dependencia ou herança indica que ComandoJogo é uma especialização ou concretização de Comando.
        // É concretizada em 'implements Comando'


// * Este Enum representa os comandos disponíveis para o personagem interagir com o ambiente.


// * Este Enum define os comandos que o jogador pode executar, garantindo que as ações sejam limitadas a valores predefinidos.


public enum ComandoJogo implements Comando {

    // * Este Enum representa os comandos disponíveis para o personagem interagir com o ambiente

    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    // Este metodo é responsável por exibir ou mostrar o comando executado
    // Implementa 'mostrar()' da interface Comando.
    @Override
    public void mostrar()
    {
        System.out.printf("Ação: %s\n", this + "\n");
    }
}
