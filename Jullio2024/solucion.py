# Definición de la excepción personalizada para números repetidos
class NumeroRepe(Exception):
    """Excepción personalizada que se lanza cuando hay números repetidos en una lista"""
    pass


def conjeturaCollatz(n):
    """
    Función que implementa la conjetura de Collatz.
    
    La conjetura de Collatz establece que para cualquier número entero positivo,
    aplicando las siguientes reglas:
    - Si es par: dividir entre 2
    - Si es impar: multiplicar por 3 y sumar 1
    Siempre se llegará al número 1.
    
    Parámetros:
    -----------
    n : int
        Número entero positivo al que aplicar la conjetura
    
    Retorna:
    --------
    int
        Número de operaciones necesarias para llegar a 1, o -1 si n no es válido
    
    Ejemplo:
    --------
    >>> conjeturaCollatz(6)
    8
    """
    # Validación: verificar que n sea un entero positivo
    # isinstance() verifica si n es del tipo int
    # n > 0 verifica que sea positivo
    if not isinstance(n, int) or n <= 0:
        return -1
    
    # Contador de operaciones realizadas
    operaciones = 0
    
    # Mientras n no sea 1, continuamos aplicando las reglas
    while n != 1:
        if n % 2 == 0:  # Si n es par (resto de división entre 2 es 0)
            n = n // 2  # División entera entre 2
        else:  # Si n es impar
            n = n * 3 + 1  # Multiplicar por 3 y sumar 1
        
        operaciones += 1  # Incrementar el contador de operaciones
    
    return operaciones


def es_primo(num):
    """
    Función auxiliar que determina si un número es primo.
    
    Un número primo es aquel que solo es divisible por 1 y por sí mismo.
    Por definición, el 1 NO es primo.
    
    Parámetros:
    -----------
    num : int
        Número a verificar
    
    Retorna:
    --------
    bool
        True si el número es primo, False en caso contrario
    """
    # Los números menores o iguales a 1 no son primos
    if num <= 1:
        return False
    
    # El 2 es el único número primo par
    if num == 2:
        return True
    
    # Los números pares mayores que 2 no son primos
    if num % 2 == 0:
        return False
    
    # Verificar divisibilidad desde 3 hasta la raíz cuadrada de num
    # Solo verificamos números impares (incrementando de 2 en 2)
    # int(num**0.5) calcula la raíz cuadrada y la convierte a entero
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True


def secCollatz(lista):
    """
    Función que aplica la conjetura de Collatz a una lista de números.
    
    Para cada número en la lista, genera:
    1. La secuencia completa de números hasta llegar a 1
    2. El primer número primo en la secuencia (o -1 si no hay)
    3. El número total de operaciones
    
    Parámetros:
    -----------
    lista : list
        Lista de números enteros positivos
    
    Retorna:
    --------
    dict
        Diccionario donde:
        - Claves: números de la lista original
        - Valores: tuplas con (secuencia, primer_primo, num_operaciones)
    
    Lanza:
    ------
    NumeroRepe
        Si hay números repetidos en la lista
    
    Ejemplo:
    --------
    >>> secCollatz([2, 4, 6])
    {2: ([2, 1], 2, 1), 4: ([4, 2, 1], 2, 2), 6: ([6, 3, 10, 5, 16, 8, 4, 2, 1], 3, 8)}
    """
    # Verificar que no haya números repetidos
    # set() crea un conjunto (elimina duplicados)
    # Si el tamaño del conjunto es menor que la lista, hay repetidos
    if len(set(lista)) != len(lista):
        raise NumeroRepe("La lista contiene números repetidos")
    
    # Diccionario para almacenar los resultados
    resultado = {}
    
    # Procesar cada número de la lista
    for numero in lista:
        # Lista para almacenar la secuencia de Collatz
        secuencia = [numero]  # Iniciamos con el número original
        n = numero  # Variable temporal para las operaciones
        
        # Generar la secuencia completa hasta llegar a 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = n * 3 + 1
            secuencia.append(n)  # Agregar cada número a la secuencia
        
        # Buscar el primer número primo en la secuencia
        primer_primo = -1  # Valor por defecto si no hay primos
        for num in secuencia:
            if es_primo(num):
                primer_primo = num
                break  # Salir del bucle al encontrar el primer primo
        
        # Calcular el número de operaciones (longitud de la secuencia - 1)
        # Restamos 1 porque la secuencia incluye el número inicial
        num_operaciones = len(secuencia) - 1
        
        # Almacenar en el diccionario como una tupla
        resultado[numero] = (secuencia, primer_primo, num_operaciones)
    
    return resultado


# Ejemplos de uso y pruebas
if __name__ == "__main__":
    # Prueba de conjeturaCollatz
    print("=== Pruebas de conjeturaCollatz ===")
    print(f"conjeturaCollatz(6) = {conjeturaCollatz(6)}")  # Esperado: 8
    print(f"conjeturaCollatz(1) = {conjeturaCollatz(1)}")  # Esperado: 0
    print(f"conjeturaCollatz(27) = {conjeturaCollatz(27)}")  # Esperado: 111
    print(f"conjeturaCollatz(-5) = {conjeturaCollatz(-5)}")  # Esperado: -1
    print(f"conjeturaCollatz(3.5) = {conjeturaCollatz(3.5)}")  # Esperado: -1
    
    print("\n=== Pruebas de secCollatz ===")
    # Prueba normal
    resultado = secCollatz([2, 4, 6])
    for key, value in resultado.items():
        print(f"{key}: {value}")
    
    # Prueba con un solo número
    print(f"\nsecCollatz([5]) = {secCollatz([5])}")
    
    # Prueba con números repetidos (debe lanzar excepción)
    print("\n=== Prueba con números repetidos ===")
    try:
        secCollatz([2, 4, 2, 6])
    except NumeroRepe as e:
        print(f"Excepción capturada: {e}")