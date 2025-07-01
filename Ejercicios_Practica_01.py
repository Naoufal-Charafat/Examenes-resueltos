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
    contador = {}
    for char in texto:
        contador[char] = contador.get(char, 0) + 1
    return contador

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
    # Limpiar y convertir a minúsculas
    p1 = palabra1.lower().replace(" ", "")
    p2 = palabra2.lower().replace(" ", "")
    
    # Contar caracteres en cada palabra
    return contarCaracteres(p1) == contarCaracteres(p2)

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
    palabras = texto.split()
    traducidas = []
    for palabra in palabras:
        traducidas.append(diccionario_traducciones.get(palabra, palabra))
    return " ".join(traducidas)

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
    for clave in diccionario:
        if operacion == "duplicar":
            diccionario[clave] *= 2
        elif operacion == "mitad":
            diccionario[clave] /= 2
        elif operacion == "cuadrado":
            diccionario[clave] **= 2
    return diccionario

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
    resultado = {}
    for gen, secuencia in diccionario_secuencias.items():
        longitud = len(secuencia)
        conteo = {"A": 0, "T": 0, "C": 0, "G": 0}
        
        for nucleotido in secuencia:
            if nucleotido in conteo:
                conteo[nucleotido] += 1
        
        # Calcular porcentajes
        analisis = {}
        for nuc, cuenta in conteo.items():
            analisis[nuc] = (cuenta / longitud) * 100 if longitud > 0 else 0
        
        analisis["longitud"] = longitud
        analisis["alto_gc"] = (conteo["G"] + conteo["C"]) / longitud > 0.5
        
        resultado[gen] = analisis
    
    return resultado

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
    resultado = dic1.copy()  # Copiar el primer diccionario
    
    for clave, valor in dic2.items():
        if clave in resultado:
            # Hay conflicto, aplicar estrategia
            if estrategia == "primero":
                pass  # Mantener el valor original
            elif estrategia == "segundo":
                resultado[clave] = valor
            elif estrategia == "suma":
                if isinstance(resultado[clave], (int, float)) and isinstance(valor, (int, float)):
                    resultado[clave] += valor
            elif estrategia == "lista":
                resultado[clave] = [resultado[clave], valor]
        else:
            # No hay conflicto, simplemente añadir
            resultado[clave] = valor
    
    return resultado

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
    resultado = {
        "conteo": {"INFO": 0, "ERROR": 0, "WARNING": 0},
        "errores": [],
        "tiempo": {"inicio": "", "fin": ""}
    }
    
    if not lista_logs:
        return resultado
    
    for i, log in enumerate(lista_logs):
        partes = log.split(maxsplit=3)  # Dividir en máximo 4 partes
        if len(partes) >= 4:
            fecha, hora, nivel, mensaje = partes
            
            # Contar niveles
            if nivel in resultado["conteo"]:
                resultado["conteo"][nivel] += 1
            
            # Guardar mensajes de error
            if nivel == "ERROR":
                resultado["errores"].append(mensaje)
            
            # Guardar primera y última hora
            if i == 0:
                resultado["tiempo"]["inicio"] = hora
            resultado["tiempo"]["fin"] = hora
    
    return resultado

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
    resultado = {}
    
    for usuario, contraseña in diccionario_usuarios.items():
        errores = []
        
        # Verificar longitud mínima
        if len(contraseña) < reglas.get("longitud_minima", 0):
            errores.append(f"Longitud menor a {reglas['longitud_minima']}")
        
        # Verificar mayúsculas
        if reglas.get("requiere_mayuscula", False):
            if not any(c.isupper() for c in contraseña):
                errores.append("Falta mayúscula")
        
        # Verificar números
        if reglas.get("requiere_numero", False):
            if not any(c.isdigit() for c in contraseña):
                errores.append("Falta número")
        
        # Verificar caracteres especiales
        if reglas.get("requiere_especial", False):
            especiales = reglas.get("caracteres_especiales", "")
            if not any(c in especiales for c in contraseña):
                errores.append("Falta carácter especial")
        
        # Determinar si es válida
        if errores:
            resultado[usuario] = {"valida": False, "errores": errores}
        else:
            resultado[usuario] = {"valida": True, "errores": []}
    
    return resultado

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