#1_
corrimiento=int(input("Ingrese de cuantos lugares va a ser el corrimiento: "))
abc="abcdefghijklmnñopqrstuvwxyz"
abcd=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(5):
    frase=input("Ingrese el mensaje deseado: ")
    l=0
    cant=len(frase)
    frase_new=[]
    for z in range(cant):
        letra=frase[l]
        posicion=abc.find(letra)
        letra_new=abc[(posicion+corrimiento)%27]
        if(letra in abcd):
            frase_new.append(letra_new)
        else:
            frase_new.append(letra)
        frase[l]==frase_new[l]
        l=l+1
    print("Mensaje encriptado:","".join(frase_new))
#_________________________________________________________________________
#2-
print("Ingresar numeros enteros positivos")
a=1
pares=0
impares=0
while a!=0:
    a=int(input("Ingrese un numero positivo: "))
    if(a<0):
        print("No es un numero positivo")
    elif(a>0):
        if(a%2==0):
            pares=pares+1
        else:
            impares=impares+1
    else:
        print("HASTA LUEGO")
print(f"La cantidad de numeros pares ingresados es de: {pares}, y de impares: {impares}")