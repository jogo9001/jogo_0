#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
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


def start():
    print("aqui comeca o jogo")

def config():
    print("aqui configura tudo")

def sair():
    print("saindo...")

def tela_inicial():
    opc=input("1-Iniciar\n2-Opções\n\n0-Sair\n\n\n: ")
    if opc == "1":
        start()
    elif opc == "2":
        config()
    elif opc == "0":
        sair()
    else:
        clear()
        tela_inicial()



if __name__ == "__main__":

    inicio()
    tela_inicial()

