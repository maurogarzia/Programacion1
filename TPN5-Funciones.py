#1_
def devolver_DNI (number):
    if len(number) == 7 or len(number) == 8:
        return True #Si el string tiene 7 u 8 caracteres devuelve True 
    else:
        return False #Sino, devuelve False

while True:
    dni = input("Ingrese su DNI: ") #Pido DNI
    if (dni.isdigit() == True): #Valido que pueda ser convertido a entero, por si se ingresa una letra
        break
    else:
        print ("No valido, ingrese nuevamente su DNI") #pide DNI nuevamente en caso de error


if (devolver_DNI(dni) == True): #VALIDACION DE DNI
    print("Documento de Identidad VALIDO")
else:
    print("Documento de Identidad NO VALIDO")

#-----------------------------------------------------------

#2_
def devolverPalabra(word):
    prhase = phrase.strip()     #Saco los espacios adelante y atras de la frase
    word = phrase.split()       #Separo las palabras por espacios
    last_word = word[-1]    #Elijo la ultima palabra
    return last_word    #Retorno la ultima palabra


phrase = input("Ingrese una frase: ")
print (devolverPalabra(phrase))

#-----------------------------------------------------------

#3_
def devolver_DNI (number):
    if len(number) == 7 or len(number) == 8:
        return True #Si el string tiene 7 u 8 caracteres devuelve True 
    else:
        return False #Sino, devuelve False

while True:
    name_complete = input ("Ingrese  su nombre y apellido (El programa finalizara en caso de que se ingrese vacio): ")
    if (name_complete == ""):
        break
    else: 
        name_complete = name_complete.strip() #Saco los espacios adelante y atras
        word = name_complete.split() #Separo por palabras

        if (len(word) == 2):
            identifier = word[0] + str(len(word[1])) #Nombre mas apellido
            while True:
                dni = input("Ingrese su DNI: ")
                if (dni.isdigit() == True and devolver_DNI(dni) == True):
                    identifier = identifier + dni[0:3] #Id + 3 primeras letras del DNI
                    break
                else:
                    print ("DNI no valido")
            print(f"Su ID es: {identifier}")
            break

        elif (len (word) == 3):
            identifier = word[0]+str(len(word[2])) #Nombre mas apellido
            while True:
                dni = input("Ingrese su DNI: ")
                if (dni.isdigit() == True and devolver_DNI(dni) == True):
                    identifier = identifier + dni[0:3] #Id + 3 primeras letras del DNI
                    break
                else:
                    print ("DNI no valido")
            print(f"Su ID es: {identifier}")
            break

        else:
            print("Se debe ingresar como minimo: nombre y apellido, y como maximo 2 nombres y un apellido") # Opcion por si se ingresa mas de 3 nombres o 1 solo

print("Saliendo!")
print ("ADIOS...")

#-----------------------------------------------------------

#4_
def multiplos(n1,n2):
    if (n1 % n2 == 0):
        return n1
    elif (n2 % n1 == 0):
        return n2

while True:
    try:
        number_1 = int(input("Ingrese el primer numero: "))
        number_2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Ingrese un numero entero")

if (multiplos(number_1, number_2) == number_1): #Si retorna el primer numero, entonces el primero es multiplo del segundo
    print(f"{number_1} es multiplo de {number_2}")
elif (multiplos(number_1, number_2) == number_2): #Si retorna el segundo numero, entonces el segundo es multiplo del primero
    print(f"{number_2} es multiplo de {number_1}")
else:
    print ("Los numeros no son multiplos") #Por su no retorna ninguno

#-----------------------------------------------------------

#5_
def temp(minimal,maxima):
    average = (minimal + maxima) / 2
    return average

i = 0
while True:
    try:
        days = int(input("Ingrese el numero de dias en los que se va a medir la temperatura media: ")) #Ingreso cantidad de dias
        while True:
            try:
                for i in range (0,days):            
                    min = float(input(f"Ingrese la temperatura minima del dia {i+1} : "))   # Ingreso temperatura minima
                    max = float(input(f"Ingrese la temperatura maxima del dia {i+1} : "))   # Ingreso temperatura maxima
                    print (f"\nLa temperatura media del dia {i+1} fue {temp(min,max)}º\n")  #Llamo a la funcion
                break
            except ValueError:
                print("Debe ingresar una temperatura valida")
        break
    except ValueError:
        print("Debe ingresar un numero entero")

#-----------------------------------------------------------

#6_
def separar(word):
    word = word.strip()
    distance = len(word) #Cuento cuantas letras tiene la palabra (contando los espacios)
    i = 0
    list = ""
    for i in range (0, distance):
        list = list + (word[i] + " ") #sumo un string vacio con la letra de la palabra mas un espacio
    return list

phrase = input("Ingrese una frase: ")
print(separar(phrase)) #Llamo a la funcion

#-----------------------------------------------------------

#7_
def min_max(numbers):
    i = 1
    minimal = min(numbers)
    maximo = max(numbers)
    while True:
        print ("Si desea ver el maximo presione 2, si desea ver el minimo presione 3")
        option = input()
        if option == '2' :
            return maximo
        elif option == '3':
            return minimal
        else:
            print("Caracter invalido")

list = []
while True:
    try:
        distance = int(input("Ingrese cuantos valores numericos desea agragar a la lista: "))
        while True:
            try:
                for i in range (0,distance):
                    value = float(input(f"Ingrese el valor {i} de la lista: "))
                    list.append(value)
                break
            except ValueError:
                print ("Los valores deben ser numericos")
        print (list)
        print (min_max(list))
        break
    except ValueError:
        print ("Debe ingresar un valor entero")

#-----------------------------------------------------------

#8_
import math

def devolverRadio(rad):
    area = math.pi * rad**2
    perimeter = 2 * math.pi * rad
    return print(f"Area = {area}, Perimetro = {perimeter}")


while True:
    try:
        radio = float(input("Ingrese el radio de la circunferencia: "))
        devolverRadio(radio)
        break
    except ValueError:
        print ("Caracter ingresado no valido, intente nuevamente")

#-----------------------------------------------------------

#9_
def login(user, passw):
    if user == "usuario1" and passw == "asdasd" :
        return True
    else: 
        return False

i = 0
while i < 3 :
    user_name = input("Ingrese su usuario: ")
    user_name = user_name.lower()
    password = input("Ingrese una contraseña para loguearse: ")
    if login(user_name, password) == True:
        print ("\nUsuario y contraseña validos!")
        print ("Accediendo...")
        break
    else :
        print ("Usuario y contraseña invalidos")
        print ("--------------------------------")
        i = i + 1

#-----------------------------------------------------------

#10_ 
def aplicar_descuento(shopping_cart, discounts, option):
    if option in shopping_cart:
        price = shopping_cart[option]
        if option in discounts:
            disc = discounts[option]
            new_price = price * (1 - disc / 100)
            return new_price
        else:
            return price
    else:
        return print("Producto no encontrado en el carrito")


shopping_cart = {
    'producto1': 100,
    'producto2': 50,
    'producto3': 75
}

discounts = {
    'producto1': 10,
    'producto3': 5
}

print("Productos disponibles en el carrito:")
for product in shopping_cart.keys():
    print(product)

option = input("Elija un producto del carrito: ")

final_price = aplicar_descuento(shopping_cart, discounts, option)

if isinstance(final_price, str):
    print(final_price)
else:
    print(f'El precio final con descuento para {option} es: {final_price}')

#-----------------------------------------------------------

#11_
def suma_listas(list1,list2):
    sum = []
    for i in range (0,2):
        sum.append(list1[i] + list2[i])
    return sum

def multi_listas(list1,list2):
    list = []
    for i in range (0,2):
        list.append(list1[i] * list2[i])
    return list

list = []
list2 = []
for i in range (0,2):
    while True:
        try:
            number = int(input(f"Ingrese el valor de la posicion {i} que desea añadir a la lista 1: "))
            number2 = int(input(f"Ingrese el valor de la posicion {i} que desea añadir a la lista 2: ")) 
            list.append(number)
            list2.append(number2)
            break
        except ValueError:
            print("Ingrese un numero entero")
print (f"Lista 1: {list}")
print (f"Lista 2: {list2}")
summation = suma_listas(list, list2)
print (f"Sumatoria de listas: {summation}")
multi = multi_listas(summation,list)
print (f"Multiplicacion de la sumatoria con la primer lista: {multi}")

#-----------------------------------------------------------

#12_ 
def longitud(word):
    separated_words = word.split()
    dictionary = {}

    for i in separated_words:
        long = len(i)
        dictionary[i] = long
    
    return dictionary

phrase = input("Ingrese una frase: ")

result = longitud(phrase)
print(result)

#-----------------------------------------------------------

#13_
def modulo(x,y):
    modul = pow(x,2) + pow(y,2)
    result = pow(modul, 1/2)
    return result

while True:
    try:
        component_x = int(input("Ingrese la componente x del vector: "))
        component_y = int(input("Ingrese la componente y del vector: "))
        print ("El modulo es: ", modulo(component_x,component_y))
        break
    except ValueError:
        print ("Debes ingresar un numero entero: ")

#-----------------------------------------------------------

#14_
def es_primo(num):
    if num == 2 or num == 3 or num == 5 or num == 7 :
        result = True
    elif num %2 != 0 and num != 1 and num %3 != 0 and num %5 != 0 and num %7 != 0 :
        result = True
    else: 
        result = False
    return result

while True:
    try:
        number = int(input("Ingrese un numero: "))
        if (es_primo(number) == True):
            print (f"{number} es primo")
        else:
            print(f"{number} no es primo")
        break
    except ValueError:
        print ("Debe ingresar un numero primo")

#-----------------------------------------------------------
#15_

def factorial (n):
    if n < 0:
        return print("No se puede calcular el factorial de un numero negativo")
    elif n == 0 :
        return print("El factorial de 0 es 1")
    else: 
        result = 1
        for i in range (1 , n + 1):
            result = result * i
        return result

def contador(list):
    count = int(len(list))
    return count

i = '2'
list = []
while True:
    try:
        while i != '1':
            num = int(input("Ingrese un numero entero: "))
            list.append(num)
            print (f"El factorial de {num} es: ", factorial(num))
            i = input ("\nPara salir presiones 1, sino toque cualquier boton: ")
        break
    except ValueError:
        print("Debe ingresar un numero entero")
print ("La cantidad de veces que se ingreso un numero es: ", contador(list))

#-----------------------------------------------------------

#16_
def frecuencia(num,digit):
    count = 0
    while num > 0:
        last_digit = num % 10
        if last_digit == digit:
            count = count + 1
        num = num // 10
    return count

while True:
    try:
        num = int(input("Ingrese un numero: "))
        digit = int(input("Ingrese un digito: "))
        print (f"La frecuencia del digito en el numero es de: ", frecuencia(num,digit))
        break
    except ValueError: 
        print ("Debe ingresar un numero entero")

#-----------------------------------------------------------

#17_
def factorial (n):
    if n < 0:
        return print("No se puede calcular el factorial de un numero negativo")
    elif n == 0 :
        return print("El factorial de 0 es 1")
    else: 
        result = 1
        for i in range (1 , n + 1):
            result = result * i
        return result


def frecuencia(num,digit):
    count = 0
    while num > 0:
        last_digit = num % 10
        if last_digit == digit:
            count = count + 1
        num = num // 10
    return count

def es_primo(num):
    if num == 2 or num == 3 or num == 5 or num == 7 :
        result = True
    elif num %2 != 0 and num != 1 and num %3 != 0 and num %5 != 0 and num %7 != 0 :
        result = True
    else: 
        result = False
    return result


def suma_digitos(num):
    sum = 0
    if num < 10:
        sum = num
        return sum
    else:
        while num > 0 :
            sum = sum + num % 10
            num = num // 10
        return sum
            
elderly = 0
prime_numbers = 3
while es_primo (prime_numbers) == True:
    try:
        prime_numbers = int(input("Ingrese numeros primos: "))
        if es_primo(prime_numbers) == True:
            if prime_numbers > elderly :
                elderly = prime_numbers
            
            print ("La suma de sus digitos es: ", suma_digitos(prime_numbers))
            while True:
                try:
                    digit = int(input("Ingrese un digito: "))
                    print (f"La frecuencia del digito en el numero es de: ", frecuencia(prime_numbers,digit))
                    break
                except ValueError:
                    prime_numbers("El digito ingreado debe ser un entero")
        else:
            print ("El numero ingresado no es primo")
            break
            
    except ValueError:
        print ("El numero ingresado debe ser entero")
print (f"El factorial de {elderly} es: ", factorial(elderly))