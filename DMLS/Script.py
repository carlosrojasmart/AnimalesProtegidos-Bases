def depurar_dicc(texto):
    dicc = {
        'á':'a',
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u',
        'Á':'A',
        'É':'E',
        'Í':'I',
        'Ó':'O',
        'Ú':'U',
        'ñ':'ny',
        'Ñ':'NY'
    }

    texto_modificado = ""
    for letra in texto:
        if letra in dicc:
            texto_modificado += dicc[letra]
        else:
            texto_modificado += letra

    return texto_modificado

'''
with open("tipoEcosistema.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "w", encoding='utf-8') as salida, open("DML_proyecto-Sin-T.sql", "a") as salida2:
    for linea in entrada:
        datos = linea.strip().split("    ")
        result = f"INSERT INTO TIPO_ECOSISTEMA(ID, TIPO_ECOSISTEMA) VALUES('{datos[0]}', '{datos[1]}');" + "\n"

        salida.write(result)
        result2 = depurar_dicc(result)
        salida2.write(result2)
    salida.write("\n")


with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("areasProtegidas.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO AREA_PROTEGIDA(ID, NOMBRE, EXTENSION, FECHA_CREACION, UBICACION_LATITUD, UBICACION_LONGITUD, TIPOECOSISTEMA_ID) VALUES('{datos[0]}', '{datos[1]}', {datos[2]}, TO_DATE('{datos[3]}', 'YYYY-MM-DD'), {datos[4]}, {datos[5]}, '{datos[6]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)
            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
        salida.write("\n")
        result2 = depurar_dicc("\n")
'''
with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("indicadorBiodiversidad.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO INDICADOR_BIODIVERSIDAD(ID, NOMBRE, DESCRIPCION) VALUES('{datos[0]}', '{datos[1]}', '{datos[2]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")
'''
with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("registroIndicador.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO REGISTRO_INDICADOR(ID, VALOR_INDICADOR, FECHA_REGISTRO, NOTAS, AREA_PROTEGIDA_ID, INDICADOR_BIODIVERSIDAD_ID) VALUES('{datos[0]}', '{datos[1]}', TO_DATE('{datos[2]}', 'YYYY-MM-DD'), '{datos[3]}', '{datos[4]}', '{datos[5]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")

with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("actividadConservacion.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO ACTIVIDAD_CONSERVACION(ID, NOMBRE, DESCRIPCION, FECHA_REALIZACION, AREA_PROTEGIDA_ID) VALUES('{datos[0]}', '{datos[1]}', '{datos[2]}', TO_DATE('{datos[3]}', 'YYYY-MM-DD'), '{datos[4]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")

with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("amenazaRiesgo.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO AMENAZA_RIESGO(ID, NOMBRE, DESCRIPCION) VALUES('{datos[0]}', '{datos[1]}', '{datos[2]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")

with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("areaAmenazada.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO AREA_AMENAZADA(ID, NOMBRE, DETALLE_AMENAZA, AMENAZA_RIESGO_ID, AREA_PROTEGIDA_ID) VALUES('{datos[0]}', '{datos[1]}', '{datos[2]}', '{datos[3]}', '{datos[4]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")

with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("estadoConservacion.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO ESTADO_CONSERVACION(ID, ESTADO, DESCRIPCION) VALUES('{datos[0]}', '{datos[1]}', '{datos[2]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")


with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("habitat.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO HABITAT(ID, NOMBRE_HABITAT) VALUES('{datos[0]}', '{datos[1]}');" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")

with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("observacion.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = f"INSERT INTO OBSERVACION(ID, FECHA_HORA, NUMERO_INDIVIDUOS, NOTAS, AREA_PROTEGIDA_ID, UBICACION_LATITUD, UBICACION_LONGITUD) VALUES('{datos[0]}', TO_DATE('{datos[1]}', 'YYYY-MM-DD'), {datos[2]}, '{datos[3]}', '{datos[4]}', {datos[5]}, {datos[6]});" + "\n"
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")


with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("especie.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            for i in range(1, 4):  # Aplica depurar_dicc a las columnas que podrían tener tildes
                datos[i] = depurar_dicc(datos[i].replace("'", ""))

            result = f"INSERT INTO ESPECIE(ID, NOMBRE_CIENTIFICO, NOMBRE_COMUN, CARACTERISTICAS_FISICAS, HABITAT_ID, ESTADO_CONSERVACION_ID) VALUES('{datos[0]}', '{datos[1]}', '{datos[2]}', '{datos[3]}', '{datos[4]}', '{datos[5]}');\n"
            salida.write(result)
            salida2.write(result)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")


with open("DML_proyecto-Sin-T.sql", "a") as salida2, open("observacionEspecie.txt", "r", encoding='utf-8') as entrada, open("DML_proyecto2_Final_Esta-Si.sql", "a", encoding='utf-8') as salida:
    num = 0
    for linea in entrada:
        try:
            datos = linea.strip().split("    ")
            result = (f"INSERT INTO OBSERVACION_ESPECIE(ID, CANTIDAD_ESPECIE, OBSERVACION_ID, ESPECIE_ID) VALUES('{datos[0]}', {datos[3]}, '{datos[1]}', '{datos[2]}');" + "\n")
            salida.write(result)
            result2 = depurar_dicc(result)
            salida2.write(result2)

            num += 1
        except IndexError:
            print(f"Error de índice en la línea {num}")
            exit(0)
    salida.write("\n")
    salida2.write("\n")
    '''
