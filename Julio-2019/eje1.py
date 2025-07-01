# Apellidos, Nombre: [Tu nombre aquí]

def dHamming(adn1, adn2, alfabeto="ATCG"):
    """
    Calcula la distancia de Hamming entre dos cadenas de ADN.
    
    La distancia de Hamming es el número de posiciones en las que
    los caracteres correspondientes de dos cadenas son diferentes.
    
    Parámetros:
    - adn1 (str): Primera cadena de ADN
    - adn2 (str): Segunda cadena de ADN
    - alfabeto (str): Caracteres válidos permitidos (por defecto "ATCG")
    
    Retorna:
    - int: Distancia de Hamming si las cadenas son válidas
    - -1: Si las cadenas tienen diferente longitud o contienen caracteres inválidos
    
    Pseudocódigo:
    1. Verificar que ambas cadenas tengan la misma longitud
    2. Verificar que todos los caracteres pertenezcan al alfabeto
    3. Contar las diferencias posición por posición
    """
    
    # Paso 1: Verificar que las cadenas tengan la misma longitud
    if len(adn1) != len(adn2):
        return -1
    
    # Paso 2: Verificar que todos los caracteres de adn1 estén en el alfabeto
    for caracter in adn1:
        if caracter not in alfabeto:
            return -1
    
    # Paso 3: Verificar que todos los caracteres de adn2 estén en el alfabeto
    for caracter in adn2:
        if caracter not in alfabeto:
            return -1
    
    # Paso 4: Calcular la distancia de Hamming
    # Inicializamos contador de diferencias
    distancia = 0
    
    # Comparamos caracter por caracter en la misma posición
    for i in range(len(adn1)):
        if adn1[i] != adn2[i]:
            distancia += 1
    
    return distancia


# Versión alternativa más compacta usando comprensión de listas
def dHamming_v2(adn1, adn2, alfabeto="ATCG"):
    """
    Versión alternativa más pythónica usando comprensión de listas.
    """
    # Verificar longitudes
    if len(adn1) != len(adn2):
        return -1
    
    # Verificar que todos los caracteres están en el alfabeto
    # all() devuelve True si todos los elementos son True
    if not all(c in alfabeto for c in adn1) or not all(c in alfabeto for c in adn2):
        return -1
    
    # Calcular distancia usando comprensión y sum()
    # zip() empareja elementos de ambas cadenas posición por posición
    return sum(1 for c1, c2 in zip(adn1, adn2) if c1 != c2)


if __name__ == "__main__":
    # Casos de prueba proporcionados en el examen
    print("=== Pruebas de la función dHamming ===")
    
    # Caso 1: Cadenas válidas con 1 diferencia
    print(f'dHamming("AAAA","ACAA") = {dHamming("AAAA","ACAA")}')  # Esperado: 1
    
    # Caso 2: Con alfabeto personalizado, 2 diferencias
    print(f'dHamming("abcd","abbb","abcd") = {dHamming("abcd","abbb","abcd")}')  # Esperado: 2
    
    # Caso 3: Caracter 'd' no está en alfabeto por defecto "ATCG"
    print(f'dHamming("abcd","abbb") = {dHamming("abcd","abbb")}')  # Esperado: -1
    
    # Caso 4: Cadenas de diferente longitud
    print(f'dHamming("ACGT","AC") = {dHamming("ACGT","AC")}')  # Esperado: -1
    
    # Caso 5: Cadenas largas
    p = "CCGAAGCAATTGAAACCCCCCCGGCCTGGGAGGCGCAAAAATCTGACCTCTTTGTGAGT"
    q = "GCGTAGTAGGTTCGCGTACCTCGTTCCGGGGAAAACACAAAGGAGAAGGGAATGCTCCT"
    print(f'dHamming(p,q) = {dHamming(p,q)}')  # Esperado: 35
    
    # Prueba adicional: cadenas idénticas
    print(f'\ndHamming("ATCG","ATCG") = {dHamming("ATCG","ATCG")}')  # Esperado: 0
    
    # Comparación con versión alternativa
    print("\n=== Verificando versión alternativa ===")
    print(f'dHamming_v2(p,q) = {dHamming_v2(p,q)}')  # Debe dar 35 también