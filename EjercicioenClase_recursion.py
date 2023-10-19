#1_
import random

def caminos():
    temp = 0
    number = random.randint(1,3)
    if number == 1:
        temp += 3
        return temp + caminos()
    elif number == 2:
        temp += 5
        return temp + caminos()
    elif number == 3:
        temp += 7
        return temp
    

print(f"La rata tardo {caminos()} minutos en salir de la jaula")
#-----------------------------------------------------------------
#2_
#Realice un subprograma en el que usando la recursividad, de vuelta un numero ingresado en el programa principal, ej para x = 123, 
#el programa debe devolver 321   