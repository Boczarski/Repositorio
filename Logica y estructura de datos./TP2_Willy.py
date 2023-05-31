nombre_archivo = input('Ingrese un nombre de archivo para analizar: ')
sigue = True
try:
    archivo = open(nombre_archivo, 'r')
except FileNotFoundError:

    sigue = False
    print('No se encontro el archivo')
     
if  sigue :
    try:
        contenido = archivo.readlines()
    except:
        cantidad_palabras = 0
        cantidad_de_caracteres = 0
        palabra_maxima = 0

for parrafo in contenido:
    cantidad_de_caracteres = cantidad_de_caracteres + len(parrafo)
    palabras = parrafo.split()
    cantidad_palabras = cantidad_palabras + len(palabras)
    
    for palabra in palabras:
       largo_palabra = len(palabra)
       if largo_palabra > palabra_maxima:
            palabra_maxima = largo_palabra
            palabra_mas_larga = palabra
    print(palabras)
    
    # pausa = input()
print('La palabra mas larga es: ', palabra_mas_larga.upper(), 'y contiene: ', palabra_maxima , 'letras.')
print('la cantidad de palabras son',cantidad_palabras)
print('cantidad de parrafos', len(contenido))
archivo.close