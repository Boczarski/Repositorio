def encontrar_parrafo_mas_largo(texto):
    parrafos = texto.split("\n") 
    parrafo_mas_largo = max(parrafos, key=len)  
    return parrafo_mas_largo.strip() 
def encontrar_palabra_mas_larga(texto):
    palabras = texto.split()  
    palabra_mas_larga = max(palabras, key=len) 
    return palabra_mas_larga

texto = input("Ingresa un texto: ")
sigue = open(texto)

parrafo_mas_largo = encontrar_parrafo_mas_largo(texto)
print("Párrafo más largo:")
print(parrafo_mas_largo)

palabra_mas_larga = encontrar_palabra_mas_larga(texto)
print("Palabra más larga:")
print(palabra_mas_larga)


# for parrafo in contenido:
#     parrafo_mas_largo = len(contenido)
#     if parrafo_mas_largo > contenido:
#         parrafo_mas_largo = parrafo
#         parrafo_mas_largo = parrafo
#     print(parrafo)
