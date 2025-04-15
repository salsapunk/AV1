def eh_primo_ou_nao(x): #define a função com a variável x
    for i in range(2, x+1): #repete de 2 até o número definido
        if x % i == 0: #se o resto da divisão do número por i for 0, ou seja, a divisão for exata, executa:
            print(f'{x} é primo') #printa o resultado
            break #finaliza o loop
        else: #caso o resto da divisão do número por i não for 0, executa:
            print(f'{x} não é primo') #printa o resultado
            break #finaliza o loop

numero = int(input('Digite o número que você quer checar: ')) #pega o input do número
eh_primo_ou_nao(numero) #chama a função com o valor do nímero