texto = input('Digite o texto que deseja inverter: ')

def inverter_texto():
    print(texto[::-1]) #o método split '[::-1]' faz uma cópia de uma lista/string e a inverte (https://docs.python.org/2/whatsnew/2.3.html#extended-slices)

inverter_texto()