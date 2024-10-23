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
        self.assertEqual(empresa.get_funcionarios()[0].nome, funcionario.get_nome())

if __name__ == '__main__':
    unittest.main()
