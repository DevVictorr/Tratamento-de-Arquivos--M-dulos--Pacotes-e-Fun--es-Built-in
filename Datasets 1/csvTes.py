arq1 = open("salarios.csv","r")

data = arq1.read()

rows = data.split('\n')


full_data = []

for row in rows :
    split_row = row.split(",")
    full_data.append(split_row)

cout = 0

for row in full_data:
    cout += 1

print(full_data)

print("Total de linhas: "+ cout)