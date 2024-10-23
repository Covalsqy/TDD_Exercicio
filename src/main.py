class Empresa:
    def __init__(self, name):
        self.nome = name
        self.lista_funcionarios = []

    def get_nome(self):
        return self.nome

    def get_funcionarios(self):
        return self.lista_funcionarios

    def adicionar_funcionario(self, f):
        self.lista_funcionarios.append(f)

class Funcionario:
    def __init__(self, name):
        self.nome = name

    def get_nome(self):
        return self.nome
