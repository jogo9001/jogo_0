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

def raiz_quadrada(n):
    a = n**0.5
    return a

def calc_dist(px1, py1, px2, py2):
    calc1 = (px1-px2)*(px1-px2)
    calc2 = (py1-py2)*(py1-py2)
    calc3 = calc1 + calc2
    calc4 = raiz_quadrada(calc3)
    return calc4

if __name__ == "__main__":
    calc_dist(3,1,5,2)

