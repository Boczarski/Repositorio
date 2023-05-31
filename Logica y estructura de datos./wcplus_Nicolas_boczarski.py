def analizar_archivo(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()

    
    parrafos = texto.split('.\n')

    parrafo_mas_largo = ""
    palabras_mas_larga = ""
    palabras_mas_larga_longitud = 0
    parrafo_mas_largo_palabras = 0
    parrafo_mas_largo_oraciones = 0

    for parrafo in parrafos:
        
        palabras = parrafo.split()
        cantidad_de_palabras = len(palabras)

        oraciones = parrafo.split('.')
        num_oraciones = len(oraciones)

        if cantidad_de_palabras > parrafo_mas_largo_palabras:
            parrafo_mas_largo = parrafo
            parrafo_mas_largo_palabras =cantidad_de_palabras
            parrafo_mas_largo_oraciones = num_oraciones

        for palabra in palabras:
            
            palabra_limpia = palabra.strip('.,!?')

            if len(palabra_limpia) > palabras_mas_larga_longitud:
                palabras_mas_larga = palabra_limpia
                palabras_mas_larga_longitud = len(palabra_limpia)

    print("╔═══════════════╗")
    print('PARRAFO MAS LARGO')
    print("╚═══════════════╝")
    print(parrafo_mas_largo)
    print("-------------------------------------")
    print("La cantidad de palabras del parrafo mas largo son --❯ ",parrafo_mas_largo_palabras )
    print("Cantidad de oraciones en el párrafo más largo --❯ ", parrafo_mas_largo_oraciones)
    print("-------------------------------------")
    print("╔═══════════════╗")
    print('PALABRA MAS LARGA')
    print("╚═══════════════╝")
    print("-------------------------------------")
    print("La palabra más larga es: ", palabras_mas_larga)
    print("La cantidad de letras en la palabra más larga son --❯ ", palabras_mas_larga_longitud)
    print("-------------------------------------")


nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
analizar_archivo(nombre_archivo)


