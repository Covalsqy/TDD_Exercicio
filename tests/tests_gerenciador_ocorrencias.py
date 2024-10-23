from src.main import Empresa
import unittest

class MyTestCase(unittest.TestCase):
    def test_criar_empresa_w(self):
        empresa = Empresa("W")
        self.assertIsNotNone(empresa)  # add assertion here
        self.assertEqual(empresa.nome, "W")


if __name__ == '__main__':
    unittest.main()
