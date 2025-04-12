texto = input('Digite o texto que deseja verificar: ') #pega o input do texto a ser verificado
valor = input('Digite a letra que deseja saber: ') #pega o input da letra

index = 0 #index que vai ser o número printado

for letra in texto: #loop que verifica cada letra no texto
    if letra == valor: #se a letra é igual a letra pega no input, executa
        print(index) #printa o número em que a letra aparece
        break #quebra o loop
    else: #se a letra não for igual a letra do input, executa:
        index = index + 1 #adiciona 1 no index
