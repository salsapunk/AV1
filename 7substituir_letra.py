def substituir_letra():
    texto = input('Digite a palavra: ')
        #pega o input da palavra
    letra_m = input('Digite a letra que será substituida: ')
        #pega o input da letra que será substituida
    letra_s = input('Digite a letra que substituirá a letra escolhida: ')
        #pega o input da letra que vai substituir
    lista_letras = [caractere for caractere in texto]
        #caractere para cada caractere em texto, isso separa os caracteres da string
    palavras = [letra_s if caractere == letra_m else caractere for caractere in lista_letras]
        #se o caractere for igual à letra_m, na lista palavras ele será letra_m
        #se não, ele será igual à lista_letras, ou seja, não sofrem mudança
    resultado = ''.join(palavras)
        #junta as letras separadas em lista numa string
    print(resultado)
    #printa o resultado

substituir_letra()
    #chama a função