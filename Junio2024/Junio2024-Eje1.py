# DNI: [Tu DNI aquí]
# Nombre: [Tu nombre aquí]

'''Apartado A: Lectura y procesamiento de mutaciones genéticas'''
def get_frec_mutaciones(fich_entrada):
    """
    Lee un archivo de datos genéticos y devuelve un diccionario con la frecuencia 
    de cada mutación.
    
    Args:
        fich_entrada (str): Nombre del archivo de entrada
    
    Returns:
        dict: Diccionario con mutaciones como claves y frecuencias como valores
        -1: Si el archivo no existe
        -2: Si ocurre cualquier otra excepción
    """
    try:
        with open(fich_entrada, 'r', encoding='utf-8') as archivo:
            # Leer todo el contenido del archivo y eliminar espacios en blanco al inicio y al final
            contenido = archivo.read().strip()
            
            # Si el archivo está vacío, devolver diccionario vacío
            if not contenido:
                return {}
            
            frecuencias = {}
            # Dividir el contenido en líneas
            # y procesar cada línea para extraer mutaciones
            lineas = contenido.split('\n')
            
            for linea in lineas:
                # Ignorar líneas vacías
                linea = linea.strip()
                if not linea:
                    continue
                
                # Separar ID del paciente de las mutaciones
                if ':' in linea:
                    # Dividir la línea en ID y mutaciones
                    # Usamos split con maxsplit=91 para evitar dividir mutaciones que contengan ':
                    partes = linea.split(':', 1)
                    # Verificar que hay dos partes (ID y mutaciones)
                    if len(partes) == 2:
                        # Obtener la parte de las mutaciones y eliminar espacios en blanco
                        # y asegurarnos de que no sea una cadena vacía
                        mutaciones_str = partes[1].strip()
                        
                        # Si hay mutaciones, procesarlas                        
                        if mutaciones_str:                             
                            # Dividir las mutaciones por comas  y se convierte cada linea en una lista
                            # de mutaciones                          
                            mutaciones = mutaciones_str.split(',')
                            # Eliminar espacios en blanco alrededor de cada mutación
                            # y asegurarnos de que no haya mutaciones vacías
                            mutaciones = [mutacion.strip() for mutacion in mutaciones]
                            
                            # Contar cada mutación
                            for mutacion in mutaciones:
                                if mutacion:  # Ignorar mutaciones vacías
                                    if mutacion in frecuencias:
                                        frecuencias[mutacion] += 1
                                    else:
                                        frecuencias[mutacion] = 1
            
            return frecuencias
            
    except FileNotFoundError:
        return -1
    except Exception:
        return -2


'''Apartado B: Guardar frecuencias de mutaciones en un archivo'''
def guarda_frec_mutaciones(dic, fich_salida):
    """
    Guarda las frecuencias de mutaciones en un archivo, ordenadas de mayor a menor.
    
    Args:
        dic (dict): Diccionario con frecuencias de mutaciones
        fich_salida (str): Nombre del archivo de salida
    """
    try:
        # Convertir diccionario a lista de tuplas (mutacion, frecuencia)
        # Usamos list(dic.items()) para convertir el diccionario en una lista de tuplas
        # donde cada tupla es (mutacion, frecuencia)
        lista_mutacionesOrdenada = list(dic.items())
        
        # Ordenar la lista de mutaciones por frecuencia (segundo elemento de la tupla)
        # Usamos sort con una función lambda para ordenar por el segundo elemento de la tupla
        # La función lambda x: x[1] indica que queremos ordenar por el segundo elemento de cada tupla
        # y reverse=True para ordenar de mayor a menor
        # Si la lista está vacía, no hay nada que hacer
        lista_mutacionesOrdenada.sort(key=lambda x: x[1], reverse=True)
        
        # Agrupar mutaciones con la misma frecuencia
        frecuencias_agrupadas = {}
        for mutacion, frecuencia in lista_mutacionesOrdenada:
            if frecuencia not in frecuencias_agrupadas:
                # Si la frecuencia no está en el diccionario, inicializamos una lista vacía
                # para almacenar las mutaciones con esa frecuencia
                # Usamos un diccionario para agrupar mutaciones por frecuencia
                # La clave es la frecuencia y el valor es una lista de mutaciones 
                frecuencias_agrupadas[frecuencia] = []
            
            # Añadimos la mutación a la lista correspondiente a su frecuencia
            # Usamos append para añadir la mutación a la lista de mutaciones
            frecuencias_agrupadas[frecuencia].append(mutacion)
        
        # Escribir al archivo
        with open(fich_salida, 'w', encoding='utf-8') as archivo:
            # Ordenar las frecuencias de mayor a menor
            # Usamos sorted para obtener una lista de frecuencias ordenadas
            # sorted devuelve una lista de las claves del diccionario frecuencias_agrupadas
            # y las ordena de mayor a menor
            # reverse=True para ordenar de mayor a menor
            frecuencias_ordenadas = sorted(frecuencias_agrupadas.keys(), reverse=True)
            
            # Escribir cada grupo de mutaciones con su frecuencia
            # Cada línea tendrá el formato: mutacion1,mutacion2,...:frecuencia
            for frecuencia in frecuencias_ordenadas:
                # Obtener las mutaciones para esta frecuencia
                mutaciones = frecuencias_agrupadas[frecuencia]
                # Ordenar las mutaciones alfabéticamente para consistencia
                mutaciones.sort()
                # Crear la línea con las mutaciones y su frecuencia            
                # Formato: mutacion1,mutacion2,...:frecuencia
                # Usamos join para unir las mutaciones con comas
                # y luego añadimos la frecuencia al final con ':'
                linea = ','.join(mutaciones) + ':' + str(frecuencia)
                archivo.write(linea + '\n')
                
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


if __name__ == "__main__":
    # Código de prueba
    
    # Crear archivo de prueba
    contenido_prueba = """
    12345:BRCA1,MDM2,P53
    67890:BRCA1,CDK2
    54321:P53,CDK2,MDM2
    45234:
    98765:BRCA1,P53
    """
    
    with open('datos_geneticos.txt', 'w', encoding='utf-8') as f:
        f.write(contenido_prueba)
    
    # Probar la función get_frec_mutaciones
    resultado = get_frec_mutaciones('datos_geneticos.txt')
    print("Frecuencias de mutaciones:", resultado)
    
    # Probar la función guarda_frec_mutaciones
    # Guardar el resultado en un archivo
    # Usamos el resultado obtenido de get_frec_mutaciones
    # y lo guardamos en un archivo llamado 'reporte_mutaciones.txt'
    # El archivo se creará en el mismo directorio donde se ejecuta el script    
    guarda_frec_mutaciones(resultado, 'reporte_mutaciones.txt')


    # Solo si el resultado es un diccionario válido
    if isinstance(resultado, dict):
        guarda_frec_mutaciones(resultado, 'reporte_mutaciones.txt')
         
        
         
    
    # Probar casos especiales
    print("\nPruebas de casos especiales:")
    
    # Archivo que no existe
    resultado_no_existe = get_frec_mutaciones('archivo_inexistente.txt')
    print("Archivo inexistente:", resultado_no_existe)
    
    # Archivo vacío
    with open('archivo_vacio.txt', 'w') as f:
        pass
    resultado_vacio = get_frec_mutaciones('archivo_vacio.txt')
    print("Archivo vacío:", resultado_vacio)