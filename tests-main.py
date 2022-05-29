def test_criaRepetido():
    criaConta('1')
    assert criaConta('1') == "Já existe uma conta com esse id"
    deletaConta('1')


def test_criaOK():
    criaConta('1')
    assert printaConta('1') == "id = 1 saldo = 0 nome = "
    deletaConta('1')


def test_achaContaOK():
    criaConta('1')
    assert achaConta('1') == 0
    deletaConta('1')
    return


def test_achaContaErro():
    criaConta('1')
    assert achaConta('2') == -1
    deletaConta('1')
    return


def test_setNomeOk():
    criaConta('1')
    assert setNome('1', 'joão') == "nome da conta 1 alterado para joão"
    deletaConta('1')


def test_setNomeErrado():
    criaConta('1')
    assert setNome('2', 'joão') == "Conta não encontrada"
    deletaConta('1')


def test_setCPFOK():
    criaConta('1')
    assert setCPF(
        '1', '09198745689') == "CPF da conta 1 alterado para 09198745689"
    deletaConta('1')


def test_setCPRFErrado():
    criaConta('1')
    assert setCPF('2', '09198745689') == "Conta não encontrada"
    deletaConta('1')


def test_deletaContaOK():
    criaConta('1')
    assert deletaConta('1') == "conta 1 deletada"


def test_deletaContaErrada():
    criaConta('1')
    assert deletaConta('2') == "Conta não encontrada"
    deletaConta('1')


def test_setSaldoOK():
    criaConta('1')
    assert adicionaSaldo('1', 30) == "O valor do saldo é: 30"


def test_saqueOK():
    criaConta('1')
    adicionaSaldo('1', 50)
    assert saque('1', 50) == "Saque de 50 reais realizado com sucesso!"


def test_transferenciaOK():
    criaConta('1')
    criaConta('2')
    adicionaSaldo('1', 60)
    adicionaSaldo('2', 30)
    transferencia('1', '2', 30)
    assert getSaldo('2') == "60"


def testHub():
    test_criaRepetido()
    test_criaOK()
    test_achaContaOK()
    test_achaContaErro()
    test_setNomeOk()
    test_setNomeErrado()
    test_setCPFOK()
    test_setCPRFErrado()
    test_deletaContaOK()
    test_deletaContaErrada()