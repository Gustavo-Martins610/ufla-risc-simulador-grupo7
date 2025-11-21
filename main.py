from src.interpretador.interpretador import Interpretador
from src.simulador.processador import Processador

def main():
    caminho = "exemplos/programa1.txt"   # arquivo de teste
    print(f"Carregando '{caminho}'...")

    # 1. Interpretador lê o programa
    memoria = Interpretador.carregar_arquivo(caminho)

    # 2. Carrega no processador
    cpu = Processador()
    cpu.carregar_programa(memoria)

    print("Programa carregado. Executando...\n")

    # 3. Executa ciclos até HALT
    while not cpu.halted:
        cpu.executar_ciclo()

    print("\nExecução finalizada!")

if __name__ == "__main__":
    main()
