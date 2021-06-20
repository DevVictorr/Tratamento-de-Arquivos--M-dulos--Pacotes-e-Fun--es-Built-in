import csv


with open ('numeros.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('primeira','segunda','terceira'))
    writer.writerow((1,2,3))
    writer.writerow((6,5,4))

with open ('numeros.csv', 'r') as arquivo:
    ler = csv.reader(arquivo)

    for x in ler:
        print('Números de colunas: ', len(x))
        print(x)

with open ('numeros.csv', 'r') as arquivo:
    ler = csv.reader(arquivo)
    dados = list(ler)

print(dados)

