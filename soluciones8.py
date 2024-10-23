"""Desarrolla un programa que genere contraseñas seguras cumpliendo con los estándares de seguridad actuales
(longitud mínima, mezcla de caracteres, números, mayúsculas y símbolos).
Además, permite al usuario definir parámetros personalizados, como longitud de la contraseña y tipos de caracteres a incluir.
"""

import random
import string

def generar_contraseña(longitud=12, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    """
    Genera una contraseña segura.

    Args:
        longitud (int): Longitud deseada de la contraseña (mínimo 8).
        incluir_mayusculas (bool): Indica si se deben incluir letras mayúsculas.
        incluir_numeros (bool): Indica si se deben incluir números.
        incluir_simbolos (bool): Indica si se deben incluir símbolos.

    Returns:
        str: La contraseña generada.

    Raises:
        ValueError: Si la longitud de la contraseña es menor a 8.
    """
    if longitud < 8:
        raise ValueError("La longitud de la contraseña debe ser al menos de 8 caracteres.")
    
    caracteres = [string.ascii_lowercase]

    if incluir_mayusculas:
        caracteres.append(string.ascii_uppercase)
    if incluir_numeros:
        caracteres.append(string.digits)
    if incluir_simbolos:
        caracteres.append(string.punctuation)

    caracteres = ''.join(caracteres)

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

def validar_entrada(mensaje):
    """
    Valida la entrada del usuario para asegurarse de que sea 's' o 'n'.

    Args:
        mensaje (str): Mensaje que se muestra al usuario.

    Returns:
        bool or None: True si la respuesta es 's', False si es 'n', o None si el usuario decide salir.
    """
    while True:
        entrada = input(mensaje).lower()
        if entrada == 'salir':
            return None
        elif entrada in ['s', 'n']:
            return entrada == 's'
        else:
            print("Entrada inválida. Por favor, introduce 's' para sí o 'n' para no.")

def menu_interactivo():
    """
    Muestra un menú interactivo para generar contraseñas.
    Permite al usuario elegir la longitud y los tipos de caracteres para la contraseña.
    """
    while True:
        print("\n--- Generador de contraseñas seguras ---")
        print("Escribe 'salir' en cualquier momento para salir.")
        
        longitud_input = input("Introduce la longitud deseada de la contraseña (mínimo 8): ")
        if longitud_input.lower() == 'salir':
            print("Saliendo del programa...")
            break
        
        try:
            longitud = int(longitud_input)
            if longitud < 8:
                print("La longitud debe ser al menos de 8 caracteres.")
                continue
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        incluir_mayusculas = validar_entrada("¿Incluir mayúsculas? (s/n): ")
        if incluir_mayusculas is None:
            print("Saliendo del programa...")
            break

        incluir_numeros = validar_entrada("¿Incluir números? (s/n): ")
        if incluir_numeros is None:
            print("Saliendo del programa...")
            break

        incluir_simbolos = validar_entrada("¿Incluir símbolos? (s/n): ")
        if incluir_simbolos is None:
            print("Saliendo del programa...")
            break
        
        try:
            contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
            print(f"Contraseña generada: {contraseña}")
        except ValueError as e:
            print(e)

        input("Presiona Enter para continuar...")

# test
menu_interactivo()