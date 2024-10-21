# Escribir un programa que almacene en una lista los números
# del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.


def test_numeros_invertidos():
    numeros = list(range(1, 11))
    
    assert len(numeros) == 10, "La lista no contiene el número correcto de elementos"
    
    assert numeros == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "La lista no contiene los números esperados"
    
    numeros_invertidos = numeros[::-1]
    
    assert numeros_invertidos == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "La lista no se ha invertido correctamente"
    
    salida_esperada = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"
    salida_real = ", ".join(map(str, numeros_invertidos))
    
    assert salida_real == salida_esperada, "La salida por pantalla no es la esperada"
    
    print("El test ha pasado correctamente.")

test_numeros_invertidos()