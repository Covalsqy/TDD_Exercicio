from src.main import Empresa, Funcionario
import unittest

class MyTestCase(unittest.TestCase):
    def test_criar_empresa_w(self):
        empresa = Empresa("W")
        self.assertIsNotNone(empresa)
        self.assertEqual(empresa.nome, "W")

    def test_criar_funcionario(self):
        funcionario = Funcionario("Arthur")
        self.assertIsNotNone(funcionario)
        self.assertEqual(funcionario.nome, "Arthur")

    def test_associar_funcionario_a_empresa(self):
        empresa = Empresa("W")
        funcionario = Funcionario("João")
        empresa.adicionar_funcionario(funcionario)
        self.assertEqual(empresa.get_funcionarios()[0].get_nome(), funcionario.get_nome())

    def test_associar_dois_funcionarios(self):
        empresa = Empresa("W")
        funcionario1 = Funcionario("José")
        funcionario2 = Funcionario("Marcos")
        empresa.adicionar_funcionario(funcionario1)
        empresa.adicionar_funcionario(funcionario2)
        self.assertEqual(empresa.get_funcionarios()[0].get_nome(), funcionario1.get_nome())
        self.assertEqual(empresa.get_funcionarios()[1].get_nome(), funcionario2.get_nome())

    def test_associar_dois_funcionarios_mesmo_nome(self):
        empresa = Empresa("W")
        funcionario1 = Funcionario("Marcos")
        funcionario2 = Funcionario("Marcos")
        empresa.adicionar_funcionario(funcionario1)
        empresa.adicionar_funcionario(funcionario2)
        self.assertEqual(empresa.get_funcionarios()[0].get_id(), funcionario1.get_id())
        self.assertEqual(empresa.get_funcionarios()[1].get_id(), funcionario2.get_id())
        self.assertEqual(empresa.get_funcionarios()[0].get_nome(), empresa.get_funcionarios()[1].get_nome())
        self.assertNotEqual(empresa.get_funcionarios()[0].get_id(), empresa.get_funcionarios()[1].get_id())

    def test_associar_funcionario_ja_associado_a_empresa(self):
        empresa = Empresa("W")
        funcionario = Funcionario("Jorge")
        empresa.adicionar_funcionario(funcionario)
        self.assertRaises(Exception, empresa.adicionar_funcionario, funcionario)

if __name__ == '__main__':
    unittest.main()
