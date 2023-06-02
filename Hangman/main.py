import random
import os
import sys
from do_while import doWhile

def read():
    list=[]
    with open("../DataBase/data.txt","r",encoding="utf-8") as f:
        for line in f:
            list.append(line)
    return list[random.randint(1,170)]

def welcome():
    os.system("clear")
    print("Bienvenido al juego del Ahorcado ")
    select=input("Introduce [S] para continuar o [N] para salir: ")
    doWhile(select)
    select=select.lower()

    if select == "s":
        pass
    elif select == "n":
        sys.exit(1)
    else:
        print("Valor no conocido")
        sys.exit(1)
    return 0

def run():
    welcome()
    word= read()
    print(word)

if __name__ == "__main__":
    run()
