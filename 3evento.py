nome = input('Digite o seu nome: ') #pega o input do nome

def exibir_nome(): #define a função que exibe o nome
    if len(nome) >= 120: #se o nome tiver mais que 120 caracteres essa parte é executada
        print('Digite um nome com menos de 120 caracteres!') #printa a mensagem
        return #retorna/cancela a função
    print(f'Seja muito bem vindo, {nome}!') #printa o nome

exibir_nome() #chama a função