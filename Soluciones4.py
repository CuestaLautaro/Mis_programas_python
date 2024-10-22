"""""
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""""

def es_palindromo(cadena):
    """
    Verifica si una cadena es un palíndromo, permitiendo letras y números.
    
    Parameters:
        cadena (str): La cadena que se desea verificar.

    Returns:
        bool: True si la cadena es un palíndromo, False en caso contrario. Mensaje de error si no se ingresa un dato del tipo string
    """
    if not isinstance(cadena, str):
        return "Error: La entrada debe ser una cadena de texto."
    
    cadena_vacia = ''.join(c for c in cadena.lower() if c.isalnum())

    return cadena_vacia == cadena_vacia[::-1]

#test   
print(es_palindromo("radar"))        # Debería devolver True
print(es_palindromo("hombre"))       # Debería devolver False
print(es_palindromo("hola"))         # Debería devolver False
print(es_palindromo("ama"))          # Debería devolver True
print(es_palindromo(1680))           # Debería devolver Error
print(es_palindromo("12321"))        # Debería devolver True   
print(es_palindromo("1232666"))      # Debería devolver False