
# -*- coding: utf-8 -*-
import time

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
        print("id: " + id[i] + " nome: " + nome[i] + " CPF: " + cpf[i]+ " saldo: " + str(saldo[i]))
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
    elif(saldo[pos]!=0):
        return "Conta ainda tem saldo"
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
        return "nome: " + nome[pos]

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
    return "O valor do saldo é: " + str(saldo[pos])

def getSaldo(_id):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"

    return "O valor do saldo é: " + str(saldo[pos])

def saque(_id, valor):
    pos = achaConta(_id)
    if(pos == -1):
        return "Conta não encontrada"
    else:
        if(saldo[pos] < valor):
            return "Valor para saque excede saldo na conta!"
        saldo[pos] -= valor
        return "Saque de " + str(valor) + " reais realizado com sucesso!"

def transferencia(_idOrigem, _idDestino, valor):
    origem = achaConta(_idOrigem)
    if(origem == -1):
        return "Conta de origem não encontrada"
    destino = achaConta(_idDestino)
    if(destino == -1):
        return "Conta de destino não encontrada"
    if(saldo[origem] < valor):
        return "Valor para transferência excede saldo na conta!"

    saldo[origem] -= valor
    saldo[destino] += valor
    return "Transferência de " + str(valor) + " a realizada da conta " + id[origem] + " para a conta " + id[destino]

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

def test_getNomeOk():
    criaConta('1')
    setNome('1', 'joão')
    assert getNome('1') == "nome: joão"
    deletaConta('1')

def test_getNomeErrado():
    criaConta('1')
    assert getNome('2') == "Conta não encontrada"
    deletaConta('1')

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
    assert setCPF('1', '09198745689') == "CPF da conta 1 alterado para 09198745689"
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

def test_deletaContaErrada():
    criaConta('1')
    adicionaSaldo('1',10)
    assert deletaConta('1') == "Conta ainda tem saldo"
    saque('1',10)
    deletaConta('1')

def test_setSaldoOK():
    criaConta('1')
    assert adicionaSaldo('1', 30) == "O valor do saldo é: 30"
    saque('1',30)
    deletaConta('1')

def test_setSaldoErrado():
    criaConta('1')
    assert adicionaSaldo('2', 30) == "Conta não encontrada"
    deletaConta('1')

def test_saqueOK():
    criaConta('1')
    adicionaSaldo('1', 50)
    assert saque('1', 50) == "Saque de 50 reais realizado com sucesso!"
    deletaConta('1')

def test_transferenciaOK():
    criaConta('1')
    criaConta('2')
    adicionaSaldo('1', 60)
    adicionaSaldo('2', 30)
    transferencia('1', '2', 30)
    assert getSaldo('2') == "O valor do saldo é: 60"
    saque('1',30)
    saque('2',60)
    deletaConta('1')
    deletaConta('2')

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
    test_setSaldoOK()
    test_setSaldoErrado()
    test_saqueOK()
    test_transferenciaOK()


id = []
saldo = []
nome = []
cpf = []


def main():
    testHub()
    menu = 1
    while(menu>0 and menu<13):
        print("Controle de contas bancárias:")
        print("")
        print("1 - Criar conta nova")
        print("2 - Definir Nome")
        print("3 - Definir CPF")
        print("4 - Depositar")
        print("5 - Sacar")
        print("6 - Transferir")
        print("7 - Ver todas as contas")
        print("8 - Ver nome de conta")
        print("9 - Ver CPF de conta")
        print("10- Ver Saldo")
        print("11- Deleta conta")
        print("12- Ver infos da conta")
        menu = int(input())
        if (menu==1):
            print("Digite um identificador para sua conta")
            _id = input()
            print(criaConta(_id))
        elif(menu==2):
            print("Digite um identificador para a conta que deseja trocar o nome")
            _id = input()
            print("Digite um nome para a conta")
            _nome = input()
            print(setNome(_id,_nome))
        elif(menu==3):
            print("Digite um identificador para a conta que deseja trocar o CPF")
            _id = input()
            print("Digite um CPF para a conta")
            _cpf = input()
            print(setCPF(_id,_cpf))
        elif(menu==4):
            print("Digite um identificador para a conta que deseja depositar")
            _id = input()
            print("Digite o valor")
            _saldo = int(input())
            print(adicionaSaldo(_id,_saldo))
        elif(menu==5):
            print("Digite um identificador para a conta que deseja sacar")
            _id = input()
            print("Digite o valor")
            _saldo = int(input())
            print(saque(_id,_saldo))
        elif(menu==6):
            print("Digite um identificador para a conta de origem")
            _id = input()
            print("Digite um identificador para a conta de destino")
            _id2 = input()
            print("Digite o valor")
            _saldo = int(input())
            print(transferencia(_id,_id2,_saldo))
        elif(menu==7):
            print(printaTodas())
        elif(menu==8):
            print("Digite um identificador para a conta que deseja ver nome")
            _id = input()
            print(getNome(_id))
        elif(menu==9):
            print("Digite um identificador para a conta que deseja ver CPF")
            _id = input()
            print(getCPF(_id))
        elif(menu==10):
            print("Digite um identificador para a conta que deseja ver saldo")
            _id = input()
            print(getSaldo(_id))
        elif(menu==11):
            print("Digite um identificador para a conta que deseja deletar")
            _id = input()
            print(deletaConta(_id))
        elif(menu==12):
            print("Digite um identificador para a conta que deseja ver")
            _id = input()
            print(printaConta(_id))
        time.sleep(1)




if __name__ == "__main__":
    main()
