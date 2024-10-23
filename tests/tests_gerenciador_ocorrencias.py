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


if __name__ == '__main__':
    unittest.main()
