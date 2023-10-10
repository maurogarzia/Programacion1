#1_
city_list = ['Buenos Aires', 'Nueva York']
lista_pasajeros = []

def add_passenger():
    nombre = input('Ingrese el nombre del pasajero:\n')
    dni = input('Ingrese el DNI del pasajero:\n')
    ciudad_destino = input('Ingrese la ciudad de destino del pasajero:\n')
    pais_destino = input('Ingrese el país de destino del pasajero:\n')
    lista_pasajeros.append((nombre, dni, ciudad_destino, pais_destino))
    city_list.append((ciudad_destino, pais_destino))

def add_city():
    print(city_list)
    ciudad = input('Ingrese la ciudad que desea agregar:\n')
    city_list.append(ciudad)

def find_city_by_dni():
    dni_busqueda = input('Ingrese el DNI que desea buscar para saber a qué ciudad viajará el pasajero:\n')
    for pasajero in lista_pasajeros:
        if dni_busqueda == pasajero[1]:
            print(f'El pasajero viajará a la ciudad de {pasajero[2]}.')
            return
    print('Pasajero no encontrado.')

def count_passengers_by_city():
    count = 0
    ciudad_busqueda = input('Ingrese la ciudad que desea buscar para saber cuántos pasajeros viajarán a ella:\n')
    for pasajero in lista_pasajeros:
        if pasajero[2] == ciudad_busqueda:
            count += 1
    print(f'{count} pasajeros viajarán a {ciudad_busqueda}')

def find_country_by_dni():
    dni_busqueda = input('Ingrese el DNI del pasajero para saber a qué país viajará:\n')
    for pasajero in lista_pasajeros:
        if dni_busqueda == pasajero[1]:
            print(f'El pasajero viajará al país de {pasajero[3]}.')
            return
    print('Pasajero no encontrado.')

def count_passengers_by_country():
    count = 0
    pais_busqueda = input('Ingrese el país que desea buscar para saber cuántos pasajeros viajarán a él:\n')
    for pasajero in lista_pasajeros:
        if pasajero[3] == pais_busqueda:
            count += 1
    print(f'{count} pasajeros viajarán a {pais_busqueda}')

while True:
    
    print("Menu de Opciones:")
    print("1)_ Agregar pasajeros a la lista de viajeros")
    print("2)_ Agregar ciudades a la lista de ciudades")
    print("3)_ Dado el DNI de un pasajero, ver a qué ciudad viaja")
    print("4)_ Dada una ciudad, mostrar la cantidad de pasajeros que viajan a ella")
    print("5)_ Dado el DNI de un pasajero, ver a qué país viaja")
    print("6)_ Dado un país, mostrar cuántos pasajeros viajan a ese país")
    print("7)_ Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        add_passenger()
    elif opcion == '2':
        add_city()
    elif opcion == '3':
        find_city_by_dni()
    elif opcion == '4':
        count_passengers_by_city()
    elif opcion == '5':
        find_country_by_dni()
    elif opcion == '6':
        count_passengers_by_country()
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print('Opción no válida. Por favor, seleccione una opción válida.')
#-------------------------------------------------------------------------------
#2_
def listdomains(billlist):
    domdic={}
    for tuple in billlist:
        domlocal=tuple[3]
        namelocal=tuple[0]
        domdic[namelocal]=domlocal
    return domdic
listcualquiera=[("Naza", 5, 700.50, "Oscarguiñazu 311")]
alldic=listdomains(listcualquiera)
for pasiv in alldic.items():
    print(f"Hay que pagarle a {pasiv}")
#-------------------------------------------------------------------------------
#3_
socios = {
    1: {'nombre': 'Amanda Núñez', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    2: {'nombre': 'Bárbara Molina', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True},
    3: {'nombre': 'Lautaro Campos', 'fecha_ingreso': '17/03/2009', 'cuota_al_dia': True}
}

def cantidad_de_socios(socios):
    return len(socios)

def pagar_cuotas(numero_socio):
    if numero_socio in socios:
        socios[numero_socio]['cuota_al_dia'] = True
        print(f"Socio {numero_socio} ha pagado todas las cuotas adeudadas.")

def modificar_fecha_de_ingreso(fecha_anterior, fecha_nueva):
    for socio in socios.values():
        if socio['fecha_ingreso'] == fecha_anterior:
            socio['fecha_ingreso'] = fecha_nueva

def dar_de_baja(nombre, apellido):
    for numero_socio, socio in socios.items():
        if socio['nombre'] == nombre and socio['apellido'] == apellido:
            del socios[numero_socio]
            print(f"{nombre} {apellido} ha sido dado de baja.")

def listar_socios():
    for numero_socio, socio in socios.items():
        print(f"Socio n°{numero_socio}: {socio['nombre']}, ingresó: {socio['fecha_ingreso']}, cuota al día: {socio['cuota_al_dia']}")

# Ejemplos de uso
print("\nCantidad de socios en el club:", cantidad_de_socios(socios))
pagar_cuotas(2)
modificar_fecha_de_ingreso('17/03/2009', '14/03/2018')
dar_de_baja('Amanda', 'Núñez')
listar_socios()