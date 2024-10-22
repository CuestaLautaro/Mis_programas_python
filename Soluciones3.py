"""""
Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""""

def inversa(cadena):
    """
    Invertir una cadena de texto.
    
    Parameters:
        cadena (str): La cadena que se desea invertir.

    Returns:
        str: La cadena invertida o un mensaje de error si la entrada no es válida.
    """
    if not isinstance(cadena, str):
        return "Error: La entrada debe ser una cadena de texto."
    if not cadena.replace(" ", "").isalpha():
        return "Error: La cadena debe contener solo letras."
    return cadena[::-1]

# Test
print(inversa("estoy probando"))  # Debería devolver "odnaborp yotse"
print(inversa("hola"))  # Debería devolver "aloH"