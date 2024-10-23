""""Definir un histograma procedimiento() que tome 
una lista de números enteros e imprima un 
Histograma en la pantalla.  Ejemplo: procedimiento([4, 9, 7])
"""

def procedimiento (lista, simbolo='*'):
    """
    Imprime un histograma en la pantalla basado en una lista de números enteros.

    Parameters:
        lista (list): Lista de números enteros.
        simbolo (str): El símbolo a usar en el histograma. Por defecto, es '*'.

    Returns:
        None
        
    Raises:
        ValueError: Si un elemento en la lista no es un número entero positivo.
    """
    for numero in lista:
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("Todos los elementos deben ser números enteros positivos.")
    
    for numero in lista:
        print(f'{numero}: {simbolo * numero}')

# test
procedimiento([4, 9, 7], simbolo='*')        # Usando el símbolo por defecto '*'
procedimiento([6, 7, 2], simbolo='$')        # Usando '$' como símbolo

#test error
try:
    procedimiento([4, -1, 7])                # Debería lanzar un ValueError
except ValueError as e:
    print(e)
    
try:
    procedimiento([4, "texto", 7])           # Debería lanzar un ValueError
except ValueError as e:
    print(e)