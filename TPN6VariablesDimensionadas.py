from FuncionesTP6 import * #IMPORTO LAS FUNCIONES
#1_
numbers_arrays = []
while True:
    try:
        number = float(input("Ingrese un numero para agregar a la lista (Para salir ingrese 0) : ")) #INPUT DE NUMEROS 
        if (number == 0):
            break
        else:
            numbers_arrays.append(number) #AGREGO LOS NUMEROS A UNA LISTA
    except ValueError:
        print ("Debe ingresar un numero")
print (numbers_arrays)
#--------------------------------------------------------------------
#2_
while True:
    try: 
        other_number = float(input("\nIngrese otro numero: ")) #PIDO OTRO NUMERO
        break
    except ValueError:
        print("Debe ingresar un numero")

distance = len(numbers_arrays) #LONGITUD DE LA LISTA numbers_arrays
for i in range (0 , distance - 1) :
    if other_number == numbers_arrays[i] : #COMPARO SI EL NUMERO SE ENCUENRTRA EN LA LISTA
        del numbers_arrays[0] #SI LA CONDICION SE CUMPLE SE ELIMINA EL ELEMENTO DE LA PRIMERA POSICION

if len(numbers_arrays) < distance: #CONDICIONAL DE SI HUBO MODIFICACIONES EN LA LISTA
    print("\nSe elimino la primer ocurrencia: ", numbers_arrays)
else:
    print("No fue posible eliminar la primera ocurrencia: ", numbers_arrays)
#--------------------------------------------------------------------
#3_
summation = 0

for i in range (0, len(numbers_arrays)):
    summation = summation + numbers_arrays[i] #SUMO TODOS LOS NUMEROS DE LA LISTA
print("\nLa sumatoria de los numeros dentro de la lista es: ",summation,"\n")
#--------------------------------------------------------------------
#4_
loop = []
while True:
    try:
        number_of_new_list = float(input("Ingrese otro numero para el cual la lista sera menor: ")) #PIDO UN NUMERO CUALQUIERA
        break
    except ValueError:
        print("Debe ingresar un numero: ")

small_than = 0
for i in range(0,len(numbers_arrays)):

    if numbers_arrays[i] > number_of_new_list: #SI EL NUMERO DE LA POSICION i DE LA LISTA ES MAYOR AL NUMERO ANTERIORMENTE PEDIDO ENTRA EN EL if
        while (numbers_arrays[i] > number_of_new_list):
            numbers_arrays[i] = numbers_arrays [i] - number_of_new_list #RESTA EL NUMERO PEDIDO AL NUMERO DE LA POSICION TANTAS VECES SEA NECESARIO, HASTA QUE SEA MENOR AL NUMERO PEDIDO
        small_than = numbers_arrays[i] 
        loop.append(small_than) #EL NUMERO SE LO ASIGNO A UNA VARIABLE Y LA AGREGO A OTRA LISTA
    else:
        loop.append(numbers_arrays[i]) #SI NO SE CUMPLE LA PRIMER CONDICION SE AGREGA EL NUMERO ORIGINAL DE LA LISTA
print("\nLa nueva lista con numeros menores al ingresado es: ",loop)

#--------------------------------------------------------------------
#5_
repeated_numbers = set(numbers_arrays) #A UN CONJUNTO LE ASIGNO LA LISTA DE numbers_arrays PARA QUE NO SE REPITAN ELEMENTOS
new_list = []

for i in repeated_numbers:
    counter = numbers_arrays.count(i) #CUENTO CUANTAS VECES SE REPITEN LOS ELEMENTOS
    new_tupla = (i,counter)
    new_list.append(new_tupla) #AGREGO LA TUPLA CON EL VALOR DE LA POSICION Y LAS VECES QUE SE REPITE A UNA LISTA
print(f"Lista con la cantidad de veces que se repite un numero: {new_list}")
#--------------------------------------------------------------------
#6_
list_numbers = "123456789" #CADENA DE NUMEROS PARA SABER SI SE INGRESAN EN UN NOMBRE 
primary = []

while True:
    students_names = input("Ingrese los nombres de los alumnos de primaria (Para finalizar ingrese x): ")
    if students_names == "x":
        break
    else: 
        for i in range (0,len(students_names)):
            if students_names[i] not in  list_numbers: #SI NO HAY NUMEROS DEVUELVE True, SINO DEVUELVE False
                check = True
            else:
                check = False
        if check == True: #SI EL NOMBRE ES VALIDO LO AGREGO A students_names
            students_names = students_names.title()
            primary.append(students_names)
print("\n",primary)

#EL BLOQUE DE CODIGO SIGUIENTE ES IGUAL AL ANTERIOR PERO CON ESTUDUIANTES DE SECUNDARIA 

secundary = []
while True:
    students_names = input("Ingrese los nombres de los alumnos de primaria (Para finalizar ingrese x): ")
    if students_names == "x":
        break
    else: 
        for i in range (0,len(students_names)):
            if students_names[i] not in  list_numbers:
                check = True
            else:
                check = False
        if check == True:
            students_names = students_names.title()
            secundary.append(students_names)
print("\n",secundary)

amount_students = primary

for i in range (0,len(secundary)):
    amount_students.append(secundary[i]) #AGREGO TODOS LOS ESTUDIANTES A UNA MISMA LISTA

total_students = set(amount_students) #LOS ASIGNO A UN CONJUNTO PARA QUE NO SE REPITAN
print("Cantidad total de estudiantes: ", total_students)

from FuncionesTP6 import * #IMPORTO FUNCIONES DE OTRO ARCHIVO QUE VOY A USAR EN ESTE ARCHIVO

repeticiones_mas_de_una_vez(amount_students) #FUNCION DEVUELVE TODOS LOS ESTUDIANTES SIN REPETIR
print ("Los estudiantes de primaria que no se repiten en secundaria son: ",repeticiones_not(primary,secundary))
#--------------------------------------------------------------------
#7_
strings = "" #CADENA DE CARACTERES
counter = 0 #INICIO CONTADOR

while counter < 50: #CUANDO EL CONTADOR SEA 50 SALE DEL BUCLE
    word = input("Ingrese un string: ")
    counter += 1
    strings = strings + word #LE SUMO LOS IMPUTS A LA CADENA DE CARACTERES
print(repeticiones_todos(strings)) #LLAMO A FUNCION QUE CUENTA TODOS LOS CARACTERES Y CUANTAS VECES APARECEN
#--------------------------------------------------------------------
#8_
def seepoints(sporteamslocaltwo):
    counterwins = 0
    counterdraws = 0
    counterallpoints = []

    for rows in range(len(sporteamslocaltwo)):
        for columns in range(len(sporteamslocaltwo)):
            if sporteamslocaltwo[rows][columns] > sporteamslocaltwo[columns][rows]:
                counterwins += 3
            elif sporteamslocaltwo[rows][columns] == sporteamslocaltwo[columns][rows]:
                counterdraws += 1
        counterallpoints.append(counterdraws+counterwins)
        counterwins = 0
        counterdraws = 0
    counteraux = 0
    for rows in sporteams:
        print(f"El equipo {counteraux+1} quedo con {counterallpoints[counteraux]} puntos")
        counteraux += 1
        
def diff(sportteamslocaltwo):
    counteraux = 0
    counterauxtwo = 0
    for rows in range(len(sportteamslocaltwo)):
        for columns in range(len(sportteamslocaltwo)):
            if rows != columns:
                print(f"Diferencia entre goles marcados y recibidos para el equipo {counteraux+1} con el equipo {counterauxtwo+1}: : {abs(sportteamslocaltwo[rows][columns] - sportteamslocaltwo[columns][rows])}")
            counterauxtwo += 1
        counteraux += 1
        counterauxtwo = 0
    print("---------------------------------------------------")
def showingvictsdefeatsanddraws(counterallgoalslocaltwo):
    counteraux = 0

    for rows in counterallgoalslocaltwo:
        for columns in range(len(rows)):
            if columns==0:
                print(Fore.GREEN+f"O"*rows[columns]+Style.RESET_ALL+f" {rows[columns]} victoria/s para el equipo {counteraux+1}")
            if columns==1:
                print(Fore.RED+f"O"*rows[columns]+Style.RESET_ALL+f" {rows[columns]} derrota/s para el equipo {counteraux+1}")
            if columns==2:
                print(Fore.YELLOW+f"O"*rows[columns]+Style.RESET_ALL+f" {rows[columns]} empate/s para el equipo {counteraux+1}")
        counteraux+=1
        print("-----------------------------------------------------")
def choose(choicelocal, counterallgoalslocal, sporteamslocal):
    if choicelocal == "1":
        showingvictsdefeatsanddraws(counterallgoalslocal)
    elif choicelocal == "2":
        diff(sporteamslocal)
    elif choicelocal == "3":
        seepoints(sporteamslocal)


while True:
    import random as ran
    from colorama import Fore, Style 
    countergreens = 0
    counterreds = 0
    counteryellows = 0
    counter = []
    counterallgoals = []
    sporteams = [[0 for elem in range(10)] for elem in range(10)]
    for visitant in range(len(sporteams)):
        for local in range(len(sporteams)):
            if visitant == local:
                sporteams[visitant][local] = 0
            else:
                sporteams[visitant][local] = ran.randrange(0, 6)
    for elem in range(len(sporteams)):
        counter = []
        for elemtwo in range(len(sporteams)):
            if sporteams[elem][elemtwo] > sporteams[elemtwo][elem]:

                print(Fore.GREEN + "["+str(sporteams[elem][elemtwo]), end = "]"+Style.RESET_ALL)
                countergreens += 1
            elif sporteams[elem][elemtwo]<sporteams[elemtwo][elem]:
                print(Fore.RED + "["+str(sporteams[elem][elemtwo]), end = "]"+Style.RESET_ALL)
                counterreds += 1
            elif sporteams[elem][elemtwo]==sporteams[elemtwo][elem]:
                print(Fore.YELLOW + "["+str(sporteams[elem][elemtwo]), end = "]"+Style.RESET_ALL)
                counteryellows += 1 
            elif sporteams[elem][elemtwo] == sporteams[elem][elem]:
                print("["+str(sporteams[elem][elemtwo]), end = "]")
        print("")
        counter.append(countergreens)
        counter.append(counterreds)
        counter.append(counteryellows)
        counterallgoals.append(counter)
        countergreens = 0
        counterreds = 0
        counteryellows = 0
    counteraux=0

    print("Dado esta tabla de goles y equipos, elija una opcion\n"
        "1) Ver victorias, derrotas y empates de cada equipo\n"
        "2) Ver diferencia entre goles marcados y recibidos de cada equipo\n"
        "3) Ver los puntos que cada equipo obtuvo")
    choice=input()
    choose(choice, counterallgoals,(sporteams))


#--------------------------------------------------------------------
#9_

attempts = 0 #Numero de intentos que se haran para completar el juego
memory = []#En esta variable guardo los pares encontrados

board = [
    [1,1,2,2],  #Tablero del memotest
    [3,3,4,4],
    [5,5,6,6],
    [7,7,8,8],
] 

print("VAMOS A JUGAR AL MEMOTEST")
while (len(memory) < 8):
    print (len(memory))
    print ("Intento numero: ",attempts)
    counter = 0 #Contador para bucle while en el que se van a hacer los intentos de las fichas
    while True:

        print("Ingrese la coordenada X de la posicion de la que desea levantar la ficha:  ")
        position_1 = devolver_fichas()
        print("Ingrese la coordenada Y de la posicion de la que desea levantar la ficha:  ")
        position_2 = devolver_fichas()

        counter += 1

        if counter == 1:
            tab1 = board[position_1][position_2]
            print(f"Ficha levantada: {tab1}")
        elif counter == 2:
            tab2 = board[position_1][position_2]
            print(f"Ficha levantada: {tab2}")
        elif tab1 == tab2:
            print("Estas levantando la misma ficha")
            break

    if tab1 == tab2: #Condicional por si se encuentra el par
        print ("PAR ENCONTRADO")
        print(f"El par encontrado es {tab1}, {tab2}")
        if tab1 not in memory:
            memory.append(tab1) #Si el par encontrado no habia sido encontrado anteriormente, lo guardo en una lista. Sino lo informo con un
            attempts += 1
        else:
            print("Par ya encontrado anteriormente...")
            attempts += 1
    else:
        print("PAR NO ENCONTRADO! intentelo de nuevo...")
        attempts += 1 

    if len(memory) == 8:
        break
print("JUEGO TERMINADO")
print("Se intento un numero de veces: ",attempts)

#--------------------------------------------------------------------
#10_
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("MATRIZ :")
for i in matrix:
    print(i)

dimension = len(matrix)

main_diagonal = [matrix [i][i] for i in range (dimension)]
reverse_diagonal = [matrix [i][dimension - 1 - i] for i in range(dimension)]

print("\nDiagonal Principal: ",main_diagonal)
print("\nDiagonal Inversa: ",reverse_diagonal)

#--------------------------------------------------------------------
#11_
dictionary = {'Euro': '€', 'Dollar':'$', 'Yen':'¥'}

option = input("Ingrese una divisa: ")
option = option.title()

if option in dictionary:
    symbol = dictionary[option]
    print(symbol)
else:
    print("La divisa ingresada no se encuentra en el diccionario")
#--------------------------------------------------------------------
#12_
while True: #PIDO EL INGRESO DEL NOMBRE
    name = input("Ingrese su nombre: ")
    if verificar_nombre(name) == True:
        name = name.title()
        break
    elif verificar_nombre(name) == False:
        print("Ingrese un nombre valido")

while True: #PIDO LA EDAD
    try:
        age = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("Ingrese una edad valida")

address = input("Ingrese su direccion: ")

while True:#PIDO UN NUMERO DE TELEFONO
    try:
        phone = int(input("Ingrese su numero de telefono: "))
        if phone > 9999999999 or phone < 100000000: #SI EL NUMERO TIENE MAS O MENOS DE 10 CIFRAS ES INVALIDO
            print("Ingrese un numero de telefono valido")
        else:
            break
    except ValueError:
        print("Ingrese un numero de telefono valido")

user = { #CREO DICCIONARIO CON: edad, nombre, telefono y direccion
    'nombre': name,
    'edad': age,
    'telefono':phone,
    'direccion': address
}

message = (f"{user['nombre']} tiene {user['edad']} años, vive en {user['direccion']} y su número de teléfono es {user['telefono']}.")

print (message)


#--------------------------------------------------------------------
#13_

print("PRECIOS DE FRUTAS: ")
print("Manzana: $300 el kilo\nPera: $400 el kilo\nUva: $250 el kilo\nBanana: $500 el kilo ")

dictionary = { #CREO DICCIONARIO CON LAS FRUTAS DE LA TABLA
    'manzana': 300,
    'pera': 400,
    'uva': 250,
    'banana': 500
}

option = input("Ingrese la fruta que desea comprar: ")
option = option.lower()

while True:
    try:    
        kg = float(input("Ingrese cuantos kilos desea comprar: ")) #PIDO QUE LOS KILOGRAMOS SEA UN float
        break
    except ValueError:
        print("Ingreso invalidado")

if option in dictionary: #VALIDO QUE LA FRUTA ESTE EN EL DICCIONARIO
    total_price = dictionary[option] * kg
    print(f"El precio a pagar es: {total_price}")
else:
    print(f"{option} no se encuentra en la tabla")

