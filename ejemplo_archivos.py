# Recorrido e impresión de las líneas de un archivo de texto
with open("maravillas_antiguas.csv", "r") as archivo:
    for linea in archivo:
        # print(linea, end='') #El end quita la línea de por medio. 
	    print(linea)