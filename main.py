def main():

  def criaConta(newId):
    id.append(newId)
    saldo.append(0)
    return
  
  def printaTodas():
    i=0
    while (i<len(id)):
      print(id[i],saldo[i])
      i = i+1
    return
  #Ler input e printar matriz
  id = []
  saldo = []
  criaConta('1')
  criaConta('2')
  printaTodas()

if __name__ == "__main__":
    main()