filename = input("Digite o nome do arquivo: ")

arq1 = open(filename+".txt","w")

arq1.write("Test")

arq1.close()