# DNI: [Tu DNI aquí]
# Nombre: [Tu nombre aquí]

'''Apartado A: Lectura y procesamiento de pHmetría'''
def leer_phmetria(ruta_fichero: str) -> dict:
    """
    Lee y procesa un fichero de pHmetría de 24 horas.
    
    Args:
        ruta_fichero (str): Ruta completa del fichero de pHmetría
    
    Returns:
        dict: Diccionario con actividades como claves y listas de tuplas (pH, síntomas) como valores
              Diccionario vacío si el fichero no existe
    """
    # Actividades válidas permitidas
    actividades_validas = {'Tumbado', 'De pie', 'Comiendo', 'Durmiendo'}
    
    # Diccionario resultado
    resultado = {}
    
    try:
        with open(ruta_fichero, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                
                # Ignorar líneas vacías
                if not linea:
                    continue
                
                # Dividir por ';'
                campos = linea.split(';')
                
                # Verificar que tenga exactamente 4 campos
                if len(campos) != 4:
                    continue
                
                timestamp, ph_str, actividad, sintomas_str = campos
                
                # Validar y convertir pH
                try:
                    ph = float(ph_str)
                except ValueError:
                    # pH no numérico, ignorar línea
                    continue
                
                # Limpiar y validar actividad
                actividad = actividad.strip()
                if actividad not in actividades_validas:
                    # Actividad no válida, ignorar línea
                    continue
                
                # Procesar síntomas
                sintomas = []
                sintomas_str = sintomas_str.strip()
                if sintomas_str:  # Si hay síntomas
                    # Dividir por comas y limpiar cada síntoma
                    sintomas_raw = sintomas_str.split(',')
                    sintomas = [sintoma.strip() for sintoma in sintomas_raw if sintoma.strip()]
                
                # Agregar al diccionario resultado
                if actividad not in resultado:
                    resultado[actividad] = []
                
                resultado[actividad].append((ph, sintomas))
    
    except FileNotFoundError:
        # Si el fichero no existe, devolver diccionario vacío
        return {}
    
    return resultado



'''Apartado B: Frecuencia de reflujo ácido por actividad'''
def frecuencia_reflujo_por_actividad(datos_ph: dict) -> dict:
    """
    Calcula la frecuencia de reflujo ácido por actividad.
    
    Define reflujo ácido como pH < 4.0.
    Calcula el porcentaje de mediciones con reflujo para cada actividad.
    
    Args:
        datos_ph (dict): Diccionario con actividades como claves y listas de tuplas (pH, síntomas) como valores
    
    Returns:
        dict: Diccionario con actividades como claves y frecuencias de reflujo (%) como valores
              Diccionario vacío si la entrada está vacía
    """
    # Si el diccionario de entrada está vacío, devolver diccionario vacío
    if not datos_ph:
        return {}
    
    resultado = {}
    
    # Procesar cada actividad
    for actividad, mediciones in datos_ph.items():
        total_mediciones = len(mediciones)
        
        # Contar mediciones con reflujo ácido (pH < 4.0)
        mediciones_reflujo = 0
        for ph, sintomas in mediciones:
            if ph < 4.0:
                mediciones_reflujo += 1
        
        # Calcular frecuencia como porcentaje
        if total_mediciones > 0:
            frecuencia = (mediciones_reflujo / total_mediciones) * 100
            # Redondear a 2 decimales
            frecuencia = round(frecuencia, 2)
        else:
            frecuencia = 0.0
        
        resultado[actividad] = frecuencia
    
    return resultado




'''Pruebas de las funciones'''
if __name__ == "__main__":
    # Código de prueba
    
    # Crear archivo de prueba con el ejemplo del enunciado
    contenido_prueba = '''
    \"00:00\";7.0;Tumbado;
    \"00:05\";6.7;De pie;
    \"00:10\";--;De pie;Tos
    \"00:15\";7;Comiendo;Acidez
    \"00:20\";3.5;Tumbado;Acidez,Tos
    \"00:25\";6.0;Tumbado;
    \"00:30\";3.8;Comiendo;
    '''
    
    with open('phm_ejemplo.txt', 'w', encoding='utf-8') as f:
        f.write(contenido_prueba)
    
    # Probar la función
    resultado = leer_phmetria('phm_ejemplo.txt')
    print("Resultado del análisis de pHmetría:")
    for actividad, mediciones in resultado.items():
        print(f"{actividad}: {mediciones}")
    
    print("\nResultado esperado:")
    print("Tumbado: [(7.0, []), (3.5, ['Acidez', 'Tos']), (6.0, [])]")
    print("De pie: [(6.7, [])]")
    print("Comiendo: [(7.0, ['Acidez']), (3.8, [])]")
    
    # Probar casos especiales
    print("\n--- Pruebas de casos especiales ---")
    
    # Archivo inexistente
    resultado_inexistente = leer_phmetria('archivo_inexistente.txt')
    print(f"Archivo inexistente: {resultado_inexistente}")
    
    # Crear archivo con diversos errores para probar la robustez
    contenido_errores = '''\"00:00\";7.0;Tumbado;
\"00:05\";abc;De pie;Tos
\"00:10\";6.5;ActividadInvalida;
\"00:15\";7.2;Comiendo;Acidez;ExtraCampo
\"00:20\";5.5;Durmiendo;Disfagia,Odinofagia
\"00:25\"
\"00:30\";6.8;De pie;   Tos   ,   Acidez   '''
    
    with open('phm_errores.txt', 'w', encoding='utf-8') as f:
        f.write(contenido_errores)
    
    resultado_errores = leer_phmetria('phm_errores.txt')
    print(f"\nArchivo con errores procesado:")
    for actividad, mediciones in resultado_errores.items():
        print(f"{actividad}: {mediciones}")
    
    # Archivo vacío
    with open('phm_vacio.txt', 'w', encoding='utf-8') as f:
        pass
    
    resultado_vacio = leer_phmetria('phm_vacio.txt')
    print(f"\nArchivo vacío: {resultado_vacio}")
    
    # Verificar que el resultado coincide con el ejemplo esperado
    resultado_esperado = {
        'Tumbado': [(7.0, []), (3.5, ['Acidez', 'Tos']), (6.0, [])],
        'De pie': [(6.7, [])],
        'Comiendo': [(7.0, ['Acidez']), (3.8, [])]
    }
    
    print(f"\n¿El resultado coincide con el esperado? {resultado == resultado_esperado}")
    
    # --- PRUEBAS DE LA PARTE B ---
    print("\n" + "="*50)
    print("PRUEBAS DE LA PARTE B - Frecuencia de Reflujo")
    print("="*50)
    
    # Probar con el resultado del ejemplo
    frecuencias = frecuencia_reflujo_por_actividad(resultado)
    print(f"Frecuencias de reflujo calculadas: {frecuencias}")
    
    # Resultado esperado según el enunciado
    frecuencias_esperadas = {'Tumbado': 33.33, 'De pie': 0.0, 'Comiendo': 50.0}
    print(f"Frecuencias esperadas: {frecuencias_esperadas}")
    
    # Verificar cálculos manualmente
    print("\nVerificación manual de cálculos:")
    print("Tumbado: [(7.0, []), (3.5, ['Acidez', 'Tos']), (6.0, [])]")
    print("  - Total mediciones: 3")
    print("  - Mediciones con pH < 4.0: 1 (pH=3.5)")
    print("  - Frecuencia: (1/3) * 100 = 33.33%")
    
    print("\nDe pie: [(6.7, [])]")
    print("  - Total mediciones: 1")
    print("  - Mediciones con pH < 4.0: 0")
    print("  - Frecuencia: (0/1) * 100 = 0.0%")
    
    print("\nComiendo: [(7.0, ['Acidez']), (3.8, [])]")
    print("  - Total mediciones: 2")
    print("  - Mediciones con pH < 4.0: 1 (pH=3.8)")
    print("  - Frecuencia: (1/2) * 100 = 50.0%")
    
    print(f"\n¿Las frecuencias coinciden? {frecuencias == frecuencias_esperadas}")
    
    # Casos especiales para la parte B
    print("\n--- Casos especiales Parte B ---")
    
    # Diccionario vacío
    frecuencias_vacio = frecuencia_reflujo_por_actividad({})
    print(f"Diccionario vacío: {frecuencias_vacio}")
    
    # Todas las mediciones con reflujo
    datos_todo_reflujo = {
        'Tumbado': [(2.5, ['Acidez']), (3.9, ['Tos']), (1.5, [])],
        'De pie': [(3.2, ['Acidez', 'Tos'])]
    }
    frecuencias_todo_reflujo = frecuencia_reflujo_por_actividad(datos_todo_reflujo)
    print(f"Todas con reflujo: {frecuencias_todo_reflujo}")
    
    # Ninguna medición con reflujo
    datos_sin_reflujo = {
        'Durmiendo': [(7.2, []), (6.8, ['Tos']), (5.5, [])],
        'Comiendo': [(4.5, ['Acidez'])]
    }
    frecuencias_sin_reflujo = frecuencia_reflujo_por_actividad(datos_sin_reflujo)
    print(f"Ninguna con reflujo: {frecuencias_sin_reflujo}")
    
    # Caso límite pH = 4.0 (no debe contar como reflujo)
    datos_limite = {
        'Tumbado': [(4.0, []), (3.99, ['Acidez']), (4.01, [])]
    }
    frecuencias_limite = frecuencia_reflujo_por_actividad(datos_limite)
    print(f"Caso límite pH=4.0: {frecuencias_limite}")
    print("  - pH=4.0 NO cuenta como reflujo (debe ser < 4.0)")
    print("  - pH=3.99 SÍ cuenta como reflujo")
    print("  - Frecuencia esperada: (1/3) * 100 = 33.33%")