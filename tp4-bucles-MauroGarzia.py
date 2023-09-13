#1_
x=0
while x < 30:
    if x == 15:
        print("La ejecución del bucle se interrumpió cuando x era", x)
        break
    elif x==4 or x==6 or x==10:
        print("Se omitió el valor", x, "de x")
    else:
        print("El valor del bucle es:", x)
    x += 1
#_______________________________________
#2_
loop=1
while loop==1:
    line=input("Ingrese lineas de codigo: ")
    if(line==""):
        break
#_______________________________________
#3_
loop=1
i=0
bank=1000
balance=[]
while loop==1:
    print("1)_PARA RETIRAR DINERO")
    print("2)_PARA DEPOSITAR DINERO")
    binnacle=input("Ingrese la opcion a realizar: ")
    if(binnacle=="1"):
        extraction=float(input("Retiro: "))
        bank=bank-extraction
        balance.append("R "+str(extraction))
        
        i+=1
    elif(binnacle=="2"):
        deposit=float(input("Deposito: "))
        bank=bank+deposit
        balance.append("D "+str(deposit))
        i+=1
    elif(binnacle==""):
        break
    else:
        print("Comando ingresado no valido")
print("Historial de movimientos: ")
for z in range (0,i):
    print(balance[z])

print("Total: ",bank)
#___________________________________________
#4_
numbers=1
prime_number=0
while numbers!=0:
    numbers=int(input("Ingrese numeros mayores a 0 (Para salir ingrese 0):"))
    if numbers==0:
        break
    elif numbers<0:
        print("Los numeros ingresados deben ser mayores a 0")
    else:
        if  numbers==2 or numbers==3 or numbers==5: 
            prime_number+=1
        elif numbers%2!=0 and numbers%3!=0 and numbers%5!=0 and numbers!=1:
            prime_number+=1
print(f"La cantidad de numeros primos ingresados es: {prime_number}")
#____________________________________________________
#5_
year1=int(input("Ingrese un año: "))
year2=int(input("Ingrese otro año: "))
if year1>year2:
    while year1>year2:
        year2+=1
        if ((year2%4==0 and year2%100!=0) or (year2%4==0 and year2%400==0)) and (year2%10==0) :
            print(year2)
elif year2 > year1:
    while year2>year1:
        year1 += 1
        if ((year1%4 == 0 and year1%100 !=0 ) or (year1%4==0 and year1%400==0)) and (year1%10==0) :
            print(year1)
else:
    print("Es el mismo año")
#____________________________________________________
#6_
for i in range(0,21):
    if i % 2 != 0:
        continue
    else: 
        print(i)
#____________________________________________________
#7_
list=[1,2,3,4,5,6]
for i in range(0,6):
    print(i)
    if i == 4:
        break
print("FINALIZANDO...")
#_____________________________________________________
#8
i=1
while i==1:
    print("1)_SALUDAR\n2)_DESPEDIRSE\n3)_FRASE MOTIVACIONAL")
    option=int(input("Ingrese una de las tres opciones (Ingrese 0 para salir): "))
    if option==0:
        break
    elif option==1:
        print("HOLAAA\n")
    elif option==2:
        print ("ADIOSSS\n")
    elif option==3:
        print('"Debes hacer las cosas que crees que no puedes hacer\n".')


