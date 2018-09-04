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
def gen_cidade_coordenadas(screen_min_x, screen_max_x, screen_min_y, screen_max_y):
    x=n_aleatorio(screen_min_x,screen_max_x)
    y=n_aleatorio(screen_min_y,screen_max_y)
    return [x,y]
def checa_dist(px1, py1, px2, py2, MAXDIST):
    if calc_dist(px1, py1, px2, py2) > MAXDIST and calc_dist(px1, py1, px2, py2) == 0:
        return False
    else:
        return True
