lista_numeros = [] #define a lista como vazia

def ordenar(): #define a função que ordena a lista
    for i in range(3):  #loop que se repete até a terceira vez
        numero = int(input('digite um dos números que deseja ordenar: ')) #pega o input do número
        lista_numeros.append(numero) #adiciona o número à lista
    lista_numeros.sort() #ordena a lista
    print(lista_numeros) #printa a lista

ordenar() #chama a função