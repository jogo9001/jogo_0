#!/usr/bin/env python
import os
def inicio():
    if os.name == "posix":
        os.system('clear')
        print('Estou num POSIX')
    elif os.name in ("nt", "dos", "ce"):
        os.system('cls')
        print('Estou num win')
    else:
        print('Não estou num unix nem num win')




