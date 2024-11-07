from projeto import Projeto
from ocorrencia import Ocorrencia

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

    def get_prioridade_ocorrencia(self, chave):
        return self.get_ocorrencia(chave).get_prioridade()

    def adicionar_funcionario(self, f):
        if f not in self.lista_funcionarios:
            f.id = len(self.lista_funcionarios) + 1
            self.lista_funcionarios.append(f)
        else:
            raise PermissionError("Funcionário já está na empresa")

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
            raise ValueError("Projeto não existe")
        if id_f > len(self.lista_funcionarios) or id_f < 1:
            raise ValueError("Funcionário não existe")
        if self.lista_funcionarios[id_f-1] not in self.dicionario_projetos[id_p]:
            raise PermissionError("Funcionário não faz parte do projeto")
        if self.lista_funcionarios[id_f-1].get_count() == 10:
            raise PermissionError("Funcinário atingiu limite de ocorrências")
        chave = str(id_p) + "_" + str(len(self.dicionario_ocorrencias) + 1)
        nova_o = Ocorrencia(self.get_funcionario(id_f), tipo, prioridade, resumo, chave)
        
        for key in self.dicionario_ocorrencias:
            if nova_o.get_responsavel() == self.dicionario_ocorrencias[key].get_responsavel() and nova_o.get_tipo() == self.dicionario_ocorrencias[key].get_tipo() and nova_o.get_prioridade() == self.dicionario_ocorrencias[key].get_prioridade() and nova_o.get_resumo() == self.dicionario_ocorrencias[key].get_resumo() and key[0] == chave[0]:
                raise ValueError("Não pode criar uma ocorrência igual a uma já existente no mesmo projeto")    
    
        self.dicionario_ocorrencias[chave] = nova_o
        self.lista_funcionarios[id_f-1].increase_count()
        return nova_o

    def fechar_ocorrencia(self, chave):
        self.dicionario_ocorrencias[chave].fechar()

    def trocar_responsavel_ocorrencia(self, chave_o, novo_res):
        id_p = chave_o.split("_")
        id_p = int(id_p[0])
        if self.lista_funcionarios[novo_res-1].get_count() == 10:
            raise PermissionError("Funcinário atingiu limite de ocorrências")
        else:
            if self.lista_funcionarios[novo_res-1] not in self.dicionario_projetos[id_p]:
                raise PermissionError("Funcionário não faz parte do projeto")
            else:
                ocorrencia = self.get_ocorrencia(chave_o)
                if ocorrencia.get_estado() == "ABERTO":
                    ocorrencia.trocar_responsavel(self.lista_funcionarios[novo_res-1])
                else:
                    raise PermissionError("Não pode alterar responsável de ocorrência fechada")

    def alterar_prioridade(self, chave, p):
        if self.get_ocorrencia(chave).get_estado() == "ABERTO":
            self.get_ocorrencia(chave).set_prioridade(p)
        else:
            raise PermissionError("Não pode alterar prioridade de ocorrencia fechada")
