class Processador:
    def __init__(self):
        # 32 registradores de 32 bits
        self.regs = [0] * 32
        
        # Flags
        self.flag_neg = 0
        self.flag_zero = 0
        self.flag_carry = 0
        self.flag_overflow = 0

        # Program Counter e Instruction Register
        self.pc = 0
        self.ir = 0

        # Memória de 64K palavras (endereçada a palavra)
        self.memoria = [0] * 65536

        # Controle interno
        self.halted = False

    def carregar_programa(self, memoria_carregada):
        """Recebe um dicionário {endereco: instrucao_binaria} do interpretador."""
        for endereco, instrucao in memoria_carregada.items():
            self.memoria[endereco] = instrucao

    def ciclo_IF(self):
        """Busca da instrução"""
        self.ir = self.memoria[self.pc]
        self.pc += 1

    def ciclo_ID(self):
        """Decodificação – não altera estado diretamente"""
        pass

    def ciclo_EX(self):
        """Execução – executa a instrução"""
        pass

    def ciclo_WB(self):
        """Write Back – escreve resultados em registradores"""
        pass

    def executar_ciclo(self):
        """Executa os 4 estágios de uma instrução"""
        if self.halted:
            return

        self.ciclo_IF()
        self.ciclo_ID()
        self.ciclo_EX()
        self.ciclo_WB()

        # Detecção de HALT
        if self.ir == 0xFFFFFFFF:
            self.halted = True
