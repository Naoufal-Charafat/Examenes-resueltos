# Nombre: [Tu nombre aquí]
# Turno: [Tu turno aquí]

def creaDiccionario(fichero="enzimas.txt"):
    """
    Función que lee un fichero de enzimas de restricción y crea un diccionario.
    
    Las enzimas de restricción son proteínas que cortan el ADN en secuencias específicas.
    Son herramientas fundamentales en biología molecular para manipular ADN.
    
    Formato del fichero:
    nombre_enzima;posicion_corte;secuencia_reconocimiento
    
    Parámetros:
    - fichero (str): Ruta del fichero con la información de las enzimas
    
    Retorna:
    - dict: {nombre_enzima: [secuencia_reconocimiento, posicion_corte]}
            Diccionario vacío si hay algún error
    """
    
    # Inicializamos el diccionario que contendrá toda la información
    diccionario_enzimas = {}
    
    try:
        # Abrimos el fichero en modo lectura
        with open(fichero, 'r') as archivo:
            # Procesamos cada línea del fichero
            for linea in archivo:
                # Eliminamos espacios en blanco y saltos de línea
                linea = linea.strip()
                
                # Ignoramos líneas vacías
                if linea:
                    # Dividimos la línea por el separador ';'
                    campos = linea.split(';')
                    
                    # Verificamos que tengamos exactamente 3 campos
                    if len(campos) == 3:
                        # Extraemos y limpiamos cada campo
                        nombre = campos[0].strip()
                        posicion = int(campos[1].strip())  # Convertimos a entero
                        secuencia = campos[2].strip()
                        
                        # Almacenamos en el diccionario
                        # Nota: El orden es [secuencia, posicion] según el enunciado
                        diccionario_enzimas[nombre] = [secuencia, posicion]
    
    except FileNotFoundError:
        # Si el fichero no existe, devolvemos diccionario vacío
        print(f"Error: No se encontró el fichero {fichero}")
        return {}
    except ValueError:
        # Si hay error al convertir la posición a entero
        print("Error: Formato incorrecto en el fichero")
        return {}
    except Exception as e:
        # Cualquier otro error
        print(f"Error inesperado: {e}")
        return {}
    
    return diccionario_enzimas


def catalizaSecuencia1Corte(nombre_enzima, secuencia, fichero="enzimas.txt"):
    """
    Simula el corte de una secuencia de ADN por una enzima de restricción específica.
    
    El corte se realiza en la primera aparición de la secuencia de reconocimiento.
    La posición de corte es relativa al inicio de la secuencia de reconocimiento.
    
    Parámetros:
    - nombre_enzima (str): Nombre de la enzima a utilizar
    - secuencia (str): Secuencia de ADN a cortar
    - fichero (str): Fichero con la información de las enzimas
    
    Retorna:
    - list: Lista con los fragmentos resultantes del corte
            [secuencia_completa] si no se puede realizar el corte
    
    Ejemplo:
    Si la enzima reconoce 'GAATTC' con posición 1:
    - Encuentra 'GAATTC' en la secuencia
    - Corta después del primer nucleótido: G|AATTC
    - Resultado: dos fragmentos
    """
    
    # Obtenemos el diccionario de enzimas
    diccionario = creaDiccionario(fichero)
    
    # Verificamos si la enzima existe en nuestro diccionario
    if nombre_enzima not in diccionario:
        # Si no existe, devolvemos la secuencia sin cortar
        return [secuencia]
    
    # Extraemos la información de la enzima
    secuencia_reconocimiento = diccionario[nombre_enzima][0]
    posicion_corte = diccionario[nombre_enzima][1]
    
    # Buscamos la secuencia de reconocimiento en el ADN
    # find() devuelve la posición de la primera aparición o -1 si no encuentra
    indice_reconocimiento = secuencia.find(secuencia_reconocimiento)
    
    # Si no se encuentra la secuencia de reconocimiento
    if indice_reconocimiento == -1:
        return [secuencia]
    
    # Calculamos el punto exacto de corte
    # indice_reconocimiento: donde empieza la secuencia de reconocimiento
    # posicion_corte: desplazamiento desde el inicio de la secuencia
    punto_corte_real = indice_reconocimiento + posicion_corte
    
    # Dividimos la secuencia en dos fragmentos
    fragmento1 = secuencia[:punto_corte_real]
    fragmento2 = secuencia[punto_corte_real:]
    
    return [fragmento1, fragmento2]


def catalizaSecuenciaTodasEnzimas(secuencia, nfs="catalizadoras.txt", nfe="enzimas.txt"):
    """
    Encuentra todas las enzimas capaces de cortar una secuencia y guarda los resultados.
    
    Esta función es útil para análisis de restricción, donde se quiere saber
    qué enzimas pueden cortar una secuencia específica de ADN.
    
    Parámetros:
    - secuencia (str): Secuencia de ADN a analizar
    - nfs (str): Nombre del fichero de salida
    - nfe (str): Nombre del fichero de entrada con las enzimas
    
    El fichero de salida tendrá el formato:
    nombre_enzima;fragmento1;fragmento2
    
    Solo se incluyen las enzimas que efectivamente cortan la secuencia.
    """
    
    # Obtenemos todas las enzimas disponibles
    diccionario = creaDiccionario(nfe)
    
    # Abrimos el fichero de salida para escritura
    with open(nfs, 'w') as archivo_salida:
        # Probamos cada enzima del diccionario
        for nombre_enzima in diccionario:
            # Intentamos cortar la secuencia con esta enzima
            fragmentos = catalizaSecuencia1Corte(nombre_enzima, secuencia, nfe)
            
            # Si la función devuelve 2 fragmentos, significa que hubo corte
            if len(fragmentos) == 2:
                # Escribimos la línea en el formato especificado
                linea = f"{nombre_enzima};{fragmentos[0]};{fragmentos[1]}\n"
                archivo_salida.write(linea)


# Función auxiliar para visualizar mejor los cortes
def visualizar_corte(nombre_enzima, secuencia, fichero="enzimas.txt"):
    """
    Función auxiliar para visualizar dónde corta una enzima.
    Útil para debugging y comprensión.
    """
    diccionario = creaDiccionario(fichero)
    
    if nombre_enzima in diccionario:
        sec_rec = diccionario[nombre_enzima][0]
        pos = diccionario[nombre_enzima][1]
        
        idx = secuencia.find(sec_rec)
        if idx != -1:
            print(f"\nEnzima: {nombre_enzima}")
            print(f"Reconoce: {sec_rec} en posición {idx}")
            print(f"Corta en posición relativa: {pos}")
            
            # Visualización con marcador de corte
            punto_corte = idx + pos
            visual = secuencia[:punto_corte] + "|" + secuencia[punto_corte:]
            print(f"Secuencia: {visual}")
            print(f"Fragmentos: '{secuencia[:punto_corte]}' y '{secuencia[punto_corte:]}'")


# Bloque de pruebas
if __name__ == "__main__":
    print("=== PRUEBAS DEL EJERCICIO DE ENZIMAS ===\n")
    
    # Crear un fichero de prueba con algunas enzimas
    contenido_enzimas = """EcoRI;1;GAATTC
SrfI;4;GCCCGGGC
BamHI;1;GGATCC
PstI;5;CTGCAG
NotI;2;GCGGCCGC"""
    
    with open("enzimas_prueba.txt", "w") as f:
        f.write(contenido_enzimas)
    
    # Prueba 1: creaDiccionario
    print("1. Prueba creaDiccionario:")
    dic = creaDiccionario("enzimas_prueba.txt")
    print(f"Diccionario creado: {dic}")
    print(f"EcoRI: {dic.get('EcoRI', 'No encontrada')}")
    
    # Prueba 2: catalizaSecuencia1Corte con EcoRI
    print("\n2. Prueba catalizaSecuencia1Corte - EcoRI:")
    secADN1 = "AAAAAAAAAAGAATTCAAAAAAAAAA"
    resultado1 = catalizaSecuencia1Corte("EcoRI", secADN1, "enzimas_prueba.txt")
    print(f"Secuencia: {secADN1}")
    print(f"Resultado: {resultado1}")
    visualizar_corte("EcoRI", secADN1, "enzimas_prueba.txt")
    
    # Prueba 3: catalizaSecuencia1Corte con SrfI
    print("\n3. Prueba catalizaSecuencia1Corte - SrfI:")
    secADN2 = "AAAAAAAAAAGCCCGGGCAAAAAAAAAA"
    resultado2 = catalizaSecuencia1Corte("SrfI", secADN2, "enzimas_prueba.txt")
    print(f"Secuencia: {secADN2}")
    print(f"Resultado: {resultado2}")
    visualizar_corte("SrfI", secADN2, "enzimas_prueba.txt")
    
    # Prueba 4: Enzima no existente
    print("\n4. Prueba con enzima no existente:")
    resultado3 = catalizaSecuencia1Corte("XyzI", secADN1, "enzimas_prueba.txt")
    print(f"Resultado: {resultado3}")
    
    # Prueba 5: catalizaSecuenciaTodasEnzimas
    print("\n5. Prueba catalizaSecuenciaTodasEnzimas:")
    secADN3 = "AAAGAATTCGGGTACCGATATCCTGCAGGGGCCCGGGCGT"
    catalizaSecuenciaTodasEnzimas(secADN3, "salida_prueba.txt", "enzimas_prueba.txt")
    
    print("Contenido del fichero de salida:")
    try:
        with open("salida_prueba.txt", "r") as f:
            contenido = f.read()
            print(contenido if contenido else "  (Ninguna enzima cortó la secuencia)")
    except:
        print("  Error al leer el fichero de salida")