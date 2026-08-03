import random
ids = []
titulos = []
textos = []
analisis_hexadecimal = []
fechas = []
estados = []
observaciones = []
#-------------------------------------------#
#--|menu_principal_analizador_hexadecimal|--#
#-------------------------------------------#
while True:
    print("menu principal analizador hexadecimal")
    print("1) crear análisis")
    print("2) editar análisis")
    print("3) eliminar análisis")
    print("4) buscar análisis")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_analisis|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_analisis = 1
        else:
            id_analisis = ids[-1] + 1
        titulo = input("título: ")
        texto = input("texto: ")
        fecha = input("fecha: ")
        estado = input("estado (analizado o pendiente): ")
        observacion = input("observación: ")
        resultado = ""
        for caracter in texto:
            resultado += caracter + " = " + format(ord(caracter), "02X") + " "
        ids.append(id_analisis)
        titulos.append(titulo)
        textos.append(texto)
        analisis_hexadecimal.append(resultado)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("análisis registrado correctamente.")
        print("id:", id_analisis)
    #---------------------#
    #--|editar_analisis|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                textos[posicion] = input("nuevo texto: ")
                fechas[posicion] = input("nueva fecha: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                resultado = ""
                for caracter in textos[posicion]:
                    resultado += caracter + " = " + format(ord(caracter), "02X") + " "
                analisis_hexadecimal[posicion] = resultado
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_analisis|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos[i]} | {fechas[i]} | {estados[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {textos[posicion]} | {fechas[posicion]} | {estados[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    textos.pop(posicion)
                    analisis_hexadecimal.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_analisis|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar análisis")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("título:", titulos[posicion])
                print("texto:", textos[posicion])
                print("representación hexadecimal:")
                print(analisis_hexadecimal[posicion])
                print("fecha:", fechas[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            analizados = 0
            pendientes = 0
            total_caracteres = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {textos[i]} | {fechas[i]} | {estados[i]}")
                total_caracteres += len(textos[i])
                if estados[i].lower() == "analizado":
                    analizados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
            print("estadísticas analizador hexadecimal")
            print("cantidad de análisis:", len(ids))
            print("análisis completados:", analizados)
            print("análisis pendientes:", pendientes)
            print("total de caracteres analizados:", total_caracteres)
            posicion = random.randint(0, len(ids) - 1)
            print("análisis seleccionado")
            print("texto:")
            print(textos[posicion])
            print("resultado:")
            print(analisis_hexadecimal[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el analizador hexadecimal.")
        break
    else:
        print("opción no válida.")