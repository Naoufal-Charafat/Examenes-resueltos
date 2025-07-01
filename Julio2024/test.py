# Nombre: [Tu nombre aquí]
# Turno: [Tu turno aquí]

def creaDiccionario(fichero="enzimas.txt"):
    """
    Función que lee un fichero de enzimas y crea un diccionario con la información.
    
    Parámetros:
    - fichero (str): Nombre del fichero a leer (por defecto "enzimas.txt")
    
    Retorna:
    - dict: Diccionario con formato {nombre_enzima: [secuencia, posicion_corte]}
            Si hay lserror, retorna diccionario vacío
    
    Funcionamiento:
    - Lee línea por línea el fichero
    - Cada línea tiene formato: nombre;posicion;secuencia
    - Crea entrada en diccionario para cada enzima válida
    """
    diccionario = {}  # Inicializamos diccionario vacío
    
    try:
        # Intentamos abrir el fichero en modo lectura
        with open(fichero, 'r') as f:
            # Leemos todas las líneas del fichero
            for linea in f:
                # Eliminamos espacios en blanco y saltos de línea al principio y final
                linea = linea.strip()
                
                # Si la línea no está vacía
                if linea:
                    # Dividimos la línea por el separador ';'
                    campos = linea.split(';')
                    
                    # Verificamos que tengamos exactamente 3 campos
                    if len(campos) == 3:
                        nombre = campos[0].strip()  # Nombre de la enzima
                        posicion = int(campos[1].strip())  # Posición de corte (convertir a entero)
                        secuencia = campos[2].strip()  # Secuencia de reconocimiento
                        
                        # Añadimos al diccionario: clave=nombre, valor=[secuencia, posicion]
                        diccionario[nombre] = [secuencia, posicion]
                        
    except (FileNotFoundError, IOError, ValueError):
        # Si hay cualquier error (fichero no existe, error E/S, error conversión), 
        # retornamos diccionario vacío como indica el enunciado
        return {}
    
    return diccionario


def catalizaSecuencia1Corte(nombre_enzima, secuencia, fichero="enzimas.txt"):
    """
    Función que divide una secuencia de ADN según la información de una enzima específica.
    
    Parámetros:
    - nombre_enzima (str): Nombre de la enzima a buscar
    - secuencia (str): Secuencia de ADN a cortar
    - fichero (str): Nombre del fichero de enzimas (por defecto "enzimas.txt")
    
    Retorna:
    - list: Lista con los fragmentos resultantes del corte
            Si no se encuentra enzima o secuencia, retorna lista con secuencia completa
    
    Funcionamiento:
    - Busca la enzima en el fichero usando creaDiccionario
    - Encuentra la secuencia de reconocimiento en el ADN
    - Corta en la posición indicada relativa al inicio de la secuencia encontrada
    """
    # Obtenemos el diccionario de enzimas del fichero
    diccionario = creaDiccionario(fichero)
    
    # Si la enzima no está en el diccionario, devolvemos la secuencia completa
    if nombre_enzima not in diccionario:
        return [secuencia]
    
    # Obtenemos la información de la enzima
    secuencia_reconocimiento = diccionario[nombre_enzima][0]
    posicion_corte = diccionario[nombre_enzima][1]
    
    # Buscamos la secuencia de reconocimiento en la cadena de ADN
    # find() retorna -1 si no encuentra la subcadena
    posicion_encontrada = secuencia.find(secuencia_reconocimiento)
    
    # Si no se encuentra la secuencia de reconocimiento
    if posicion_encontrada == -1:
        return [secuencia]
    
    # Calculamos dónde cortar:
    # posicion_encontrada = inicio de la secuencia de reconocimiento
    # posicion_corte = desplazamiento desde el inicio
    punto_corte = posicion_encontrada + posicion_corte
    
    # Dividimos la secuencia en dos partes
    parte1 = secuencia[:punto_corte]  # Desde el inicio hasta el punto de corte
    parte2 = secuencia[punto_corte:]  # Desde el punto de corte hasta el final
    
    return [parte1, parte2]


def catalizaSecuenciaTodasEnzimas(secuencia, nfs="catalizadoras.txt", nfe="enzimas.txt"):
    """
    Función que encuentra todas las enzimas capaces de cortar una secuencia y
    guarda el resultado en un fichero.
    
    Parámetros:
    - secuencia (str): Secuencia de ADN a analizar
    - nfs (str): Nombre del fichero de salida (por defecto "catalizadoras.txt")
    - nfe (str): Nombre del fichero de entrada con enzimas (por defecto "enzimas.txt")
    
    Funcionamiento:
    - Lee todas las enzimas del fichero de entrada
    - Para cada enzima, intenta cortar la secuencia
    - Si el corte es exitoso (produce 2 fragmentos), guarda el resultado
    - Formato salida: nombre_enzima;fragmento1;fragmento2
    """
    # Obtenemos el diccionario de todas las enzimas
    diccionario = creaDiccionario(nfe)
    
    # Abrimos el fichero de salida para escritura
    with open(nfs, 'w') as f_salida:
        # Iteramos por cada enzima en el diccionario
        for nombre_enzima in diccionario:
            # Intentamos cortar la secuencia con esta enzima
            resultado = catalizaSecuencia1Corte(nombre_enzima, secuencia, nfe)
            
            # Si el resultado tiene 2 elementos, significa que hubo corte exitoso
            if len(resultado) == 2:
                # Escribimos la línea en el formato requerido
                # nombre;fragmento1;fragmento2
                linea = f"{nombre_enzima};{resultado[0]};{resultado[1]}\n"
                f_salida.write(linea)


# Bloque de pruebas
if __name__ == "__main__":
    # Prueba 1: creaDiccionario
    print("=== Prueba creaDiccionario ===")
    dic = creaDiccionario("enzimas.txt")
    print(f"Número de enzimas leídas: {len(dic)}")
    if "EcoRI" in dic:
        print(f"EcoRI: {dic['EcoRI']}")
    
    # Prueba 2: catalizaSecuencia1Corte con EcoRI
    print("\n=== Prueba catalizaSecuencia1Corte - EcoRI ===")
    secADN = "AAAAAAAAAAGAATTCAAAAAAAAAA"
    resultado = catalizaSecuencia1Corte("EcoRI", secADN)
    print(f"Secuencia original: {secADN}")
    print(f"Resultado corte: {resultado}")
    
    # Prueba 3: catalizaSecuencia1Corte con SrfI
    print("\n=== Prueba catalizaSecuencia1Corte - SrfI ===")
    secADN = "AAAAAAAAAAGCCCGGGCAAAAAAAAAA"
    resultado = catalizaSecuencia1Corte("SrfI", secADN)
    print(f"Secuencia original: {secADN}")
    print(f"Resultado corte: {resultado}")
    
    # Prueba 4: catalizaSecuenciaTodasEnzimas
    print("\n=== Prueba catalizaSecuenciaTodasEnzimas ===")
    secADN = "AAAGAATTCGGGTACCGATATCCTCCCGGGGTGGATGGAAAGGGCGAATTCACGT"
    catalizaSecuenciaTodasEnzimas(secADN)
    print("Fichero 'catalizadoras.txt' creado con las enzimas que pueden cortar la secuencia")
    
    # Mostrar primeras líneas del fichero generado
    try:
        with open("catalizadoras.txt", "r") as f:
            print("\nPrimeras 5 líneas del fichero generado:")
            for i, linea in enumerate(f):
                if i < 5:
                    print(linea.strip())
                else:
                    break
    except:
        print("No se pudo leer el fichero de salida")