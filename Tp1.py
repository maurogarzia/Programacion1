##FECHA DE EXAMENES
##dia_semana=input("Ingrese el dia de la semana: ")
##dia=input("Ingrese la fecha:" )
##mes=input("Ingrese el mes: ")
fecha= input("Ingrese dia(semanal), dia(dd)/mes(mm)\n")
dia_semana=fecha[0:fecha.find(",")].lower()
dia=int(fecha[fecha.find(" ")+1:fecha.find('/')])
mes=int(fecha[fecha.find("/")+1:])

semana=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
if(dia_semana!=semana[0] and dia_semana!=semana[1] and dia_semana!=semana[2] and dia_semana!=semana[3] and dia_semana!=semana[4] and dia_semana!=semana[5] and dia_semana!=semana[6]):

    print("Error, el dia ingresado es invalido")
elif (dia>31) or (dia<1):
    print("Error, hay un error en la cantidad de dias")
elif (mes>12) or (mes<1):
    print("Error, hay un error en la cantidad de meses")
else:
    if((dia_semana==semana[0]) or (dia_semana==semana[1]) or (dia_semana==semana[2])): ##DIA DE EXAMENES
        resp=input("Se tomaron examenes ese dia?: ").lower()
        if(resp=="si"):
            aprob=int(input("Ingrese la cantidad de alumnos aprobados: "))
            desaprob=int(input("Ingrese la cantidad de alumnos desaprobados: "))
            suma=aprob+desaprob
            porcentaje=(aprob*100)//suma
            print("El porcentaje de aprobados fue de: ",porcentaje,"%")
        else:
            print("No hubo examen")

    elif (dia_semana==semana[3]): ##PRACTICA HABLADA
        asist=int(input("Ingrese el porcentaje de asistencia a clase: "))
        if(asist>50):
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")    
    
    elif(dia_semana==semana[4]): ##INGLES PARA VIAJEROS
        if ((dia==1) and (mes==1 or mes==7)):
            print("Comienzo de nuevo ciclo")
            alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel=int(input("Ingrese la cantidad a abonar por cada alumno: "))
            total=alumnos*arancel
            print("El total a pagar es: $",total)
    elif(dia_semana==semana[5] or dia_semana==semana[6]):
        print("No hay clases el fin de semana")



