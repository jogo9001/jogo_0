from random import randint

def n_aleatorio(a,b):
    n = randint(a,b)
    return n

def testa_ataque(intervalo):
    n = n_aleatorio(1,intervalo)
    if n == 1:
        return True
    else:
        return False

