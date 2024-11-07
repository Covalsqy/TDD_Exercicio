class Ocorrencia:
    def __init__(self, resp, tipo, prio, res, c):
        self.responsavel = resp
        
        self.tipos = ["BUG", "MELHORIA", "TAREFA"]
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            raise ValueError("São permitidos apenas os seguintes tipos de ocorrência: BUG, MELHORIA e TAREFA")
        
        self.prioridades = ["BAIXA", "MÉDIA", "ALTA"]
        if prio in self.prioridades:
            self.prioridade = prio
        else:
            raise ValueError("São permitidas apenas as seguintes prioriodades de ocorrência: BAIXA, MÉDIA e ALTA")
        
        self.resumo = res
        self.chave = c
        self.estado = "ABERTO"

    def get_responsavel(self):
        return self.responsavel

    def get_tipo(self):
        return self.tipo

    def get_prioridade(self):
        return self.prioridade

    def get_resumo(self):
        return self.resumo

    def get_chave(self):
        return self.chave

    def get_estado(self):
        return self.estado

    def fechar(self):
        if self.estado ==  "ABERTO":
            self.estado = "FECHADO"
            self.responsavel.decrease_count()
        else:
            raise PermissionError("Ocorrência já foi fechada")

    def trocar_responsavel(self, novo_res):
        self.responsavel.decrease_count()
        self.responsavel = novo_res
        self.responsavel.increase_count()

    def set_prioridade(self, p):
        self.prioridade = p
