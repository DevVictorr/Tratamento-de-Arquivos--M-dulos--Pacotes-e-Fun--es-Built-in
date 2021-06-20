import json


dict = {
    "Nome":"Victor",
    "linguagem":"Python",
    "similiar":["sim","nao","talvez"],
    "idade":25
}

for k,v in dict.items():
    print(k,v)


json.dumps(dict)

with open ('dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))

with open ('dados.json','r') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
print(data)

print(data['Nome'])