from banco import Banco

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

def test_saqueOK():
    banco = Banco()
    banco.criaConta('1', 1000, 'Bruna', '123456')
    assert banco.saque('1', 50) == "Saque de 50 reais realizado com sucesso!"
    banco.saque('1', 950)
    banco.deletaConta('1')

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