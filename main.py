from banco import Banco

def main():
    banco = Banco()
    banco.criaConta(1, 1000, 'bruna', '125416')
    banco.achaConta(1)


if __name__ == "__main__":
    main()