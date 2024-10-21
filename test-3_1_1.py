# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

def test_asignaturas():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    
    assert len(asignaturas) == 5, "La lista no contiene el número correcto de asignaturas"
    
    assert asignaturas == ["Matemáticas", "Física", "Química", "Historia", "Lengua"], "Las asignaturas no coinciden con las esperadas"
    
    salida_esperada = "\n".join(asignaturas)
    salida_real = "\n".join(asignaturas)
    assert salida_real == salida_esperada, "La salida por pantalla no es la esperada"

    print("El test ha pasado correctamente.")
    
test_asignaturas()