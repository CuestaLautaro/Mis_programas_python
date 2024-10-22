"""
Escribir una función sum() y una función multip() 
que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24
"""

def sum(lista):
    """"
    Suma todos los numeros en la lista.
    
    Parameters:
        lista (list): Una lista de numeros.

    Returns:
        int: La suma de los numeros en la lista.
    """""
    if not all(isinstance(num, (int, float)) for num in lista):
        return "Error: La lista debe contener solo numeros."
    
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    """"
    multiplica todos los numeros en la lista.
    
    Parameters:
        lista (list): Una lista de numeros.

    Returns:
        int: La multiplicacion de los numeros en la lista.
    """""
    if not all(isinstance(num, (int, float)) for num in lista):
        return "Error: La lista debe contener solo numeros."
    
    total = 1
    for num in lista:
        total *= num
    return total
#test
print(sum([1, 2, 3, 4]))    # Debería devolver 10
print(multip([1, 2, 3, 4])) # Debería devolver 24