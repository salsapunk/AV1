x = int(input('Digite um dos números do intervalo: '))
y = int(input('Digite o outro número do intervalo: '))

if x>y: #checa se x é maior que y
    for i in range (y, x+1): #loop no alcance do intervalo de y a x
        if i % 5 == 2: #se o resto da divisão do número no intervalo por 5 for 2
            print(i) #printa o número
        if i % 5 == 3: #se o resto da divisão do número no intervalo por 5 for 3
            print(i) #printa o número
else: #checa se y é maior que x
    for i in range (x, y+1): #loop no alcance do intervalo de x a y
        if i % 5 == 2: #se o resto da divisão do número no intervalo por 5 for 2
            print(i) #printa o número
        if i % 5 == 3: #se o resto da divisão do número no intervalo por 5 for 3
            print(i) #printa o número