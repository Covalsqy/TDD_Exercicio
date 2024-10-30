from src.main import Empresa, Funcionario, Ocorrencia
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

    def test_criar_dois_projetos(self):
        self.empresa.criar_projeto("Treinamento")
        self.empresa.criar_projeto("Refatoramento Código")
        self.assertEqual(self.empresa.get_projetos()[0].get_titulo(), "Treinamento")
        self.assertEqual(self.empresa.get_projetos()[1].get_titulo(), "Refatoramento Código")

    def test_associar_funcionario_a_projeto(self):
        funcionario = Funcionario("Felipe")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.criar_projeto("Fabricar Peças")
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.assertIn(funcionario, self.empresa.dicionario_projetos[1])

    def test_associar_dois_funcionarios_a_dois_projetos(self):
        funcionario1 = Funcionario("Felipe")
        funcionario2 = Funcionario("Francisco")
        self.empresa.adicionar_funcionario(funcionario1)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.criar_projeto("Fabricar Peças")
        self.empresa.criar_projeto("Encomenda")
        self.empresa.atribuir_funcionario_a_projeto(1, 2)
        self.empresa.atribuir_funcionario_a_projeto(2, 1)
        self.assertIn(funcionario1, self.empresa.dicionario_projetos[2])
        self.assertIn(funcionario2, self.empresa.dicionario_projetos[1])
        self.assertNotIn(funcionario2, self.empresa.dicionario_projetos[2])
        self.assertNotIn(funcionario1, self.empresa.dicionario_projetos[1])

    def test_associar_um_funcionario_a_dois_projetos(self):
        funcionario = Funcionario("Pedro")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.criar_projeto("Refatorar Código")
        self.empresa.criar_projeto("Especificar Requisitos")
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.atribuir_funcionario_a_projeto(1, 2)
        self.assertIn(funcionario, self.empresa.dicionario_projetos[1])
        self.assertIn(funcionario, self.empresa.dicionario_projetos[2])

    def test_associar_funcionario_a_projeto_inexistente(self):
        funcionario = Funcionario("Carlos")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertRaises(KeyError, self.empresa.atribuir_funcionario_a_projeto, 1, 1)

    def test_associar_funcionario_inexistente_a_projeto(self):
        self.empresa.criar_projeto("Refatorar Código")
        self.assertRaises(IndexError, self.empresa.atribuir_funcionario_a_projeto, 1, 1)

    def test_criar_ocorrencia(self):
        funcionario = Funcionario("Rogério")
        nova_ocorrencia = Ocorrencia(funcionario, "TAREFA", "BAIXA", "Fazer Documentação", "1_1")
        self.assertEqual("TAREFA", nova_ocorrencia.get_tipo())
        self.assertEqual("BAIXA", nova_ocorrencia.get_prioridade())
        self.assertEqual("Fazer Documentação", nova_ocorrencia.get_resumo())
        self.assertEqual(funcionario, nova_ocorrencia.get_responsavel())
        self.assertEqual(nova_ocorrencia.get_chave(), "1_1")

    def test_criar_ocorrencia_em_empresa(self):
        funcionario = Funcionario("Rogério")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Erro na página inicial")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_responsavel(), funcionario)
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_prioridade(), "ALTA")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_resumo(), "Erro na página inicial")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_tipo(), "BUG")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_chave(), "1_1")

    def test_criar_ocorrencia_com_projeto_inexistente(self):
        funcionario = Funcionario("Felipe")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertRaises(Exception, self.empresa.criar_ocorrencia, 2, 1, "MELHORIA", "MÉDIA", "Refatorar Código")

    def test_criar_ocorrencia_com_id_de_projeto_menor_que_um(self):
        funcionario = Funcionario("Arthur")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertRaises(Exception, self.empresa.criar_ocorrencia, 0, 1, "MELHORIA", "MÉDIA", "Refatorar Código")

    def test_criar_ocorrencia_responsavel_inexistente(self):
        self.empresa.criar_projeto("Apollo 20")
        self.assertRaises(Exception, self.empresa.criar_ocorrencia, 1, 2, "TAREFA", "BAIXA", "Limpar Tanque")

    def test_criar_ocorrencia_com_id_de_funcionario_menor_que_um(self):
        self.empresa.criar_projeto("Desenvolver Debugger")
        self.assertRaises(Exception, self.empresa.criar_ocorrencia, -1, 2, "TAREFA", "ALTA", "Iniciar desenvolvimento")

    def test_fechar_ocorrencia(self):
        funcionario = Funcionario("Greg")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "MÉDIA", "Identificar causa de querrie não funcionar")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertEqual(self.empresa.get_estado_ocorrencia("1_1"), "FECHADO")

    def test_fechar_ocorrencia_fechada(self):
        funcionario = Funcionario("Greg")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "MÉDIA", "Identificar causa de querrie não funcionar")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertRaises(Exception, self.empresa.fechar_ocorrencia)

    def test_alterar_responsavel_ocorrencia_aberta(self):
        funcionario = Funcionario("Greg")
        funcionario2 = Funcionario("Renato")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "BAIXA", "Concertar impressora")
        self.empresa.trocar_responsavel_ocorrencia("1_1", 2)
        self.assertEqual(self.empresa.get_responsavel("1_1"), funcionario2)

    def test_alterar_responsavel_ocorrencia_fechada(self):
        funcionario = Funcionario("Greg")
        funcionario2 = Funcionario("Renato")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "BAIXA", "Concertar impressora")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertRaises(Exception, self.empresa.trocar_responsavel_ocorrencia, "1_1", 2)

if __name__ == '__main__':
    unittest.main()
