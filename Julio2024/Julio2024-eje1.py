"""
Ejercicio 1: Gestión de calificaciones de examen
Este programa gestiona las calificaciones de estudiantes en teoría y prácticas
"""

def obten_notas_teoria(nombre_fichero="notasTeoria.txt"):
    """
    Función que lee las notas de teoría de un fichero y devuelve un diccionario
    con la mejor nota de cada estudiante.
    
    Parámetros:
    -----------
    nombre_fichero : str, opcional
        Nombre del fichero con las notas de teoría. Por defecto "notasTeoria.txt"
        
    Retorna:
    --------
    dict o int
        Diccionario con DNI como clave y mejor nota como valor
        Retorna -1 si el fichero no existe
        
    Funcionamiento:
    --------------
    1. Intenta abrir el fichero especificado
    2. Lee línea por línea
    3. Para cada línea, extrae DNI y notas
    4. Calcula la nota máxima considerando 0 para exámenes no presentados
    5. Almacena en diccionario la mejor nota de cada estudiante
    """
    
    # Diccionario para almacenar los resultados
    # Un diccionario en Python es una estructura de datos que almacena pares clave-valor
    notas_estudiantes = {}
    
    try:
        # open() intenta abrir un fichero. El modo 'r' significa lectura (read)
        # encoding='utf-8' asegura que se lean correctamente caracteres especiales
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            
            # readlines() lee todas las líneas del fichero y las devuelve como lista
            lineas = fichero.readlines()
            
            # Procesamos cada línea del fichero
            # Cada línea representa un estudiante y sus notas
            for linea in lineas:
                # strip() elimina espacios en blanco y saltos de línea al inicio y final
                linea = linea.strip()
                
                # Si la línea está vacía, la saltamos
                if not linea:
                    continue
                
                # split(';') divide la cadena en partes usando ';' como separador
                # Ejemplo: "11111111H;3;7" se convierte en ["11111111H", "3", "7"]
                partes = linea.split(';')
                
                # El DNI es siempre el primer elemento
                dni = partes[0]
                
                # Lista para almacenar las notas del estudiante
                notas = []
                
                # Procesamos las notas (elementos desde el índice 1 en adelante)
                # range(1, len(partes)) genera números desde 1 hasta len(partes)-1
                for i in range(1, len(partes)):
                    nota_str = partes[i]
                    
                    # Si la nota está vacía (estudiante no presentado), asignamos 0
                    if nota_str == '':
                        notas.append(0.0)
                    else:
                        # float() convierte una cadena a número decimal
                        # Usamos float para manejar notas con decimales
                        notas.append(float(nota_str))
                
                # Si faltan notas (menos de 2 exámenes), completamos con ceros
                # Esto maneja el caso donde un estudiante solo tiene una nota
                while len(notas) < 2:
                    notas.append(0.0)
                
                # max() devuelve el valor máximo de una lista
                # Guardamos la mejor nota del estudiante en el diccionario
                notas_estudiantes[dni] = max(notas)
    
    except FileNotFoundError:
        # Esta excepción se lanza cuando el fichero no existe
        # Según el enunciado, debemos devolver -1 en este caso
        return -1
    
    except Exception as e:
        # Capturamos cualquier otro error que pueda ocurrir
        print(f"Error al procesar el fichero: {e}")
        return -1
    
    # Devolvemos el diccionario con las mejores notas
    return notas_estudiantes


def obten_notas_practicas(nombre_fichero="notasPracticas.txt"):
    """
    Función que lee las notas de prácticas de un fichero y devuelve un diccionario
    con la media de las tres mejores notas de cada estudiante.
    
    Parámetros:
    -----------
    nombre_fichero : str, opcional
        Nombre del fichero con las notas de prácticas. Por defecto "notasPracticas.txt"
        
    Retorna:
    --------
    dict o int
        Diccionario con DNI como clave y media de las 3 mejores notas como valor
        Retorna -1 si el fichero no existe
        
    Funcionamiento:
    --------------
    1. Lee el fichero línea por línea
    2. Extrae DNI y todas las notas de prácticas
    3. Ordena las notas de mayor a menor
    4. Toma las 3 mejores (completando con 0 si hay menos de 3)
    5. Calcula la media de estas 3 notas
    """
    
    # Diccionario para almacenar los resultados
    notas_estudiantes = {}
    
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as fichero:
            lineas = fichero.readlines()
            
            # Procesamos cada línea del fichero
            # Cada línea representa un estudiante y sus notas de prácticas
            for linea in lineas:
                linea = linea.strip()
                
                if not linea:
                    continue
                
                # Dividimos la línea por punto y coma
                partes = linea.split(';')
                
                # El DNI es el primer elemento
                dni = partes[0]
                
                # Lista para almacenar todas las notas de prácticas
                notas = []
                
                # Procesamos todas las notas (desde el índice 1)
                for i in range(1, len(partes)):
                    nota_str = partes[i]
                    
                    # Si la nota no está vacía, la añadimos
                    if nota_str != '':
                        notas.append(float(nota_str))
                
                # sorted() ordena una lista. Con reverse=True ordena de mayor a menor
                # [:3] toma los primeros 3 elementos de la lista
                mejores_tres = sorted(notas, reverse=True)[:3]
                
                # Si hay menos de 3 notas, completamos con ceros
                while len(mejores_tres) < 3:
                    mejores_tres.append(0.0)
                
                # sum() suma todos los elementos de una lista
                # len() devuelve el número de elementos
                # Calculamos la media de las 3 mejores notas
                media = sum(mejores_tres) / 3
                
                # Guardamos la media en el diccionario
                notas_estudiantes[dni] = media
    
    except FileNotFoundError:
        return -1
    
    except Exception as e:
        print(f"Error al procesar el fichero: {e}")
        return -1
    
    return notas_estudiantes


# Función adicional para calcular la nota final
def calcular_nota_final(notas_teoria, notas_practicas, peso_teoria=0.6, peso_practicas=0.4):
    """
    Calcula la nota final combinando teoría y prácticas.
    
    Parámetros:
    -----------
    notas_teoria : dict
        Diccionario con las notas de teoría
    notas_practicas : dict
        Diccionario con las notas de prácticas
    peso_teoria : float, opcional
        Peso de la teoría en la nota final (por defecto 60%)
    peso_practicas : float, opcional
        Peso de las prácticas en la nota final (por defecto 40%)
        
    Retorna:
    --------
    dict
        Diccionario con las notas finales de cada estudiante
    """
    
    notas_finales = {}
    
    # set() crea un conjunto (colección sin duplicados)
    # union() combina dos conjuntos
    # Obtenemos todos los DNIs únicos de ambos diccionarios
    todos_los_dnis = set(notas_teoria.keys()).union(set(notas_practicas.keys()))
    
    for dni in todos_los_dnis:
        # get() obtiene un valor del diccionario, devolviendo 0 si la clave no existe
        nota_t = notas_teoria.get(dni, 0)
        nota_p = notas_practicas.get(dni, 0)
        
        # Calculamos la nota final ponderada
        nota_final = nota_t * peso_teoria + nota_p * peso_practicas
        
        # round() redondea un número a n decimales
        notas_finales[dni] = round(nota_final, 2)
    
    return notas_finales


# Código de prueba
if __name__ == "__main__":
    """
    El bloque if __name__ == "__main__": se ejecuta solo cuando el script
    se ejecuta directamente, no cuando se importa como módulo
    """
    
    print("=== GESTIÓN DE CALIFICACIONES ===\n")
    
    # Prueba con el ejemplo del enunciado
    print("1. Probando con el ejemplo del enunciado:")
    
    # Crear fichero de prueba para teoría
    contenido_teoria = """11111111H;3;7
22222222M;;
33333333J;4
44444444K;9;8
55555555L;;6"""
    
    # Escribimos el fichero de prueba
    with open("notasTeoria_prueba.txt", "w", encoding="utf-8") as f:
        f.write(contenido_teoria)
    
    # Probamos la función
    resultado_teoria = obten_notas_teoria("notasTeoria_prueba.txt")
    print(f"Notas de teoría: {resultado_teoria}")
    
    # Crear fichero de prueba para prácticas
    contenido_practicas = """11111111H;3;7;6;7;9
22222222M;4;3"""
    
    with open("notasPracticas_prueba.txt", "w", encoding="utf-8") as f:
        f.write(contenido_practicas)
    
    # Probamos la función de prácticas
    resultado_practicas = obten_notas_practicas("notasPracticas_prueba.txt")
    print(f"\nNotas de prácticas:")
    for dni, nota in resultado_practicas.items():
        print(f"  {dni}: {nota:.2f}")
    
    # Prueba con fichero inexistente
    print("\n2. Probando con fichero inexistente:")
    resultado_error = obten_notas_teoria("fichero_que_no_existe.txt")
    print(f"Resultado con fichero inexistente: {resultado_error}")
    
    # Limpieza: eliminamos los ficheros de prueba
    import os
    try:
        os.remove("notasTeoria_prueba.txt")
        os.remove("notasPracticas_prueba.txt")
    except:
        pass
    
    print("\n=== FIN DE LAS PRUEBAS ===")