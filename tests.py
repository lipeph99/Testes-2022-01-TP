# -*- coding: utf-8 -*-
from banco import Banco

"""
Testes Criação do Banco
"""


def test_criarContaIdJaExistente():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.criaConta(
        '1', 1000, 'Bruna', '123456') == "Já existe uma conta com esse id"


def test_criarContaCPFJaExistente():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.criaConta(
        '2', 1000, 'Bruna', '123456') == "Já existe uma conta com esse cpf"


def test_criaOK():
    banco = Banco()
    assert banco.criaConta('1', 1000, 'Bruna', '123456') == "Conta criada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_criarContaSaldoInicialInvalido():
    banco = Banco()
    assert banco.criaConta(
        '1', -100, 'Bruna', '123456') == "Saldo inicial inválido"


def test_criarContaNomeVazio():
    banco = Banco()
    assert banco.criaConta(
        '1', 1000, '', '123456') == "Nome não pode estar vazio"


def test_criarContaCPFVazio():
    banco = Banco()
    assert banco.criaConta('1', 100, 'Bruna', '') == "CPF inválido"


def test_criarContaCPFInvalido():
    banco = Banco()
    assert banco.criaConta(
        '1', 100, 'Bruna', '1234567891011') == "CPF inválido"


"""
Testes Identificar Conta
"""


def test_encontrarContaPorIdOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.encontrarContaPorId('1') == 0
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_encontrarContaPorIdErro():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.encontrarContaPorId('2') == -1
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_encontrarContaPorCPFErro():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.encontrarContaPorCPF('123') == -1
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_encontrarContaPorCPFOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.encontrarContaPorCPF('123456') == 0
    banco.saque('1', 1000)
    banco.deletaConta('1')


"""
Testes Nome 
"""


def test_getNomeOk():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.getNome('1') == "nome: Bruna"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_getNomeErrado():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.getNome('2') == "Conta não encontrada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_setNomeOk():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setNome('1', 'joão') == "nome da conta 1 alterado para joão"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_setNomeErrado():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setNome('2', 'joão') == "Conta não encontrada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


"""
Testes CPF
"""


def test_setCPFOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setCPF(
        '1', '09198745689') == "CPF da conta 1 alterado para 09198745689"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_setCPRFErrado():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setCPF('2', '09198745689') == "Conta não encontrada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


"""
Testes Deletar Conta
"""


def test_deletaContaOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    banco.saque('1', 1000)
    assert banco.deletaConta('1') == "conta 1 deletada"


def test_deletaContaErrada():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.deletaConta('2') == "Conta não encontrada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_deletaContaComSaldo():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.deletaConta('1') == "Conta ainda tem saldo"
    banco.saque('1', 1000)
    banco.deletaConta('1')


"""
Testes Depositar
"""


def test_adicionaSaldoOK():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    assert banco.adicionaSaldo('1', 30) == "Saldo adicionado com sucesso!"
    banco.saque('1', 970)
    banco.deletaConta('1')


def test_adicionaSaldoContaNaoEncontrada():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.adicionaSaldo('2', 30) == "Conta não encontrada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_adicionaSaldoValorInvalido():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.adicionaSaldo('1', -30) == "Valor inválido!"
    banco.saque('1', 1000)
    banco.deletaConta('1')


"""
Testes Saque
"""


def test_saqueOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.saque('1', 50) == "Saque de 50 reais realizado com sucesso!"
    banco.saque('1', 950)
    banco.deletaConta('1')


def test_saqueContaNaoEncontrada():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.saque('2', 50) == "Conta não encontrada"
    banco.saque('1', 1000)
    banco.deletaConta('1')


def test_saqueValorExcedeSaldo():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.saque('1', 2000) == "Valor para saque excede saldo na conta!"
    banco.saque('1', 1000)
    banco.deletaConta('1')


"""
Testes Transferência
"""


def test_transferenciaOK():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.criaConta('2', 0, 'João', '123456123')
    banco.adicionaSaldo('1', 60)
    banco.adicionaSaldo('2', 30)
    banco.transferencia('1', '2', 30)
    assert banco.getSaldo('2') == "O valor do saldo é: 60"
    banco.saque('1', 30)
    banco.saque('2', 60)
    banco.deletaConta('1')
    banco.deletaConta('2')


def test_transferenciaSemContaOrigem():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.adicionaSaldo('1', 60)
    assert banco.transferencia(
        '3', '1', 30) == "Conta de origem não encontrada"
    banco.saque('1', 60)
    banco.deletaConta('1')


def test_transferenciaSemContaDestino():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.adicionaSaldo('1', 60)
    assert banco.transferencia(
        '1', '3', 30) == "Conta de destino não encontrada"
    banco.saque('1', 60)
    banco.deletaConta('1')


def test_transferenciaExcedeSaldo():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.criaConta('2', 0, 'João', '123456123')
    banco.adicionaSaldo('1', 60)
    assert banco.transferencia(
        '1', '2', 120) == "Valor para transferência excede saldo na conta!"
    banco.saque('1', 60)
    banco.deletaConta('1')
    banco.deletaConta('2')


def test_transferenciaValorNegativo():
    banco = Banco()
    banco.criaConta('1', 110, 'Bruna', '123456')
    banco.criaConta('2', 220, 'João', '123456123')
    banco.adicionaSaldo('1', 60)
    assert banco.transferencia(
        '1', '2', -30) == "Valor inválido para transferência!"
    banco.deletaConta('1')
    banco.deletaConta('2')


def test_transferenciaValorZerado():
    banco = Banco()
    banco.criaConta('1', 110, 'Bruna', '123456')
    banco.criaConta('2', 220, 'João', '123456123')
    banco.adicionaSaldo('1', 60)
    assert banco.transferencia(
        '1', '2', 0) == "Valor inválido para transferência!"
    banco.deletaConta('1')
    banco.deletaConta('2')


"""
Testes Idade
"""


def test_getIdadeOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    banco.setIdade('1', 20)
    assert banco.getIdade('1') == 20
    banco.deletaConta('1')


def test_getIdadeContaNaoEncontrada():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.getIdade('2') == "Conta não encontrada"
    banco.deletaConta('1')


def test_setIdadeOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setIdade('1', 20) == "Idade da conta 1 definida como 20"
    banco.deletaConta('1')


def test_setIdadeContaNaoEncontrada():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setIdade('2', 20) == "Conta não encontrada"
    banco.deletaConta('1')


def test_setIdadeNumeroInvalido():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setIdade('1', -20) == "Número inválido"
    banco.deletaConta('1')


def test_setIdadeMenorDeIdade():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.setIdade('1', 17) == "Contas apenas para maiores"
    banco.deletaConta('1')


"""
Testes Printar Conta
"""


def test_printaContaOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.printaConta('1') == "id: 1 | saldo: 1000 | nome: Bruna"
    banco.deletaConta('1')


def test_printaContaNaoEncontrada():
    banco = Banco()
    assert banco.printaConta('2') == "Conta não encontrada"


"""
Testes Printar Todas as contas
"""


def test_printaContasBancoSemContas():
    banco = Banco()
    assert banco.printaTodasContas() == "Esse banco ainda não possui contas"


def test_printaContasOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.printaTodasContas() == "id: 1 nome: Bruna CPF: 123456 saldo: 1000"
    banco.deletaConta('1')


"""
HUB
"""


def testHub():
    test_criarContaIdJaExistente()
    test_criaOK()
    test_criarContaCPFInvalido()
    test_criarContaCPFVazio()
    test_criarContaNomeVazio()
    test_criarContaSaldoInicialInvalido()
    test_encontrarContaPorIdOK()
    test_encontrarContaPorIdErro()
    test_getNomeOk()
    test_getNomeErrado()
    test_setNomeOk()
    test_setNomeErrado()
    test_setCPFOK()
    test_setCPRFErrado()
    test_deletaContaOK()
    test_deletaContaErrada()
    test_deletaContaComSaldo()
    test_adicionaSaldoOK()
    test_adicionaSaldoContaNaoEncontrada()
    test_adicionaSaldoValorInvalido()
    test_saqueOK()
    test_transferenciaOK()
    test_transferenciaSemContaOrigem()
    test_transferenciaSemContaDestino()
    test_transferenciaExcedeSaldo()
    test_transferenciaValorNegativo()
    test_transferenciaValorZerado()
    test_getIdadeOK()
    test_getIdadeContaNaoEncontrada()
    test_setIdadeOK()
    test_setIdadeContaNaoEncontrada()
    test_setIdadeMenorDeIdade()
    test_setIdadeNumeroInvalido()
    test_printaContaNaoEncontrada()
    test_printaContaOK()
    test_printaContasBancoSemContas()
    test_printaContasOK()
    test_saqueContaNaoEncontrada()
    test_saqueValorExcedeSaldo()
    test_encontrarContaPorCPFErro()
    test_encontrarContaPorCPFOK()
