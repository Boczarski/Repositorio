numeros = []
ordinales = ['primer','segundo','tercero','cuarto', 'quinto','sexto']

for iterador in range(6):
    titulo = 'ingrese el  ' + ordinales[iterador] + -'numero: '
    numero = input('Ingrese un número: ')
    
    try:
        numeros.append (float(numero))
    except:
        print('Solo se aceptan numeros , no letras ni caracteres')
        numeros.append(0)

suma = 0
producto = 1
for valor in numeros:
    suma = suma + valor 
    producto = producto * valor


print('#'* 70)
print('el numero mayor es: ', max(numero))
print('el numero menor es : ', min(numeros))
print('la suma de todos los numeros es :', suma)
print('El profucto de todos los numeros es :', producto)
print('#'* 70)
