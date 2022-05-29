# -*- coding: utf-8 -*-

class Banco:
    def __init__(self):
        self.contas = []

    def achaConta(self, _id):
        pos = -1
        i = 0
        while (i < len(self.contas)):
            if self.contas[i].id == _id:
                pos = i
                break
            i = i+1
        return pos
        
    def criaConta(self, _id, saldo, nome, cpf):
        pos = self.achaConta(_id)
        if(pos == -1):
            conta = Conta(_id, saldo, nome, cpf)
            self.contas.append(conta)
            return "Conta criada"
        else:
            return "Já existe uma conta com esse id"

    def printaTodasContas(self):
        i = 0
        while (i < len(self.contas)):
            print("id: " + self.contas[i].id + " nome: " + self.contas[i].nome + " CPF: " + self.contas[i].cpf + " saldo: " + str(self.contas[i].saldo) )
            i = i+1
        return

    def deletaConta(self, _id):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        elif(self.contas[pos].saldo != 0):
            return "Conta ainda tem saldo"
        else:
            self.contas.pop(pos)
            return "conta " + _id + " deletada"
            
    def printaConta(self, _id):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            return "id = " + self.contas[pos].id + " saldo = " + str(self.contas[pos].saldo ) + " nome = " + self.contas[pos].nome

    def getNome(self, _id):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            return "nome: " + self.contas[pos].nome
            
    def setNome(self, _id, _nome):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            self.contas[pos].nome = _nome
            return "nome da conta " + self.contas[pos].id + " alterado para " + self.contas[pos].nome


    def getCPF(self, _id):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            return self.contas[pos].cpf


    def setCPF(self, _id, _cpf):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            self.contas[pos].cpf = _cpf
            return "CPF da conta " + self.contas[pos].id + " alterado para " + self.contas[pos].cpf


    def adicionaSaldo(self, _id, valor):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"

        if(valor <= 0):
            return "Valor inválido!"

        self.contas[pos].saldo = valor + self.contas[pos].saldo 
        return "Saldo adicionado com sucesso!"


    def getSaldo(self, _id):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"

        return "O valor do saldo é: " + str(self.contas[pos].saldo)


    def saque(self, _id, valor):
        pos = self.achaConta(_id)
        if(pos == -1):
            return "Conta não encontrada"
        else:
            if(self.contas[pos].saldo < valor):
                return "Valor para saque excede saldo na conta!"
            self.contas[pos].saldo = self.contas[pos].saldo - valor
            return "Saque de " + str(valor) + "reais realizado com sucesso!"


    def transferencia(self, _idOrigem, _idDestino, valor):
        origem = self.achaConta(_idOrigem)
        if(origem == -1):
            return "Conta de origem não encontrada"
        destino = self.achaConta(_idDestino)
        if(destino == -1):
            return "Conta de destino não encontrada"
        if(self.contas[_idOrigem].saldo < valor):
            return "Valor para transferência excede saldo na conta!"

        self.contas[_idOrigem].saldo = self.contas[_idOrigem].saldo - valor
        self.contas[_idDestino].saldo = self.contas[_idDestino].saldo + valor
        return "Transferência de " + str(valor) + " a realizada da conta " + str(idOrigem) + " para a conta " + str(idDestino)

class Conta:
    def __init__(self, id, saldo, nome, cpf):
        self.id = id
        self.saldo = saldo
        self.nome = nome
        self.cpf = cpf