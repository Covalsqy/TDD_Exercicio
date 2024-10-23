from src.main import Empresa, Funcionario
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa("W")

    def test_criar_empresa_w(self):
        self.assertIsNotNone(self.empresa)
        self.assertEqual(self.empresa.nome, "W")

    def test_criar_funcionario(self):
        funcionario = Funcionario("Arthur")
        self.assertIsNotNone(funcionario)
        self.assertEqual(funcionario.nome, "Arthur")

    def test_associar_funcionario_a_empresa(self):
        funcionario = Funcionario("João")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertEqual(self.empresa.get_funcionarios()[0].get_nome(), funcionario.get_nome())

    def test_associar_dois_funcionarios(self):
        funcionario1 = Funcionario("José")
        funcionario2 = Funcionario("Marcos")
        self.empresa.adicionar_funcionario(funcionario1)
        self.empresa.adicionar_funcionario(funcionario2)
        self.assertEqual(self.empresa.get_funcionarios()[0].get_nome(), funcionario1.get_nome())
        self.assertEqual(self.empresa.get_funcionarios()[1].get_nome(), funcionario2.get_nome())

    def test_associar_dois_funcionarios_mesmo_nome(self):
        funcionario1 = Funcionario("Marcos")
        funcionario2 = Funcionario("Marcos")
        self.empresa.adicionar_funcionario(funcionario1)
        self.empresa.adicionar_funcionario(funcionario2)
        self.assertEqual(self.empresa.get_funcionarios()[0].get_id(), funcionario1.get_id())
        self.assertEqual(self.empresa.get_funcionarios()[1].get_id(), funcionario2.get_id())
        self.assertEqual(self.empresa.get_funcionarios()[0].get_nome(), self.empresa.get_funcionarios()[1].get_nome())
        self.assertNotEqual(self.empresa.get_funcionarios()[0].get_id(), self.empresa.get_funcionarios()[1].get_id())

    def test_associar_funcionario_ja_associado_a_empresa(self):
        funcionario = Funcionario("Jorge")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertRaises(Exception, self.empresa.adicionar_funcionario, funcionario)

    def test_criar_projeto(self):
        self.empresa.criar_projeto("Desenvolver TDD")
        self.assertEqual(self.empresa.get_projetos()[0].get_titulo(), "Desenvolver TDD")

    def test_associar_funcionario_a_projeto(self):
        funcionario = Funcionario("Felipe")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.criar_projeto("Fabricar Peças")
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.assertIn(funcionario, self.empresa.dicionario_projetos[1])

if __name__ == '__main__':
    unittest.main()
