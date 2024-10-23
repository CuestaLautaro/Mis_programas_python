"""Definir una función generar_n_caracteres() 
que tome un entero n y devuelva el caracter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    """
    Genera una cadena que contiene el 'caracter' repetido 'n' veces.

    Parameters:
        n (int): Número de veces que se repetirá el carácter.
        caracter (str): El carácter a repetir.

    Returns:
        str: Una cadena con el carácter repetido n veces.
        
    Raises:
        ValueError: Si 'n' no es un entero positivo o si 'caracter' no es de longitud igual a 1.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El numero de repeticiones debe ser un entero positivo. \n")

    if not isinstance(caracter, str) or len(caracter) != 1:
        raise ValueError("El segundo argumento debe ser un caracter de longitud igual a 1. \n")
    
    return caracter * n

# test
print(generar_n_caracteres(5, "x"))  # Debería devolver "xxxxx"
print(generar_n_caracteres(3, "a"))  # Debería devolver "aaa"
print(generar_n_caracteres(0, "z"))  # Debería devolver "" (cadena vacía)

# test de errores
try:
    print(generar_n_caracteres(-2, "x"))  # Debería lanzar ValueError
except ValueError as e:
    print(e)                              # Imprimir el mensaje de error

try:
    print(generar_n_caracteres(5, "xy"))  # Debería lanzar ValueError
except ValueError as e:
    print(e)                              # Imprimir el mensaje de error