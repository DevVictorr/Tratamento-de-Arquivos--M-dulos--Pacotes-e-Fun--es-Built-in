import os

texto = "Testando usar python com TXT"

arquivo = open(os.path.join("testando.txt") , "w")

for palavra in texto.split():
    arquivo.write(palavra+' ')

arquivo.close()

arquivo = open(("testando.txt") , "r")

conteudo = arquivo.read()

print(conteudo)
