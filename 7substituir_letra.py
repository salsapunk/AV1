def substituir_letra():
    texto = input('Digite a palavra: ')
    letra_mudavel = input('Digite a letra que será substituida: ')
    letra_substitui = input('Digite a letra que substituirá a letra escolhida: ')

    palavras = [palavra for palavra in texto if palavra != "e"]
    resultado = ''.join(palavras)
    print(resultado)

substituir_letra()