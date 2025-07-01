# EJERCICIOS DE DICCIONARIOS Y CADENAS
# Nivel: Básico a Avanzado

# ==============================================================================
# EJERCICIO 1: Contador de Caracteres (Básico)
# ==============================================================================
"""
Crea una función contarCaracteres(texto) que reciba una cadena y devuelva
un diccionario donde las claves sean los caracteres y los valores sean
el número de veces que aparece cada carácter.

Ejemplo:
contarCaracteres("hola mundo") → {'h':1, 'o':2, 'l':1, 'a':1, ' ':1, 'm':1, 'u':1, 'n':1, 'd':1}
"""

def contarCaracteres(texto):
    # Tu código aquí
    pass

# Tests para el ejercicio 1
def test_ejercicio1():
    print("=== EJERCICIO 1: Contador de Caracteres ===")
    print(f"contarCaracteres('hola') = {contarCaracteres('hola')}")
    print(f"contarCaracteres('aaa') = {contarCaracteres('aaa')}")
    print()


# ==============================================================================
# EJERCICIO 2: Comparador de Anagramas (Básico-Medio)
# ==============================================================================
"""
Crea una función sonAnagramas(palabra1, palabra2) que determine si dos palabras
son anagramas (tienen las mismas letras en diferente orden).
Usa un diccionario para contar las letras de cada palabra.
Ignora mayúsculas/minúsculas y espacios.

Ejemplo:
sonAnagramas("Roma", "amor") → True
sonAnagramas("hola", "algo") → False
"""

def sonAnagramas(palabra1, palabra2):
    # Tu código aquí
    pass

# Tests para el ejercicio 2
def test_ejercicio2():
    print("=== EJERCICIO 2: Comparador de Anagramas ===")
    print(f"sonAnagramas('Roma', 'amor') = {sonAnagramas('Roma', 'amor')}")
    print(f"sonAnagramas('listen', 'silent') = {sonAnagramas('listen', 'silent')}")
    print(f"sonAnagramas('hola', 'algo') = {sonAnagramas('hola', 'algo')}")
    print()


# ==============================================================================
# EJERCICIO 3: Traductor de Palabras (Medio)
# ==============================================================================
"""
Crea una función traducirTexto(texto, diccionario_traducciones) que reciba
un texto y un diccionario de traducciones, y devuelva el texto traducido.
Solo traduce palabras completas (no partes de palabras).

Ejemplo:
dic = {"hola": "hello", "mundo": "world", "amigo": "friend"}
traducirTexto("hola mundo amigo", dic) → "hello world friend"
traducirTexto("hola amigos", dic) → "hello amigos"  # 'amigos' no está en el diccionario
"""

def traducirTexto(texto, diccionario_traducciones):
    # Tu código aquí
    pass

# Tests para el ejercicio 3
def test_ejercicio3():
    print("=== EJERCICIO 3: Traductor de Palabras ===")
    dic = {"hola": "hello", "mundo": "world", "amigo": "friend"}
    print(f"traducirTexto('hola mundo', dic) = {traducirTexto('hola mundo', dic)}")
    print(f"traducirTexto('hola amigos', dic) = {traducirTexto('hola amigos', dic)}")
    print()


# ==============================================================================
# EJERCICIO 4: Modificador de Diccionario (Medio)
# ==============================================================================
"""
Crea una función modificarValores(diccionario, operacion) que reciba un
diccionario con valores numéricos y una operación ('duplicar', 'mitad', 'cuadrado').
La función debe modificar todos los valores según la operación.
Debe modificar el diccionario original y también devolverlo.

Ejemplo:
dic = {"a": 10, "b": 20, "c": 30}
modificarValores(dic, "duplicar") → {"a": 20, "b": 40, "c": 60}
"""

def modificarValores(diccionario, operacion):
    # Tu código aquí
    pass

# Tests para el ejercicio 4
def test_ejercicio4():
    print("=== EJERCICIO 4: Modificador de Diccionario ===")
    dic = {"a": 10, "b": 20, "c": 30}
    print(f"Original: {dic}")
    modificarValores(dic, "duplicar")
    print(f"Después de duplicar: {dic}")
    print()


# ==============================================================================
# EJERCICIO 5: Analizador de ADN (Medio-Avanzado)
# ==============================================================================
"""
Crea una función analizarSecuencias(diccionario_secuencias) que reciba un
diccionario donde las claves son nombres de genes y los valores son
secuencias de ADN. La función debe devolver un nuevo diccionario con:
- El porcentaje de cada nucleótido (A, T, C, G)
- La longitud de la secuencia
- Si tiene más de 50% de GC (alto_gc: True/False)

Ejemplo:
dic = {"gen1": "ATCGATCG", "gen2": "GGCCGGCC"}
analizarSecuencias(dic) → {
    "gen1": {"A": 25.0, "T": 25.0, "C": 25.0, "G": 25.0, "longitud": 8, "alto_gc": False},
    "gen2": {"A": 0.0, "T": 0.0, "C": 50.0, "G": 50.0, "longitud": 8, "alto_gc": True}
}
"""

def analizarSecuencias(diccionario_secuencias):
    # Tu código aquí
    pass

# Tests para el ejercicio 5
def test_ejercicio5():
    print("=== EJERCICIO 5: Analizador de ADN ===")
    dic = {"gen1": "ATCGATCG", "gen2": "GGCCGGCC"}
    resultado = analizarSecuencias(dic)
    for gen, analisis in resultado.items():
        print(f"{gen}: {analisis}")
    print()


# ==============================================================================
# EJERCICIO 6: Fusionador de Diccionarios con Conflictos (Avanzado)
# ==============================================================================
"""
Crea una función fusionarDiccionarios(dic1, dic2, estrategia) que fusione
dos diccionarios. Si hay claves duplicadas, usa la estrategia indicada:
- "primero": mantiene el valor del primer diccionario
- "segundo": mantiene el valor del segundo diccionario
- "suma": suma los valores (solo si ambos son numéricos)
- "lista": crea una lista con ambos valores

Ejemplo:
dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"b": 20, "c": 30, "d": 40}
fusionarDiccionarios(dic1, dic2, "suma") → {"a": 1, "b": 22, "c": 33, "d": 40}
"""

def fusionarDiccionarios(dic1, dic2, estrategia):
    # Tu código aquí
    pass

# Tests para el ejercicio 6
def test_ejercicio6():
    print("=== EJERCICIO 6: Fusionador de Diccionarios ===")
    dic1 = {"a": 1, "b": 2, "c": 3}
    dic2 = {"b": 20, "c": 30, "d": 40}
    print(f"dic1: {dic1}")
    print(f"dic2: {dic2}")
    print(f"Fusión con 'suma': {fusionarDiccionarios(dic1, dic2, 'suma')}")
    print(f"Fusión con 'lista': {fusionarDiccionarios(dic1, dic2, 'lista')}")
    print()


# ==============================================================================
# EJERCICIO 7: Procesador de Logs (Avanzado)
# ==============================================================================
"""
Crea una función procesarLogs(lista_logs) que reciba una lista de strings
representando logs con formato: "FECHA HORA NIVEL MENSAJE"
Debe devolver un diccionario con:
- Conteo por nivel (ERROR, WARNING, INFO)
- Lista de mensajes de ERROR
- Hora del primer y último log

Ejemplo:
logs = [
    "2024-01-01 10:00:00 INFO Sistema iniciado",
    "2024-01-01 10:05:00 ERROR Fallo en conexión",
    "2024-01-01 10:10:00 WARNING Memoria baja"
]
procesarLogs(logs) → {
    "conteo": {"INFO": 1, "ERROR": 1, "WARNING": 1},
    "errores": ["Fallo en conexión"],
    "tiempo": {"inicio": "10:00:00", "fin": "10:10:00"}
}
"""

def procesarLogs(lista_logs):
    # Tu código aquí
    pass

# Tests para el ejercicio 7
def test_ejercicio7():
    print("=== EJERCICIO 7: Procesador de Logs ===")
    logs = [
        "2024-01-01 10:00:00 INFO Sistema iniciado",
        "2024-01-01 10:05:00 ERROR Fallo en conexión",
        "2024-01-01 10:10:00 WARNING Memoria baja",
        "2024-01-01 10:15:00 ERROR Disco lleno"
    ]
    resultado = procesarLogs(logs)
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
    print()


# ==============================================================================
# EJERCICIO 8: Validador de Contraseñas con Reglas (Avanzado)
# ==============================================================================
"""
Crea una función validarContraseñas(diccionario_usuarios, reglas) donde:
- diccionario_usuarios: {"usuario": "contraseña"}
- reglas: diccionario con reglas de validación

La función debe devolver un diccionario indicando qué contraseñas son válidas
y por qué fallan las inválidas.

Reglas ejemplo:
{
    "longitud_minima": 8,
    "requiere_mayuscula": True,
    "requiere_numero": True,
    "requiere_especial": True,
    "caracteres_especiales": "!@#$%"
}
"""

def validarContraseñas(diccionario_usuarios, reglas):
    # Tu código aquí
    pass

# Tests para el ejercicio 8
def test_ejercicio8():
    print("=== EJERCICIO 8: Validador de Contraseñas ===")
    usuarios = {
        "juan": "Pass123!",
        "maria": "abc123",
        "pedro": "SuperSecure#2024"
    }
    reglas = {
        "longitud_minima": 8,
        "requiere_mayuscula": True,
        "requiere_numero": True,
        "requiere_especial": True,
        "caracteres_especiales": "!@#$%"
    }
    resultado = validarContraseñas(usuarios, reglas)
    for usuario, validacion in resultado.items():
        print(f"{usuario}: {validacion}")
    print()
 

# ==============================================================================
# EJECUTAR TODOS LOS TESTS
# ==============================================================================
if __name__ == "__main__":
    print("EJERCICIOS DE DICCIONARIOS Y CADENAS\n")
    print("Ejecutando todos los tests:\n")
    
    test_ejercicio1()
    test_ejercicio2()
    test_ejercicio3()
    test_ejercicio4()
    test_ejercicio5()
    test_ejercicio6()
    test_ejercicio7()
    test_ejercicio8()