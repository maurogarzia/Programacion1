def repeticiones_not(array1,array2):#Muestro los elementos del array1 que no se repiten en array2
    students_primary = []
    for i in array1: 
        if i not in array2:
            students_primary.append(i)
    return students_primary

#-----------------------------------------------------------------------------------------------

def repeticiones_mas_de_una_vez(array): #Muestra los elementos que se repiten mas de una
    new_list = []
    for i in array:
        counter = array.count(i) #Cuento cuantas veces se repiten los elementos
        if counter > 1:
            new_tupla = (i,f"Se repite: {counter}")
            new_list.append(new_tupla) #Agrego la tupla con el vlaor de la posicion y las veces que se repite a una lista
    new_list = set(new_list)
    return new_list

#-----------------------------------------------------------------------------------------------

def repeticiones_todos(array): #Muestra los elementos que se repiten y los que no se repiten
    new_list = []
    for i in array:
        counter = array.count(i) #Cuento cuantas veces se repiten los elementos
        new_tupla = (i,f"Se repite: {counter}")
        new_list.append(new_tupla) #Agrego la tupla con el valor de la posicion y las veces que se repite a una lista
    new_list = set(new_list)
    return new_list

#-----------------------------------------------------------------------------------------------

def verificar_nombre(variable): #Funcion para validar un sustantivo propio
    list_numbers = "123456789"
    list_special_characters = "!@#$%^&*()_+}{|?><,./[]"
    for i in range (0,len(variable)):
        if variable[i] not in list_numbers and variable[i] not in list_special_characters:
            check = True
        else:
            check = False
    return check

#-----------------------------------------------------------------------------------------------

def devolver_fichas(): #Pide la posicion de las fichas y valida que sea correcta (memotest)
    while True:
        try:
            position = int(input(">"))
            if position > 3 :
                print("Posicion invalida, intentelo de nuevo")
            elif position < 0 :
                print("Posicion invalida, intentelo de nuevo")
            else:
                break
        except ValueError:
            print("Posicion invalida, intentelo de nuevo")