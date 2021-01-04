from random import randint
sorteio = []

def loteria():
    cont = 0
    while cont < 6:
        x = randint(1,60)
        if x not in sorteio:
            sorteio.append(x)
        cont += 1
    return sorteio
