# -*- coding: utf-8 -*-
from banco import Banco

"""
Teste de sistema
"""

def test_system_umaContaOk():
    banco = Banco()
    assert banco.criaConta('1', 0, 'João', '123') == "Conta criada"
    assert banco.getIdade('1') == 0
    assert banco.printaConta('1') == "id: 1 | saldo: 0 | nome: João"
    assert banco.getNome('1') == "nome: João"
    assert banco.setNome('1', 'Joãozinho') == "nome da conta 1 alterado para Joãozinho"
    assert banco.getNome('1') == "nome: Joãozinho"
    assert banco.adicionaSaldo('1', 30) == "Saldo adicionado com sucesso!"
    assert banco.getSaldo('1') == "O valor do saldo é: 30"
    assert banco.adicionaSaldo('1', 20) == "Saldo adicionado com sucesso!"
    assert banco.getSaldo('1') == "O valor do saldo é: 50"
    assert banco.saque('1', 40) == "Saque de 40 reais realizado com sucesso!"
    assert banco.getSaldo('1') == "O valor do saldo é: 10"
    assert banco.getCPF('1') == "123"
    assert banco.setCPF('1', '234') == "CPF da conta 1 alterado para 234"
    assert banco.getCPF('1') == "234"
    assert banco.setIdade('1', 20) == "Idade da conta 1 definida como 20"
    assert banco.getIdade('1') == 20
    assert banco.printaConta('1') == "id: 1 | saldo: 10 | nome: Joãozinho"
    assert banco.printaTodasContas() == "id: 1 nome: Joãozinho CPF: 234 saldo: 10"
    assert banco.saque('1', 10) == "Saque de 10 reais realizado com sucesso!"
    assert banco.deletaConta('1') == "conta 1 deletada"

def test_system_umaContaMultiplosErros():
    banco = Banco()
    assert banco.printaTodasContas() == "Esse banco ainda não possui contas"
    assert banco.printaConta('1') == "Conta não encontrada"
    assert banco.criaConta('1', -1, 'João', '123') == "Saldo inicial inválido"
    assert banco.criaConta('1', 10, '', '123') == "Nome não pode estar vazio"
    assert banco.criaConta('1', 10, 'João', '') == "CPF inválido"
    assert banco.criaConta('1', 10, 'João', '123') == "Conta criada"
    assert banco.deletaConta('1') == "Conta ainda tem saldo"
    assert banco.deletaConta('2') == "Conta não encontrada"
    assert banco.getNome('2') == "Conta não encontrada"
    assert banco.setNome('2', 'Joãozinho') == "Conta não encontrada"
    assert banco.getCPF('2') == "Conta não encontrada"
    assert banco.setCPF('2', '234') == "Conta não encontrada"
    assert banco.adicionaSaldo('2', 20) == "Conta não encontrada"
    assert banco.adicionaSaldo('1', -20) == "Valor inválido!"
    assert banco.getSaldo('2') == "Conta não encontrada"
    assert banco.saque('2', 1) == "Conta não encontrada"
    assert banco.saque('1', -1) == "Valor inválido para saque!"
    assert banco.saque('1', 40) == "Valor para saque excede saldo na conta!"
    assert banco.getIdade('2') == "Conta não encontrada"
    assert banco.setIdade('2', 20) == "Conta não encontrada"
    assert banco.setIdade('1', -20) == "Número inválido"
    assert banco.setIdade('1', 2) == "Contas apenas para maiores"
    assert banco.deletaConta('2') == "Conta não encontrada"
    assert banco.deletaConta('1') == "Conta ainda tem saldo"
    assert banco.criaConta('1', 0, 'Maria', '234') == "Já existe uma conta com esse id"
    assert banco.criaConta('2', 0, 'Maria', '123') == "Já existe uma conta com esse cpf"
    assert banco.saque('1', 10) == "Saque de 10 reais realizado com sucesso!"
    assert banco.deletaConta('1') == "conta 1 deletada"

def testHub():
    test_system_umaContaOk()
    test_system_umaContaMultiplosErros()