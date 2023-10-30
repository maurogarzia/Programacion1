#1_
def cant_digits(n,counter):
    if n < 10:
        counter =+ 1
        return counter
    else:
        counter =+ 1
        return cant_digits(n/10,counter) + counter



while True:
    try:
        number = int(input("Ingrese un numero entero: "))
        break
    except ValueError:
        print("Ingrese un numero entero")
print("La cantidad de digitos que tiene el numero es: ",cant_digits(number,0))
#-------------------------------------------------------------------------------------
#2_
def is_power(number_local, exponent):
    if number_local == exponent:
        return True
    elif exponent<number_local:
        return False
    else:
        return is_power(number_local, exponent/number_local)



number=int(input("Ingrese el numero que esta elevando\n"))
number_exponent=int(input("Ingrese el numero que sea saber si es potencia del anterior ingresado\n"))
print("Es potencia" if is_power(number, number_exponent) else "No es potencia")
#-------------------------------------------------------------------------------------------------------
#3_
def how_many_string_in(string_local, sub_string_local, start=0, positions=None):
    if positions is None:
        positions=[]
    index=string_local.find(sub_string_local, start)
    if index !=-1:
        positions.append(index)
        start=index+1
        return how_many_string_in(string_local, sub_string_local, start, positions)
    else:
        return positions



string=input("Ingrese una cadena\n")
sub_string=input("Ingrese una subcadena\n")
print(how_many_string_in(string, sub_string))
#-----------------------------------------------------------------------------------------------------
#4_

def even(number_local):
    if number_local % 2 == 0:
        return "Es par"
    else:
        return odd(number_local)
def odd(number_local):
    if number_local % 2 != 0:
        return "Es impar"
    else:
        return even(number_local)

number=int(input("Ingrese un numero entero\n"))
print(odd(number))


#---------------------------------------------------------------------------------------------------
#5_
def greatest_in_list(number_list_local, counter=0, greatest=0):
    counter=len(number_list_local)-1
    if number_list_local[counter] > greatest and counter != 0:
        greatest=number_list_local[counter]
        counter-=1
        return greatest_in_list(number_list_local, counter, greatest)
    else:
        return greatest

number_list=[1, 4, 6, 8, 11]
print("El mayor de la lista es", greatest_in_list(number_list))


#--------------------------------------------------------------------------------------------------
#6_

def replicate_elems_in_list(list_local, times_to_replicate):
    if not list_local:
        return []
    element = list_local[0] 
    replicated_elements = [element] * times_to_replicate  
    return replicated_elements + replicate_elems_in_list(list_local[1:], times_to_replicate)

list_any = [1, 2, 3]
result = replicate_elems_in_list(list_any, 2)
print(result)
#---------------------------------------------------------------------------------------------
#7_

def calculate_sum(n, p):
    if n == 1:
        return p
    else:
        return n * p + calculate_sum(n - 1, p)
#---------------------------------------------------------------------------------------------

# 8_
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
#---------------------------------------------------------------------------------------------
#9_
def combinations(lst, k, current=""):
    if k == 0:
        print(current)
        return
    for char in lst:
        combinations(lst, k - 1, current + char)
#---------------------------------------------------------------------------------------------

# 10_
def paper_sizes_A(N):
    if N == 0:
        return (841, 1189)  # Measurements of A0 paper
    else:
        previous_width, previous_length = paper_sizes_A(N - 1)
        new_width = previous_length // 2
        new_length = previous_width
        return (new_width, new_length)
