# -*- coding: utf-8 -*-

class Banco:
    def __init__(self):
        self.contas = []

    def encontrarContaPorId(self, _id):
        pos = -1
        i = 0
        while (i < len(self.contas)):
            if self.contas[i].id == _id:
                pos = i
                break
            i = i+1
        return pos

    def encontrarContaPorCPF(self, cpf):
        pos = -1
        i = 0
        while (i < len(self.contas)):
            if self.contas[i].cpf == cpf:
                pos = i
                break
            i = i+1
        return pos

    def criaConta(self, _id, saldo, nome, cpf):
        pos = self.encontrarContaPorId(_id)
        pos_cpf = self.encontrarContaPorCPF(cpf)
        if(pos == -1 and pos_cpf == -1):
            if saldo < 0:
                return "Saldo inicial inválido"
            if nome == "":
                return "Nome não pode estar vazio"
            if cpf == "" or len(cpf) > 10:
                return "CPF inválido"
            conta = Conta(_id, saldo, nome, cpf)
            self.contas.append(conta)
            return "Conta criada"
        else:
            if pos == 0:
                return "Já existe uma conta com esse id"
            if pos_cpf == 0:
                return "Já existe uma conta com esse cpf"

    def printaTodasContas(self):
        i = 0
        contas = ""
        if(len(self.contas) == 0):
            return "Esse banco ainda não possui contas"
        while (i < len(self.contas)):
            contas += "id: " + self.contas[i].id + " nome: " + self.contas[i].nome + \
                " CPF: " + self.contas[i].cpf + \
                " saldo: " + str(self.contas[i].saldo)
            i = i+1
        return contas

    def deletaConta(self, _id):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        elif(self.contas[pos].saldo != 0):
            return "Conta ainda tem saldo"
        else:
            self.contas.pop(pos)
            return "conta " + _id + " deletada"

    def printaConta(self, _id):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            return "id: " + self.contas[pos].id + " | saldo: " + str(self.contas[pos].saldo) + " | nome: " + self.contas[pos].nome

    def getNome(self, _id):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            return "nome: " + self.contas[pos].nome

    def setNome(self, _id, _nome):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            self.contas[pos].nome = _nome
            return "nome da conta " + self.contas[pos].id + " alterado para " + self.contas[pos].nome

    def getCPF(self, _id):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            return self.contas[pos].cpf

    def setCPF(self, _id, _cpf):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            self.contas[pos].cpf = _cpf
            return "CPF da conta " + self.contas[pos].id + " alterado para " + self.contas[pos].cpf

    def adicionaSaldo(self, _id, valor):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"

        if(valor <= 0):
            return "Valor inválido!"

        self.contas[pos].saldo = valor + self.contas[pos].saldo
        return "Saldo adicionado com sucesso!"

    def getSaldo(self, _id):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"

        return "O valor do saldo é: " + str(self.contas[pos].saldo)

    def saque(self, _id, valor):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        if(valor <= 0):
            return "Valor inválido para saque!"
        else:
            if(self.contas[pos].saldo < valor):
                return "Valor para saque excede saldo na conta!"
            self.contas[pos].saldo = self.contas[pos].saldo - valor
            return "Saque de " + str(valor) + " reais realizado com sucesso!"

    def transferencia(self, _idOrigem, _idDestino, valor):
        if(valor <= 0):
            return "Valor inválido para transferência!"
        origem = self.encontrarContaPorId(_idOrigem)
        if(origem == -1):
            return "Conta de origem não encontrada"
        destino = self.encontrarContaPorId(_idDestino)
        if(destino == -1):
            return "Conta de destino não encontrada"
        if(self.contas[int(_idOrigem)].saldo < valor):
            return "Valor para transferência excede saldo na conta!"

        self.contas[int(_idOrigem) -
                    1].saldo = self.contas[int(_idOrigem) - 1].saldo - valor
        self.contas[int(_idDestino) -
                    1].saldo = self.contas[int(_idDestino)-1].saldo + valor
        return "Transferência de " + str(valor) + " a realizada da conta " + str(_idOrigem) + " para a conta " + str(_idDestino)

    def getIdade(self, _id):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        return self.contas[pos].idade

    def setIdade(self, _id, _idade):
        pos = self.encontrarContaPorId(_id)
        if(pos == -1):
            return "Conta não encontrada"
        if(_idade < 0):
            return "Número inválido"
        if(_idade < 18):
            return "Contas apenas para maiores"
        self.contas[pos].idade = _idade
        return "Idade da conta " + self.contas[pos].id + " definida como " + str(self.contas[pos].idade)


class Conta:
    def __init__(self, id, saldo, nome, cpf):
        self.id = id
        self.saldo = saldo
        self.nome = nome
        self.cpf = cpf
