arq1 = open("texto.txt","r")

print(arq1.read())

arq1.close()

arq1 = open("texto.txt","w")

arq1.write('Ola')

arq1.close()


arq1 = open("texto.txt","a")

arq1.write(', Agora o Ola ficou junto com esse texto.')

arq1.close()

arq1 = open("texto.txt","r")

print(arq1.read())

arq1.close()
