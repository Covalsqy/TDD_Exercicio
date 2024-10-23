class Empresa:
    def __init__(self, name):
        self.nome = name
        self.lista_funcionarios = []
        self.lista_projetos = []

    def get_nome(self):
        return self.nome

    def get_funcionarios(self):
        return self.lista_funcionarios

    def get_projetos(self):
        return self.lista_projetos

    def adicionar_funcionario(self, f):
        if f not in self.lista_funcionarios:
            f.id = len(self.lista_funcionarios) + 1
            self.lista_funcionarios.append(f)
        else:
            raise Exception("Funcionário já está na empresa")

    def criar_projeto(self, p):
        novo_projeto = Projeto(p)
        self.lista_projetos.append(novo_projeto)

class Funcionario:
    def __init__(self, name):
        self.nome = name
        self.id = 0

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id

class Projeto:
    def __init__(self, t):
        self.titulo = t

    def get_titulo(self):
        return self.titulo
