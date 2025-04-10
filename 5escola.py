quantidade_de_alunos = int(input('Quantos alunos têm na escola? ')) #pega o input da quantidade de alunos
notas = [] #define a lista de notas como vazia

def escola(n): #define a função
    if quantidade_de_alunos>2000: #se a quantidade for maior que 2000, executa:
        print('O número de alunos precisa ser menor ou igual a 2000!') #printa o aviso
        return #retorna/cancela a função
    else: #se a quantidade não for menor ou igual a 2000, executa:
        for i in range(n): #laço de repetição que se repete na quantidade de alunos
            nota_individual = float(input(f'Digite a nota do aluno {i+1}: ')) #pega o input da nota individual
            notas.append(nota_individual) #adiciona a nota individual a lista de notas
        dividendo = sum(notas) #define o dividendo como a soma das notas em lista de notas
        media = (dividendo/quantidade_de_alunos) #define a média como o dividendo dividido pela quantidade de alunos
        print(f'A média da turma é: {media}') #printa a média

escola(quantidade_de_alunos) #chama a função