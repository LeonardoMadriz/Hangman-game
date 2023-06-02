#Creación de un nódulo que sirva como bucle do while en python
import os
def doWhile(variable):
    aux = variable.isnumeric()
    while aux == True:
        os.system("clear")
        if variable.isnumeric() == True:
            print("Ingrese un valor que sea las letras indicadas")
            aux = True
            variable = input("Introduce [S] para continuar o [N] para salir: ")
        elif variable.isnumeric() == False:
            aux = False
