limite = int(input('Digite quantos números serão inseridos: '))

lista = []

for i in range(limite):
    dado = int(input('Digite o número que deseja inserir: '))
    lista.append(dado)

print(lista.sort(reverse=True)) #resultado = None
