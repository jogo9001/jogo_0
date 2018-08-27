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
    except:
        print("Impossivel converter o valor digitado para um int\nPermanece o valor anterior: ",n_cidades,"\n\n")
        tmp = None

    if tmp:
        if int(tmp) > 100 or int(tmp) <= 0:
            print('O intervalo válido é somente entre 1 e 100\n\n')
        else:
            n_cidades = int(tmp)   # <---- correcao do outro bug antes era "tmp" string; agora int(tmp) int
            print("novo valor:",n_cidades)
   
    tmp=input("probabilidade de ataques (Atual "+str(prob_ataque)+") :"  )
    try: 
        float(tmp)
    except:
        print('Impossível converter o valor digitado para um float\nPermanece o valor anterior: ', prob_ataque,'\n\n')
        tmp = None
    if tmp:
        if float(tmp)> 1.0 or float(tmp) <= 0.00:
            print('O intervalo válido é somente entre 0.01 e 1.00\n\n')
        else:
            prob_ataque = float(tmp)
            print("novo valor",prob_ataque)

    tmp=input("distancia maxima entre cidades (Atual "+str(max_dist)+") :"  )
    try:
        float(tmp)
    except:
        print('Impossível converter o valor digitado para um float\nPermanece o valor anterior: ', max_dist,'\n\n')
        tmp = None
    if tmp:
        if float(tmp) > 100 or float(tmp) <= 0:
            print('O intervalo válido é somente entre 1 e 100\n\n')
        else:
            max_dist = float(tmp)
            print("novo valor", max_dist)
    return n_cidades,prob_ataque,max_dist

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

