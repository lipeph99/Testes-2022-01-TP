import time
from tests import testHub 
from banco import Banco

def main():
    testHub()
    menu = 1
    banco = Banco()
    while(menu>0 and menu<15):
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
        print("13- Definir idade")
        print("14- Ver idade")
        menu = int(input())
        if (menu==1):
            print("Digite um identificador para sua conta")
            _id = input()
            print("Digite um nome para a conta")
            _nome = input()
            print("Digite um CPF para a conta")
            _cpf = input()
            print("Digite o valor do saldo inicial")
            _saldo = int(input())
            print(banco.criaConta(_id, _saldo, _nome, _cpf))
        elif(menu==2):
            print("Digite um identificador para a conta que deseja trocar o nome")
            _id = input()
            print("Digite um nome para a conta")
            _nome = input()
            print(banco.setNome(_id,_nome))
        elif(menu==3):
            print("Digite um identificador para a conta que deseja trocar o CPF")
            _id = input()
            print("Digite um CPF para a conta")
            _cpf = input()
            print(banco.setCPF(_id,_cpf))
        elif(menu==4):
            print("Digite um identificador para a conta que deseja depositar")
            _id = input()
            print("Digite o valor")
            _saldo = int(input())
            print(banco.adicionaSaldo(_id,_saldo))
        elif(menu==5):
            print("Digite um identificador para a conta que deseja sacar")
            _id = input()
            print("Digite o valor")
            _saldo = int(input())
            print(banco.saque(_id,_saldo))
        elif(menu==6):
            print("Digite um identificador para a conta de origem")
            _id = input()
            print("Digite um identificador para a conta de destino")
            _id2 = input()
            print("Digite o valor")
            _saldo = int(input())
            print(banco.transferencia(_id,_id2,_saldo))
        elif(menu==7):
            print(banco.printaTodas())
        elif(menu==8):
            print("Digite um identificador para a conta que deseja ver nome")
            _id = input()
            print(banco.getNome(_id))
        elif(menu==9):
            print("Digite um identificador para a conta que deseja ver CPF")
            _id = input()
            print(banco.getCPF(_id))
        elif(menu==10):
            print("Digite um identificador para a conta que deseja ver saldo")
            _id = input()
            print(banco.getSaldo(_id))
        elif(menu==11):
            print("Digite um identificador para a conta que deseja deletar")
            _id = input()
            print(banco.deletaConta(_id))
        elif(menu==12):
            print("Digite um identificador para a conta que deseja ver")
            _id = input()
            print(banco.printaConta(_id))
        elif(menu==13):
            print("Digite um identificador para a conta que deseja trocar a idade")
            _id = input()
            print("Digite uma idade para a conta")
            _idade = input()
            print(banco.setIdade(_id,_idade))
        elif(menu==14):
            print("Digite um identificador para a conta que deseja ver a idade")
            _id = input()
            print(banco.setIdade(_id))
        time.sleep(1)




if __name__ == "__main__":
    main()
