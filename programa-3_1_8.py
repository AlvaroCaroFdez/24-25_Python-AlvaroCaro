# Escribir un programa que pida al usuario una palabra
# y muestre por pantalla si es un palíndromo.

def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

palabra = input("Introduce una palabra: ")
    
if palindromo(palabra):
    print(palabra, "es un palíndromo.")
else:
    print(palabra, "no es un palíndromo.")