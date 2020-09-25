import csv

# with cierra el mismo el archivo por eso no se ocupa usar el close. 
with open("maravillas_nuevas.csv") as archivo_entrada:
    lector = csv.reader(archivo_entrada)

    with open("maravillas_nuevas_occidente.csv", "w") as archivo_salida:
        escritor = csv.writer(archivo_salida, delimiter=',')
        i = 0
        for linea in lector:
            if i == 0:
                # Línea del encabezado
                escritor.writerow(linea)
                print(linea)
            elif float(linea[2]) <= 0:
                 # La ubicación es hemisferio occidental
                escritor.writerow(linea)
                print(linea)
            i = i + 1
