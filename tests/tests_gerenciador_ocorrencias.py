import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from empresa import Empresa
from funcionario import Funcionario
from ocorrencia import Ocorrencia

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
        self.assertRaises(PermissionError, self.empresa.adicionar_funcionario, funcionario)

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
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Erro na página inicial")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_responsavel(), funcionario)
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_prioridade(), "ALTA")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_resumo(), "Erro na página inicial")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_tipo(), "BUG")
        self.assertEqual(self.empresa.get_ocorrencia("1_1").get_chave(), "1_1")

    def test_criar_ocorrencia_com_projeto_inexistente(self):
        funcionario = Funcionario("Felipe")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 2, 1, "MELHORIA", "MÉDIA", "Refatorar Código")

    def test_criar_ocorrencia_com_id_de_projeto_menor_que_um(self):
        funcionario = Funcionario("Arthur")
        self.empresa.adicionar_funcionario(funcionario)
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 0, 1, "MELHORIA", "MÉDIA", "Refatorar Código")

    def test_criar_ocorrencia_responsavel_inexistente(self):
        self.empresa.criar_projeto("Apollo 20")
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 1, 2, "TAREFA", "BAIXA", "Limpar Tanque")

    def test_criar_ocorrencia_com_id_de_funcionario_menor_que_um(self):
        funcionario = Funcionario("Greg")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 1, 0, "TAREFA", "ALTA", "Iniciar desenvolvimento")

    def test_fechar_ocorrencia(self):
        funcionario = Funcionario("Greg")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "MÉDIA", "Identificar causa de querrie não funcionar")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertEqual(self.empresa.get_estado_ocorrencia("1_1"), "FECHADO")

    def test_fechar_ocorrencia_fechada(self):
        funcionario = Funcionario("Greg")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "MÉDIA", "Identificar causa de querrie não funcionar")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertRaises(PermissionError, self.empresa.fechar_ocorrencia, "1_1")

    def test_funcionario_uma_ocorrencia_a_menos_apos_ocorrencia_fechada(self):
        funcionario = Funcionario("Greg")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "MÉDIA", "Identificar causa de querrie não funcionar")
        qntd_ocorr_funcionario_antes = self.empresa.get_funcionario(1).get_count()
        self.empresa.fechar_ocorrencia("1_1")
        qntd_ocorr_funcionario_depois = self.empresa.get_funcionario(1).get_count()
        self.assertEqual(qntd_ocorr_funcionario_depois, qntd_ocorr_funcionario_antes - 1)

    def test_alterar_responsavel_ocorrencia_aberta(self):
        funcionario = Funcionario("Greg")
        funcionario2 = Funcionario("Renato")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.atribuir_funcionario_a_projeto(2, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "BAIXA", "Concertar impressora")
        self.empresa.trocar_responsavel_ocorrencia("1_1", 2)
        self.assertEqual(self.empresa.get_responsavel("1_1"), funcionario2)

    def test_alterar_responsavel_ocorrencia_fechada(self):
        funcionario = Funcionario("Greg")
        funcionario2 = Funcionario("Renato")
        self.empresa.criar_projeto("TDD")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.atribuir_funcionario_a_projeto(2, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "BAIXA", "Concertar impressora")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertRaises(PermissionError, self.empresa.trocar_responsavel_ocorrencia, "1_1", 2)

    def test_criar_ocorrencia_com_funcionario_e_projeto_nao_conectados(self):
        funcionario = Funcionario("Amanda")
        self.empresa.criar_projeto("Alpha")
        self.empresa.criar_projeto("Omega")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.assertRaises(PermissionError, self.empresa.criar_ocorrencia, 2, 1, "MELHORIA", "ALTA", "Experiência do Usuário")

    def test_alterar_responsavel_por_ocorrencia_em_projeto_diferente(self):
        funcionario = Funcionario("Amanda")
        funcionario2 = Funcionario("Laura")
        self.empresa.criar_projeto("Alpha")
        self.empresa.criar_projeto("Omega")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.atribuir_funcionario_a_projeto(1, 2)
        self.empresa.atribuir_funcionario_a_projeto(2, 1)
        self.empresa.criar_ocorrencia(2, 1, "TAREFA", "BAIXA", "Calcular salários")
        self.assertRaises(PermissionError, self.empresa.trocar_responsavel_ocorrencia,"2_1", 2)

    def test_criar_duas_ocorrencias_mesmo_funcionario(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "TAREFA", "BAIXA", "Calcular salários")
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        self.assertEqual(self.empresa.get_responsavel("1_1"), funcionario)
        self.assertEqual(self.empresa.get_responsavel("1_2"), funcionario)

    def test_criar_mais_de_uma_ocorrencia_em_projeto(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        occor1 = self.empresa.criar_ocorrencia(1, 1, "TAREFA", "BAIXA", "Calcular salários")
        occor2 = self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        self.assertEqual(self.empresa.get_ocorrencia("1_1"), occor1)
        self.assertEqual(self.empresa.get_ocorrencia("1_2"), occor2)

    def test_criar_duas_ocorrencias_iguais_no_mesmo_projeto(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 1, 1, "BUG", "ALTA", "Transações incorretas")

    def test_criar_ocorrencias_iguais_em_projetos_diferentes(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.criar_projeto("Omega")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.atribuir_funcionario_a_projeto(1, 2)
        occor1 = self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        occor2 = self.empresa.criar_ocorrencia(2, 1, "BUG", "ALTA", "Transações incorretas")
        self.assertEqual(self.empresa.get_ocorrencia("1_1"), occor1)
        self.assertEqual(self.empresa.get_ocorrencia("2_2"), occor2)

    def test_criar_diferente_tipo_ocorrencia(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.criar_projeto("Omega")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 1, 1, "CORREÇÃO", "ALTA", "Transações Proibidas")

    def test_criar_diferente_prioridade_ocorrencia(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.criar_projeto("Omega")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.assertRaises(ValueError, self.empresa.criar_ocorrencia, 1, 1, "BUG", "ALTÍSSIMA", "Transações Proibidas")


    def test_criar_mais_de_dez_ocorrencias_mesmo_funcionario(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "TAREFA", "BAIXA", "Calcular salários")
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        # setup
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "AAA")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "BBB")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "CCC")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "DDD")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "EEE")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "FFF")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "GGG")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "HHH")
        self.assertRaises(PermissionError, self.empresa.criar_ocorrencia, 1, 1, "MELHORIA", "MÉDIA", "III")

    def test_criar_mais_de_dez_ocorrencias_fechando_duas_mesmo_funcionario(self):
        funcionario = Funcionario("Clara")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "TAREFA", "BAIXA", "Calcular salários")
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "AAA")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "BBB")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "CCC")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "DDD")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "EEE")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "FFF")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "GGG")
        self.empresa.fechar_ocorrencia("1_4")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "HHH")
        self.empresa.fechar_ocorrencia("1_1")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "III")
        self.assertEqual(self.empresa.get_funcionario(1).get_count(), 9)

    def test_trocar_funcionario_no_limite_de_ocorrencias_para_uma_nova(self):
        funcionario = Funcionario("Clara")
        funcionario2 = Funcionario("Jorge")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.atribuir_funcionario_a_projeto(2, 1)
        self.empresa.criar_ocorrencia(1, 2, "TAREFA", "BAIXA", "Calcular salários")
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "AAA")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "BBB")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "CCC")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "DDD")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "EEE")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "FFF")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "GGG")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "HHH")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "III")
        self.assertRaises(PermissionError, self.empresa.trocar_responsavel_ocorrencia,"1_1", 1)

    def test_testar_contagem_de_ocorrencias_durante_troca_de_responsaveis(self):
        funcionario = Funcionario("Clara")
        funcionario2 = Funcionario("Jorge")
        self.empresa.criar_projeto("Delta")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.adicionar_funcionario(funcionario2)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.atribuir_funcionario_a_projeto(2, 1)
        self.empresa.criar_ocorrencia(1, 2, "TAREFA", "BAIXA", "Calcular salários")
        self.empresa.criar_ocorrencia(1, 1, "BUG", "ALTA", "Transações incorretas")
        self.empresa.criar_ocorrencia(1, 1, "MELHORIA", "MÉDIA", "AAA")
        self.empresa.trocar_responsavel_ocorrencia("1_1", 1)
        self.assertEqual(self.empresa.get_funcionario(1).get_count(), 3)
        self.assertEqual(self.empresa.get_funcionario(2).get_count(), 0)

    def test_alterar_prioridade_ocorrencia_aberta(self):
        funcionario = Funcionario("Peter")
        self.empresa.criar_projeto("Psi")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "TAREFA", "BAIXA", "Prioridade Incorreta")
        self.empresa.alterar_prioridade("1_1", "ALTA")
        self.assertEqual(self.empresa.get_prioridade_ocorrencia("1_1"), "ALTA")

    def test_alterar_prioridade_ocorrencia_fechada(self):
        funcionario = Funcionario("Peter")
        self.empresa.criar_projeto("Psi")
        self.empresa.adicionar_funcionario(funcionario)
        self.empresa.atribuir_funcionario_a_projeto(1, 1)
        self.empresa.criar_ocorrencia(1, 1, "TAREFA", "BAIXA", "Prioridade Incorreta")
        self.empresa.fechar_ocorrencia("1_1")
        self.assertRaises(PermissionError, self.empresa.alterar_prioridade,"1_1", "ALTA")

if __name__ == '__main__':
    unittest.main()
