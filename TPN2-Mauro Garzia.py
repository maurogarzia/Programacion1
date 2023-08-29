#1_
edad=int(input("Ingresar los años de la computadora: "))
if (edad<=2):
    print("El computador es nuevo")
else:
    print("El computador es viejo")
#-----------------------------------------------
#2_
edad=int(input("Ingresar los años de la computadora: "))
if(edad<0):
    print("Error, la edad no puede ser negativa")
else:
    if (edad<=2):
        print("El computador es nuevo")
    else:
        print("El computador es viejo")
#------------------------------------------------
#3_
nom1=input("Ingrese el nombre la primer personas: ")
nom2=input("Ingrese el nombre de la segunda persona: ")
nom1=nom1.lower()
nom2=nom2.lower()
inicial1=nom1[0]
inicial2=nom2[0]
if(inicial1==inicial1):
    print("coincidencia")
else:
    print("no hay coincidencia")
#--------------------------------------------------
#4_
can_A="Partido Rojo"
can_B="Partido verdad"
can_C="Partido Azul"
print(f"Los candidatos a votar son: Candidato A: {can_A}, Candidato B: {can_B}, Candidato C: {can_C}")
voto=input("Elegir que candidato: ")
voto=voto.lower()
if(voto=="a"):
    print(f"Usted ha votad por el {can_A}")
elif (voto=="b"):
    print(f"Usted ha votado por el {can_B}")
elif (voto=="c"):
    print(f"Usted ha votado por el {can_C}")
elif (voto!="a" or voto!="b" or voto!="c"):
    print("Opcion erronea")
#-----------------------------------------------------
#5_
letra=input("Ingrese una letra: ")
letra=letra.lower()
cont=int(len(letra))
if(cont>1):
    print("No se puede procesar el dato")
else:
    if(letra=='a'or letra=='e' or letra=='i' or letra=='o' or letra=='u'):
        print("Es una vocal")
    else:
        print("No es una vocal")
#-----------------------------------------------------
#6_
anio=int(input("Ingrese un año: "))
if(anio%4==0 and anio%100!=0):
    print("El año es bisiesto")
elif(anio%4==0 and anio%400==0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
#------------------------------------------------------
#7-
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
if (num1<num2 and num1<num3):
    print("El menor es: ",num1)
elif(num2<num1 and num2<num3):
    print("El memor es: ",num2)
else :
    print("El menor es: ",num3)
#-------------------------------------------------------
#8-
nom=input("Ingrese le nombre de usuario: ")
key=input("Ingrese una contraseña: ")
key=key.lower()
nom=nom.title()
if (nom=="Gwenevere" and key=="excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")
#---------------------------------------------------------
#9-(POR TERMINAR)
sexo=input("Ingrese su sexo (hombre o mujer): ")
sexo=sexo.lower()
nom=input("Ingrese su nombre: ")
nom=nom.lower()
inicial=nom[0]
mujer=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
hombre=["n","o","p","q","r","s","t","u","v","w","x","y","z"]

if((sexo=="mujer" and inicial in mujer) or (sexo=="hombre" and inicial in hombre)):
    print("Usted pertenece al grupo A")
else:
    print("Usted pertenece al grupo B")
#---------------------------------------------------------
#10_
edad=int(input("Ingrese su edad: "))
if (edad<4):
    precio_entrada="Gratis"
    print("Precio de entrada: ",precio_entrada)
elif(edad>=4 and edad<=18):
    precio_entrada="500"
    print("Precio de entrada: ",precio_entrada)
else:
    precio_entrada="1000"
    print("Precio de entrada: ",precio_entrada)
#----------------------------------------------------------
#11_
print("Marque la opcion que mas desee: ")
print("(A)_Vegetariana / (B)_No vegetariana")
eleccion=input()
eleccion=eleccion.lower()
if(eleccion=="a"):
    print("Los ingredientes disponibles son (mozzarella y tomate ya incluidos): ")
    print("1)_    .Pimiento")
    print("2)_    .Tofu")
    opcion=int(input("Ingrese que ingrediente quiere agregar(solo un ingrediente): "))
    if(opcion==1):
        print("Pizza elegida: VEGETARIANA")
        print("Ingredientes: Mozzarella, tomate y pimiento")
    elif(opcion==2):
        print("Pizza elegida: VEGETARIANA")
        print("Ingredientes: Mozzarella, tomate y tofu")
    else: 
        print("Opcion invalida")
elif(eleccion=="b"):
    print("Los ingredientes disponibles son (mozzarella y tomate ya incluidos): ")
    print("1)_    .Peperoni")
    print("2)_    .Jamon")
    print("3)_    .Salmon")
    opcion=int(input("Ingrese que ingrediente quiere agregar(solo un ingrediente): "))
    if(opcion==1):
        print("Pizza elegida: NO vegetariana")
        print("Ingredientes: Mozzarella, tomate y peperoni")
    elif(opcion==2):
        print("Pizza elegida: NO vegetariana")
        print("Ingredientes: Mozzarella, tomate y jamon")
    elif(opcion==3):
        print("Pizza elegida: NO vegetariana")
        print("Ingredientes: Mozzarella, tomate y salmon")
    else: 
        print("Opcion invalida")
else:
    print("Tecla ingresada no valida")
#---------------------------------------------------------------
#12_
anio_actual=int(input("Ingrese el año actual: "))
anio_cualquiera=int(input("Ingrese un anio cualquiera: "))
if (anio_actual>anio_cualquiera):
    tiempo=anio_actual-anio_cualquiera
    print(f"Han pasado: {tiempo} años")
elif(anio_actual<anio_cualquiera):
    tiempo=anio_cualquiera-anio_actual
    print(f"Faltan : {tiempo} años")
else:
    print("Ingresaste el mismo año en los dos")
#---------------------------------------------------------------
#13_
n1=int(input("Ingrese el primer numero: "))
n2=int(input("Ingrese el segundo numero: "))
if(n1>n2):
    if(n1%n2==0):
        print("El mayor es multiplo del menor")
    else:
        print("El mayor no es multiplo del menor")
elif(n1<n2):
    if(n2%n1==0):
        print("El mayor es multiplo del menor")
    else:
        print("El mayor no es multiplo del menor")
else:
    print("Los numeros son iguales")

if(n1<0 and n2<0):
    print(f"Los numeros {n1} y {n2} son negativos")
elif(n1<0 and n2>0):
    print(f"El numero {n1} es negativo y el numero {n2} es psotitivo")
elif(n1>0 and n2<0):
    print(f"El numero {n2} es negativo y el numero {n1} es psotitivo")
elif(n1>0 and n2>0):
    print(f"Los numeros {n1} y {n2} son positivos")
elif(n1==0 and n2<0):
        print(f"El numero {n1} es nulo y el numero {n2} es neagtivo")
elif(n1==0 and n2>0):
        print(f"El numero {n1} es nulo y el numero {n2} es positivo")
elif(n1<0 and n2==0):
        print(f"El numero {n2} es nulo y el numero {n1} es neagtivo")
elif(n1>0 and n2==0):
        print(f"El numero {n2} es nulo y el numero {n1} es positivo")
else:
    print("Ambos numeros son negativos")
#-----------------------------------------------------------------
#14_
a=float(input("Ingrese el primer coeficiente: "))
b=float(input("Ingrese el segundo coeficiente: "))
if(a==0 and b!=0):
    print("Sin solucion")
elif(b==0 and a==0):
    print("Tiene infinitas soluciones")
else: 
    formula=-b/a
    print(f"La solucion es: {formula}")
#---------------------------------------------------------------
#15_
print("Para escribir el area de un triangulo presione t/T")
print("Para escribir el area de un circulo presione c/C")
opcion=input("Ingrese area desea saber: ")
opcion=opcion.lower()
if(opcion=="t"):
    base=float(input("Ingrese la base del triangulo: "))
    altura=float(input("Ingrese la altura del triangulo: "))
    area=(base*altura)/2
    print(f"El area del triangulo es de: {area}")
elif(opcion=="c"):
    radio=float(input("Ingrese el radio del circulo: "))
    area=3.1416*(radio)**2
else:
    print("Opcion invalida")
#--------------------------------------------------------------
#16_
print("Operaciones a realizar: ")
print("1)_SUMA")
print("2)_MULTIPLICACION")
print("3)_RESTA")
print("4)_DIVISION")
opcion=int(input("Ingrese el numero de la operacion a realizar: "))
a=float(input("Ingrese el primer valor: "))
b=float(input("Ingrese el segundo valor: "))
if(opcion==1):
    resul=a+b
    print(f"El resultado de la suma es: {resul}")
elif(opcion==2):
    resul=a*b
    print(f"El resultado de la multiplicacion es: {resul}")
elif(opcion==3):
    resul=a-b
    print(f"El resultado de la resta es: {resul}")
elif(opcion==4):
    resul=a/b
    print(f"El resultado de la division es: {resul}")
else:
    print("Tecla ingresada invalida")
#---------------------------------------------------------------
#17_
dia=input("Ingrese un dia de la semana: ")
dia=dia.lower()
if(dia=="lunes"):
    print("ES LUNES?")
elif(dia=="martes"):
    print("ES MARTES?")
elif(dia=="sabado" or dia=="domingo"):
    print("ES FINDE?")
else:
    print("NO SE QUE DIA ES")
#----------------------------------------------------------
#18_
hs=int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salario=float(input("Ingrese su salario por hora: $"))
minimo=48
if(hs>minimo):
    extra_hs=hs-minimo
    mas=salario*(10/100)
    paga=(minimo*salario)+(extra_hs*(salario+mas))
    print(f"Las horas extra trabajadas son: {extra_hs}")
    print(f"El salario total es de: ${paga}")
else:
    print("No se trabajaron horas extra")
    paga=minimo*salario
    print(f"El salario total es de: ${paga}")
#----------------------------------------------------------
#19_
cant=int(input("Cuantos lapices desea comprar?: "))
if(cant>=1000):
    costo=cant*60
    descuento=costo*0.07
    costo_total=costo-descuento
    print(f"Descuento: ${descuento}")
    print("Costo Total: $",costo_total)
else:
    costo_total=cant*60
    print("Costo Total: $",costo_total)
#----------------------------------------------------------
#20_
nota1=float(input("Ingrese la primer nota: "))
nota2=float(input("Ingrese la segunda nota: "))
nota3=float(input("Ingrese la tercer nota: "))
nota4=float(input("Ingrese la cuarta nota: "))
prom=(nota1+nota2+nota3+nota4)/4
if(prom>=6):
    print("APROBADO")
else:
    print("DESPROBADO") 
