#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def inicio():
    if os.name == "posix":
        clear()
        print('Estou num POSIX')
    elif os.name in ("nt", "dos", "ce"):
        clear()
        print('Estou num win')
    else:
        print('Não estou num unix nem num win')

def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('cls')


def start():
    print("aqui comeca o jogo")

def config():
    print("aqui configura tudo")

def tela_inicial():
    opc=input("1-Iniciar\n2-Opções\n: ")
    if opc == "1":
        start()
    elif opc == "2":
        config()
    else:
        clear()
        tela_inicial()



if __name__ == "__main__":

    inicio()
    tela_inicial()

