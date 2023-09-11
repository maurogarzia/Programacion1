#CORRECCIONES DEL TP1.2 
#20-
date=input("Ingrese la fecha de su nacimiento(DDMMAAA): ")
day=int(date[0:2])
print(day)
month=int(date[2:4])
year=int(date[4:])
print(f"La fecha de tu cumpleaños es: {day}/{month}/{year}")

#CORRECCIONES DEL TP2

totals_peers=0
totals_odd=0
loop=1
number=1
while loop!=0:
    print("Ingrese un numero positivo: ")
    print("Para salir pulse 0")
    number=int(input())
    if number==0:
        loop=0
    else:
        pair=0
        odd=0
        while number>0:
            digit=number%10
            if digit%2==0:
                pair+=1
            else:
                odd+=1
            number//=10
        print(f"La cantidad de digitos pares del numero es de: {pair}")
        print(f"La cantidad de digitos impares es de: {odd}")
        totals_odd+=odd
        totals_peers+=pair
print(f"La cantidad total de digitos pares es de {totals_peers}")
print(f"La cantidad total de digitos impares es de: {totals_odd}")