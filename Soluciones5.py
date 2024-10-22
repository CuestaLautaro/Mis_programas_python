"""
Definir una función superposicion() que tome dos listas y devuelva 
True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1, lista2):
    """
    Verifica si dos listas tienen al menos un miembro en común.

    Parameters:
        lista1 (list): La primera lista.
        lista2 (list): La segunda lista.

    Returns:
        bool: True si hay al menos un miembro en común, False en caso contrario.
        
    Raises:
        ValueError: Si alguno de los argumentos no es una lista.
    """
    if not isinstance(lista1, list) or not isinstance(lista2, list):
        raise ValueError("Ambos argumentos deben ser listas.")
    
    for miembro1 in lista1:
        for miembro2 in lista2:
            if miembro1 == miembro2:
                return True
    return False

#test
print (superposicion([1, 2, 3], [4, 5, 6]))                 # Debería devolver False
print (superposicion([1, 2, 3], [3, 5, 6]))                 # Debería devolver True
print (superposicion([1, 2, 3], [1, 2, 6]))                 # Debería devolver True
print (superposicion(['a', 'b', 'c'], ['d', 'e', 'f']))     # Debería devolver False
print (superposicion(['a', 'b', 'c'], ['b', 'e', 'f']))     # Debería devolver True
print (superposicion(['a', 'b', 'c'], ['a', 'c', 'f']))     # Debería devolver True    

try:
    print(superposicion("no soy una lista", [1, 2, 3]))     # Debería lanzar ValueError
except ValueError as e:
    print(e)  # Imprimir el mensaje de error