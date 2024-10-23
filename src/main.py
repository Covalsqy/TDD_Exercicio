class Empresa:
    def __init__(self, name):
        self.nome = name
        self.lista_funcionarios = []
        self.lista_projetos = []
        self.dicionario_projetos = {}

    def get_funcionarios(self):
        return self.lista_funcionarios

    def get_funcionario(self, n):
        return self.lista_funcionarios[n-1]

    def get_projetos(self):
        return self.lista_projetos

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
