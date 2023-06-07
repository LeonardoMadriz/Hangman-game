import random
import os
import sys
from do_while import doWhile
import cowsay

def read():
    list=[]
    with open("../DataBase/data.txt","r",encoding="utf-8") as f:
        for line in f:
            list.append(line)

        chosen_word=list[random.randint(1,170)]
        chosen_word=chosen_word.strip()
        return chosen_word


def welcome():
    os.system("clear")
    print(cowsay.get_output_string('tux',"Bienvenido al juego del ahorcado"))
    select=input("\n\nIntroduce [S] para continuar o [N] para salir: ")
    doWhile(select)
    select=select.lower()

    if select == "s":
        pass
    elif select == "n":
        print("Adios!!!")
        sys.exit(1)
    else:
        print("Valor no conocido")
        sys.exit(1)
    return 0

def enviroment(word):
    space_word=len(word)
    print("_"*space_word)

def run():
# Bienvenida y carga de datos
    word= read()
    welcome()
    print(word)


# Algoritmo del juego
    secret_word = "_" * len(word)
    os.system('clear')
    messenger ="Que comience el juego!"
    attempts=10
    
    while secret_word.find("_") != -1:
        os.system("clear")
        print(cowsay.get_output_string('tux',messenger))
        print(secret_word)
        print(word)
        print(f"\nVidas: {attempts}")
        secret_word=list(secret_word)
        new_word=input("\nIngrese una palabra: ")

        for value in enumerate(word):
            index=value[0]
            if new_word==value[1]:
                secret_word[index] = value[1]
                messenger="Excelente!"
        secret_word = "".join(secret_word)


    

if __name__ == "__main__":
    run()
