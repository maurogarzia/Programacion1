#1_
letter=input("Escriba un palabra para que se repita: ")
for i in range(10):
    print(letter)
#_________________________________________________________
#2_
date=int(input("Ingrese su edad: "))
for i in range(1,date):
    if(i==1):
        print(f"Ha cumplido {i} año ")
    else: 
        print(f"Ha cumplido {i} años")
#_________________________________________________________
#3_LIVE SHAR EXTENSION
number=int(input("Ingrese un numero entero positivo: "))
odd=[]
for i in range(number):
    if(i%2!=0):
        odd.append(str(i))
print(", ".join(odd))

#_________________________________________________________
#4_
number=int(input("Ingrese un numero entero positivo: "))
row=[]
for i in range(number,0,-1):
    row.append(str(i))
print(", ".join(row))
#_________________________________________________________
#5_
years=int(input("Ingrese la cantidad de años a invertir: "))
interest=float(input("Ingrese el porcentaje de interes anual: "))
for i in range(years):
    amount=float(input("Ingrese la cantidad a invertir: $"))
    money=amount*(interest/100)
    print(f"El capital obtenido es: ${money}")
#_________________________________________________________
#6_
number=int(input("Ingrese un numero entero: "))
loop=[]
for i in range(number):
    loop.append("*")
    print("".join(loop))
#__________________________________________________________
#7_
print("TABLAS DE MULTIPLICAR DEL 1 AL 10: ")
for i in range(1,11):
    print("_____________")
    print("Tabla del:",i)
    print("_____________")
    for z in range(11):
        print(f"{i}X{z}={i*z}")
#__________________________________________________________
#8_
number=int(input("Ingrese un numero entero: "))
loop=""
for i in range(number):
    if (i%2!=0):
        loop=str(i)+" "+loop
        print(loop)
#__________________________________________________________
#9_
password="holamundo"
i=1
while (i==1) :
    password1=input("Ingrese la contraseña: ")
    password1=password1.lower()
    if (password1==password):
        i=2
        print("Contraseña correcta, Accediendo...")
    else:
        print("Contraseña incorrecta. Intente de nuevo")
#__________________________________________________________
#10_
number=int(input("Ingrese un numero primo: "))
i=1
while i==1:
    if (number==1 or number==2 or number==3 or number==5):
        print(f"{number} es un numero primo")
    elif(number%2==0 or number%3==0 or number%5==0):
        print(f"{number} no es un numero primo")
    else:
        print(f"{number} es un numero primo")
    i=int(input("Para salir presione 2, sino toque cualquier letra: "))
    if(i==2):
        print("ADIOS..")
#__________________________________________________________
#11_
word=input("Ingrese una palabra: ")
space=len(word)
while space>0:
    print(word[space-1])
    space=space-1
#__________________________________________________________
#12_
phrase=input("Ingrese una frase: ")
letter=input("Que letra quiere buscar dentro de la frase?: ")
phrase=phrase.lower()
letter=letter.lower()
counter=0
loop=len(phrase)
for i in range(loop):
    if(letter==phrase[i]):
        counter+=1
print(f"La cantidad de veces que sale la letra {letter} en la frase es: {counter}")
#__________________________________________________________
#13_
word="hola"
while word!="salir":
    phrase=input("Ingrese una palabra para saber el eco: ")
    counter=len(phrase)
    for i in range(2):
        echo=(phrase[(counter-4):counter])
        print(echo,"...")
    print(f"Desea salir?")
    word=input("Escriba salir para dejar de ingresar palabras, sino toque cualquier letra: ")
#____________________________________________________________
#14_
number1=int(input("Ingrese el primer numero entero: "))
number2=int(input("Ingrese el segundo numero entero: "))
for i in range(number1,number2+1):
    if (i%2==0):
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar")
#____________________________________________________________
#15_
number=int(input("Escriba un numero mayor a 0: "))
dividers=[]
for i in range (1,number):
    if (number%i==0):
        dividers.append(i)
print(f"Los divisores de {number} son: {dividers}")
#____________________________________________________________
#16_
amount=int(input("Ingrese cuantos numeros quiere introducir: "))
negative=0
for i in range (0,amount):
    number=float(input(f"Ingrese el numero {i}: "))
    if(number<0):
        negative+=1
print(f"Se han introducido {negative} numeros negativos")
#____________________________________________________________
#17_
phrase=input("Ingrese una frase: ")
phrase=phrase.lower()
count=len(phrase)
loop=[]
a=False
e=False
i=False
o=False
u=False
for i in range (count):
    loop.append(phrase[i])
    if ("a" in loop):
        a=True
    if ("e" in loop):
        e=True
    if ("i" in loop):
        i=True
    if ("o" in loop):
        o=True
    if ("u" in loop):
        u=True
if (a==True):
    print("Aparece a")
if (e==True):
    print("Aparece e")
if (i==True):
    print("Aparece i")
if (o==True):
    print("Aparece o")
if (u==True):
    print("Aparece u")
#____________________________________________________________
#18_
print("SUCECION DE FIBONACCI")
n1=0
n2=1
print(n1)
print(n2)
for i in range(10):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
#____________________________________________________________
#19_
saving=float(input("Ingresa la cantidad que quiere ahorrar: "))
count=0
while count<saving:
    money=float(input("Ingrese el monto a ahorrar: "))
    if(money<0):
        print("No se puede ahorrar una cantidad negativa")
    else:
        count=count+money
        print(f"Dinero en alcancia: {count}")
print(f"Total ahorrado: {count}")
print("ALCANCIA LLENA")
#____________________________________________________________
#20_
summation=0
i=1
while i!=0 :
    number=float(input("Ingrese un numero: "))
    summation=summation+number
    i=int(input("Si desea salir, presione 0, sino toque cualquier letra: "))
print(f"El total de la sumatoria es: {summation}")
#____________________________________________________________
#21_
big_num=0
i=1
while i!=0:
    number=int(input("Ingrese un numero: "))
    if(number<0):
        print("No se pueden ingresar numeros negativos")
    else:
        if(number>big_num):
            big_num=number
            print(f"Ahora el mayor es {big_num}")
        else:
            print(f"El numero ingresado es menor al mayor")
        i=int(input("Si desea salir, presione 0, sino toque cualquier letra: "))
print(f"El mayor numero ingresado fue: {big_num}")
#____________________________________________________________
#22_
number=int(input("Ingrese un numero distinto de -1: "))
even=0
while number!=-1:
    a=number//10
    b=number%10
    c=a+b
    if(number%2==0):
        even=even+1
    print(f"La suma de los digitos es: {c}")
    number=int(input("Ingrese otro numero: "))
print(f"La cantidad de numeros pares ingresados fueron: {even}")
#____________________________________________________________
#23_
amount=float(input("Ingrese el monto de la compra: $"))
count=0 
while amount!=0:
    count=count+amount
    print(f"Cantidad total: ${count}")
    amount=float(input("Ingrese un importe: $"))
#____________________________________________________________
#24_
i=1
count=0
while i!=0:
    amount=float(input("Ingrese el monto de la compra: $"))
    if(amount<0):
        print("Ingrese un monto positivo")
    elif(amount==0):
        i=0
    else:
        count=count+amount
if(count>1000):
    discount=count*(0.10)
    print(f"Descuento: {discount}")
    count=count-discount
    print(f"El total de las ventas es de: ${count}")
else:
    print(f"El total de las ventas es de: ${count}")
#____________________________________________________________
#25_
facto=int(input("Ingrese un numero para saber su factorial: "))
for i in range (facto):
    if i==0:
        factorial=1
    else:
        factorial=factorial*(i+1)
print(f"El factorial de {facto} es {factorial}")