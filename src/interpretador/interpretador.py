class Interpretador:
    @staticmethod
    def carregar_arquivo(caminho):
        """
        Lê um arquivo de instruções e retorna um dicionário:
        {endereco: instrucao_32bits}
        """

        memoria_carregada = {}
        endereco_atual = 0  # padrão começa no endereço 0

        with open(caminho, "r") as f:
            for linha in f:
                linha = linha.strip()

                # Ignora linhas vazias
                if linha == "":
                    continue

                # Caso seja a diretiva "address XXXXX"
                if linha.startswith("address"):
                    partes = linha.split()
                    if len(partes) != 2:
                        raise ValueError(f"Diretiva inválida: {linha}")

                    endereco_atual = int(partes[1], 2)
                    continue

                # Caso seja uma instrução binária
                if all(c in "01" for c in linha) and len(linha) == 32:
                    instrucao = int(linha, 2)
                    memoria_carregada[endereco_atual] = instrucao
                    endereco_atual += 1
                else:
                    raise ValueError(f"Linha inválida encontrada: {linha}")

        return memoria_carregada
