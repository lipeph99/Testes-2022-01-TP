from banco import Banco

"""
Testes Criação do Banco
"""
def test_criaRepetido():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.criaConta('1', 1000, 'Bruna', '123456') == "Já existe uma conta com esse id"
    banco.saque('1', 1000)
    banco.deletaConta('1')

def test_criaOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.printaConta('1') == "id: 1 | saldo: 1000 | nome: Bruna"
    banco.saque('1', 1000)
    banco.deletaConta('1')

"""
Testes Identificar Conta
"""
def test_achaContaOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.achaConta('1') == 0
    banco.saque('1', 1000)
    banco.deletaConta('1')
    return

def test_achaContaErro():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.achaConta('2') == -1
    banco.saque('1', 1000)
    banco.deletaConta('1')
    return

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
    assert banco.setCPF('1', '09198745689') == "CPF da conta 1 alterado para 09198745689"
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
Testes Saldo
"""
def test_setSaldoOK():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    assert banco.adicionaSaldo('1', 30) == "Saldo adicionado com sucesso!"
    banco.saque('1', 970)
    banco.deletaConta('1')

def test_setSaldoErrado():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.adicionaSaldo('2', 30) == "Conta não encontrada"
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
    banco.saque('1',30)
    banco.saque('2',60)
    banco.deletaConta('1')
    banco.deletaConta('2')

def test_transferenciaSemContaOrigem():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.adicionaSaldo('1', 60)
    assert  banco.transferencia('3', '1', 30) == "Conta de origem não encontrada"
    banco.saque('1',60)
    banco.deletaConta('1')

def test_transferenciaSemContaDestino():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.adicionaSaldo('1', 60)
    assert  banco.transferencia('1', '3', 30) == "Conta de destino não encontrada"
    banco.saque('1', 60)
    banco.deletaConta('1')

def test_transferenciaExcedeSaldo():
    banco = Banco()
    banco.criaConta('1', 0, 'Bruna', '123456')
    banco.criaConta('2', 0, 'João', '123456123')
    banco.adicionaSaldo('1', 60)
    assert  banco.transferencia('1', '2', 120) == "Valor para transferência excede saldo na conta!"
    banco.saque('1',60)
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
HUB
"""
def testHub():
    test_criaRepetido()
    test_criaOK()
    test_achaContaOK()
    test_achaContaErro()
    test_getNomeOk()
    test_getNomeErrado()
    test_setNomeOk()
    test_setNomeErrado()
    test_setCPFOK()
    test_setCPRFErrado()
    test_deletaContaOK()
    test_deletaContaErrada()
    test_deletaContaComSaldo()
    test_setSaldoOK()
    test_setSaldoErrado()
    test_saqueOK()
    test_transferenciaOK()
    test_transferenciaSemContaOrigem()
    test_transferenciaSemContaDestino()
    test_transferenciaExcedeSaldo()
    test_getIdadeOK()
    test_getIdadeContaNaoEncontrada()
    test_setIdadeOK()
    test_setIdadeContaNaoEncontrada()
    test_setIdadeMenorDeIdade()
    test_setIdadeNumeroInvalido()