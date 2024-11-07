class Funcionario:
    def __init__(self, name):
        self.nome = name
        self.id = 0
        self.count = 0

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id

    def get_count(self):
        return self.count

    def increase_count(self):
        self.count += 1

    def decrease_count(self):
        self.count -= 1
