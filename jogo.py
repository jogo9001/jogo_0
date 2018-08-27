#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

n_cidades = 10
prob_ataque = 0.01
max_dist = 100

def inicio():
    clear()
    print("System: ",os.name)

def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('cls')
    else:
        print('Não estou num win nem num unix')
        sair()

def start(n_c, p_a, m_d):
    print("aqui comeca o jogo",n_c,p_a,m_d)

def config(n_cidades,prob_ataque,max_dist):
    print("configurações:")
    tmp=input("numero de cidades (Atual "+str(n_cidades)+") :"  )
    try:    
        int(tmp)
        n_cidades = int(tmp)   # <---- correcao do outro bug antes era "tmp" string; agora int(tmp) int
        print("novo valor:",n_cidades)
    except:
        print("Impossivel converter o valor digitado para um int\nPermanece o valor anterior: ",n_cidades,"\n\n")
    
    if n_cidades > 100 or n_cidades <= 0:
        print('O intervalo válido é somente entre 1 e 100')
        #config(n_cidades,prob_ataque,max_dist) <------ e melhor simplesmente ir pra proxima variavel nao e necessario ficar reiniciando toda vez.  

    tmp=input("probabilidade de ataques (Atual "+str(prob_ataque)+") :"  )
    try: 
        float(prob_ataque)
        prob_ataque = tmp
        print("novo valor",prob_ataque)
    except:
        pass

    if float(tmp)> 1.0 or float(tmp) <= 0.00:
        print('O intervalo válido é somente entre 0.01 e 1.00')
        config(n_cidades,prob_ataque,max_dist)

    tmp=input("distancia maxima entre cidades (Atual "+str(max_dist)+") :"  )
    try:
        float(max_dist)
        max_dist = tmp
        print("novo valor", max_dist)
    except:
        pass
    return n_cidades,prob_ataque,max_dist

    if float(tmp) > 100 or float(tmp) <= 0:
        print('O intervalo válido é somente entre 1 e 100')
        config(n_cidades,prob_ataque,max_dist)

def sair():
    print("saindo...")
    exit(1)

def tela_inicial():
    global n_cidades
    global prob_ataque
    global max_dist
    opc=input("1-Iniciar\n2-Opções\n\n0-Sair\n\n\n: ")
    if opc == "1":
        start(n_cidades,prob_ataque,max_dist)
    elif opc == "2":
        n_cidades,prob_ataque,max_dist=config(n_cidades,prob_ataque,max_dist)
    elif opc == "0":
        sair()
    else:
        clear()
    tela_inicial()



if __name__ == "__main__":

    inicio()
    tela_inicial()

