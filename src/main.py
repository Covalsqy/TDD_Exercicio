class Empresa:
    def __init__(self, name):
        self.nome = name
        self.lista_funcionarios = []
        self.lista_projetos = []
        self.dicionario_projetos = {}
        self. dicionario_ocorrencias = {}

    def get_funcionarios(self):
        return self.lista_funcionarios

    def get_funcionario(self, n):
        return self.lista_funcionarios[n-1]

    def get_projetos(self):
        return self.lista_projetos

    def get_ocorrencia(self, chave):
        return self.dicionario_ocorrencias[chave]

    def get_responsavel(self, chave):
        return self.get_ocorrencia(chave).get_responsavel()

    def get_estado_ocorrencia(self, chave):
        return self.get_ocorrencia(chave).get_estado()

    def adicionar_funcionario(self, f):
        if f not in self.lista_funcionarios:
            f.id = len(self.lista_funcionarios) + 1
            self.lista_funcionarios.append(f)
        else:
            raise Exception("Funcionário já está na empresa")

    def criar_projeto(self, p):
        id = len(self.dicionario_projetos) + 1
        novo_projeto = Projeto(p, id)
        self.lista_projetos.append(novo_projeto)
        self.dicionario_projetos[id] = []

    def atribuir_funcionario_a_projeto(self, id_f, id_p):
        funcionario = self.get_funcionario(id_f)
        self.dicionario_projetos[id_p].append(funcionario)

    def criar_ocorrencia(self, id_p, id_f, tipo, prioridade, resumo):
        if id_p > len(self.dicionario_projetos) or id_p < 1:
            raise Exception("Projeto não existe")
        if self.lista_funcionarios[id_f-1] not in self.dicionario_projetos[id_p]:
            raise Exception("Funcionário não faz parte do projeto")
        chave = str(id_p) + "_" + str(len(self.dicionario_ocorrencias) + 1)
        nova_o = Ocorrencia(self.get_funcionario(id_f), tipo, prioridade, resumo, chave)
        self.dicionario_ocorrencias[chave] = nova_o

    def fechar_ocorrencia(self, chave):
        self.dicionario_ocorrencias[chave].fechar()

    def trocar_responsavel_ocorrencia(self, chave_o, novo_res):
        id_p = chave_o.split("_")
        id_p = int(id_p[0])
        if self.lista_funcionarios[novo_res-1] not in self.dicionario_projetos[id_p]:
            raise Exception("Funcionário não faz parte do projeto")
        ocorrencia = self.get_ocorrencia(chave_o)
        if ocorrencia.get_estado() == "ABERTO":
            ocorrencia.trocar_responsavel(self.lista_funcionarios[novo_res-1])
        else:
            raise Exception("Não pode alterar responsável de ocorrência fechada")

class Funcionario:
    def __init__(self, name):
        self.nome = name
        self.id = 0

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id

class Projeto:
    def __init__(self, t, n):
        self.titulo = t
        self.id = n

    def get_titulo(self):
        return self.titulo

class Ocorrencia:
    def __init__(self, resp, tipo, prio, res, c):
        self.responsavel = resp
        self.tipo = tipo
        self.prioridade = prio
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
        else:
            raise Exception("Ocorrência já foi fechada")

    def trocar_responsavel(self, novo_res):
        self.responsavel = novo_res
