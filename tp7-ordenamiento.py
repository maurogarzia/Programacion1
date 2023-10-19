#1_
list_numbers = [8,4,6,0,9,2,1,10]

for i in range (len(list_numbers)):
    exchange = False
    for j in range(0,len(list_numbers) - i - 1):
        if list_numbers[j] > list_numbers[j + 1]:
            list_numbers[j],list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
            exchange = True
    if not exchange:
        break

print(list_numbers)

#------------------------------------------------------------------
#2_

list_words = ["river", "ayer", "adios", "jamas", "pera"]

distance = len(list_words)

for i in range(distance - 1):
    index = i
    
    for j in range(i + 1, distance):
        if list_words[j] < list_words[index]:
            index = j

    list_words[i], list_words[index] = list_words[index], list_words[i]

print( list_words)
#------------------------------------------------------------------
#3_

books = [
    {'titulo': 'Libro A', 'autor': 'Autor 4', 'anio_publicacion': 2003},
    {'titulo': 'Libro B', 'autor': 'Autor 3', 'anio_publicacion': 1990},
    {'titulo': 'Libro C', 'autor': 'Autor 1', 'anio_publicacion': 2010},
    {'titulo': 'Libro D', 'autor': 'Autor 2', 'anio_publicacion': 1832},
]


distance = len(books)

for i in range(distance):
    for j in range(0, distance - i - 1):
        if books[j]['anio_publicacion'] > books[j + 1]['anio_publicacion']:
            books[j], books[j + 1] = books[j + 1], books[j]


print("Lista de libros ordenada por año de publicación:")
for libro in books:
    print(libro)


for i in range(distance):
    for j in range(0, distance - i - 1):
        if books[j]['autor'] > books[j + 1]['autor']:
            books[j], books[j + 1] = books[j + 1], books[j]


print("\nLista de libros ordenada por autor:")
for libro in books:
    print(libro)
#------------------------------------------------------------------
#4_

list_words = ["manzana", "banana", "uva", "naranja", "pera"]

distance = len(list_words)

for i in range(1, distance):
    current_word = list_words[i]
    j = i - 1
    while j >= 0 and len(current_word) < len(list_words[j]):
        list_words[j + 1] = list_words[j]
        j -= 1
    list_words[j + 1] = current_word

print("Lista de cadenas ordenada por longitud:")
for i in list_words:
    print(i)

#------------------------------------------------------------------
#5_

numbers = [33, 105, 25, 175, 2, 69, 1000]

distance = len(numbers)

for i in range(distance):
    for j in range(0, distance - i - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

for i in numbers:
    print(i)
#------------------------------------------------------------------
#6_

numbers = [4, 3, 2, 5, 3, 18, 1]

max = max(numbers)
min = min(numbers)

rango = max - min + 1
counter = [0] * rango

for num in numbers:
    counter[num - min] += 1

ordered_list = []
for i in range(rango):
    ordered_list.extend([i + min] * counter[i])

print("Lista original:", numbers)
print("Lista ordenada por conteo:", ordered_list)
#------------------------------------------------------------------
#7_

lista = [10, "manzana", 5, "Nazareno", "uva", 2, "gaseosa", 8, "pera"]

numbers = [x for x in lista if isinstance(x, (int, float))]
cadenas = [x for x in lista if isinstance(x, str)]

numbers.sort()

cadenas.sort()

lista_ordenada = numbers + cadenas

print( lista_ordenada)
#------------------------------------------------------------------
#8_
def merge_sort(lista):
    if len(lista) > 1:

        mitad = len(lista) // 2
        mitad_izquierda = lista[:mitad]
        mitad_derecha = lista[mitad:]


        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                lista[k] = mitad_izquierda[i]
                i += 1
            else:
                lista[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            lista[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            lista[k] = mitad_derecha[j]
            j += 1
            k += 1

lista_numeros = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", lista_numeros)

merge_sort(lista_numeros)
print("Lista ordenada con Merge Sort:", lista_numeros)


