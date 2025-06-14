from agente.agente_delib import AgenteDelib
from agente.agente_delib_pdm import AgenteDelibPDM
from agente.agente_reactivo import AgenteReactivo
from sae import Simulador

"""
    Script para executar uma simulação de um agente deliberativo em um ambiente controlado. 
"""

# Bloco para testes.
if __name__ == "__main__":

    # Instancia um agente deliberativo.
    agente = AgenteDelibPDM()

    # Instancia um simulador com dimensão 4, o agente deliberativo e visualização do modelo ativada.
    simulador = Simulador(4, agente, vista_modelo=True)

    # Executa a simulação.
    simulador.executar()
