
# -*- coding: utf-8 -*-
def criaConta(_id):
    pos = achaConta(_id)
    if(pos == -1):
        id.append(_id)
        saldo.append(0)
        nome.append('')
        cpf.append('')
        return "Conta criada"
    else:
        return "Já existe uma conta com esse id"


def printaTodas():
    i = 0
    while (i < len(id)):
        print(id[i], saldo[i])
        i = i+1
    return


def achaConta(_id):
    pos = -1
    i = 0
    while (i < len(id)):
        if id[i] == _id:
            pos = i
            break
        i = i+1
    return pos


def deletaConta(_id):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        id.pop(pos)
        saldo.pop(pos)
        nome.pop(pos)
        cpf.pop(pos)
        return "conta " + _id + " deletada"


def printaConta(_id):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        return "id = " + id[pos] + " saldo = " + str(saldo[pos]) + " nome = " + nome[pos]


def getNome(_id):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        return nome[pos]


def setNome(_id, _nome):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        nome[pos] = _nome
        return "nome da conta " + id[pos] + " alterado para " + nome[pos]


def getCPF(_id):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        return cpf[pos]


def setCPF(_id, _cpf):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        cpf[pos] = _cpf
        return "CPF da conta " + id[pos] + " alterado para " + cpf[pos]


def adicionaSaldo(_id, valor):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"

    if(valor <= 0):
        return "Valor inválido!"

    saldo[pos] += valor
    return "Saldo adicionado com sucesso!"


def getSaldo(_id):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"

    return saldo[pos]


def saque(_id, valor):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        if(saldo[pos] < valor):
            return "Valor para saque excede saldo na conta!"
        saldo[pos] -= valor
        return "Saque de " + valor + "reais realizado com sucesso!"


def transferencia(_idOrigem, _idDestino, valor):
    origem = achaConta(_idOrigem)
    destino = achaConta(_idDestino)
    if(pos == -1):
        return "Conta não encontrada"

    if(saldo[origem] < valor):
        return "Valor para transferência excede saldo na conta!"

    saldo[origem] -= valor
    saldo[destino] += valor
    return "Transferência realizada com sucesso!"


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


id = []
saldo = []
nome = []
cpf = []


def main():
    testHub()


if __name__ == "__main__":
    main()
