"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""
def es_vocal(caracter):
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # Verificar si el input es un solo carácter y es una letra
    if len(caracter) != 1 or not caracter.isalpha():
        return "Error: Ingrese solo una letra, no números ni cadenas"
    
    # Convertir el carácter a minúscula usando lower()
    if caracter.lower() in vocales:
        return True
    else:
        return False

# Bucle que se repite hasta que el usuario escriba "salir"
while True:
    letra = input("Ingrese una letra (o escriba 'salir' para terminar): \n")
    
    # Si el usuario escribe "salir", se rompe el bucle
    if letra.lower() == 'salir':
        print("Programa terminado.")
        break
    
    # Llamar a la función con la variable letra
    print(es_vocal(letra))