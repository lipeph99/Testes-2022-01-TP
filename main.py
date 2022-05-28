def criaConta(_id):
  id.append(_id)
  saldo.append(0)
  nome.append('')
  cpf.append('')
  return

def printaTodas():
  i=0
  while (i<len(id)):
    print(id[i],saldo[i])
    i = i+1
  return

def achaConta(_id):
  pos = -1
  i=0
  while (i<len(id)):
    if id[i]==_id:
      pos = i
      break
    i = i+1
  return pos

def printaConta(_id):
  pos = achaConta(_id)
  if(pos==-1):
    return "Conta não encontrada"
  else:
    return "id = " + id[pos] + " saldo = " + str(saldo[pos]) + " nome = " + nome[pos]

def getNome(_id):
  pos = achaConta(_id)
  if(pos==-1):
    return "Conta não encontrada"
  else:
    return nome[pos]
  return

def setNome(_id,_nome):
  pos = achaConta(_id)
  if(pos==-1):
    return "Conta não encontrada"
  else:
    nome[pos] = _nome
    return "nome da conta " + id[pos] + " alterado para " + nome[pos]

  
def test_cria():
  criaConta('1')
  assert printaConta('1') == "id = 1 saldo = 0 nome = "

def test_setNome():
  criaConta('2')
  assert setNome('2','joão') == "nome da conta 2 alterado para joão"

def get_nome():
  return
id = []
saldo = []
nome = []
cpf = []

def main():
  criaConta('4')
  printaTodas()
  print(achaConta('4'))
  print(printaConta('4'))

if __name__ == "__main__":
    main()