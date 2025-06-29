def evaluar_riesgo_renal(edad, sexo, lista_valores, drangos):
    """
    Evalúa el riesgo renal basado en valores de creatinina sérica.
    
    Args:
        edad (int): Edad del paciente (≥ 0)
        sexo (str): Sexo del paciente ('M' o 'F')
        lista_valores (list): Lista de valores diarios de creatinina
        drangos (dict): Diccionario con rangos normales de creatinina
    
    Returns:
        int: Código de evaluación:
             1 = dentro del rango normal
             2 = por debajo del rango normal
             3 = por encima del rango normal
            -1 = edad inválida
            -2 = sexo inválido
            -3 = menos de 5 valores válidos
    """
    
    # Validación 1: Verificar que edad sea un entero >= 0
    if not isinstance(edad, int) or edad < 0:
        return -1
    
    # Validación 2: Verificar que sexo sea 'M' o 'F'
    if sexo not in ['M', 'F']:
        return -2
    
    # Filtrar valores válidos (float > 0)
    valores_validos = []
    for valor in lista_valores:
        try:
            # Intentar convertir a float
            valor_float = float(valor)
            # Verificar que sea positivo
            if valor_float > 0:
                valores_validos.append(valor_float)
        except (ValueError, TypeError):
            # Ignorar valores que no se pueden convertir a float
            continue
    
    # Validación 3: Verificar que hay al menos 5 valores válidos
    if len(valores_validos) < 5:
        return -3
    
    # Calcular el promedio y redondearlo a 2 decimales
    promedio = round(sum(valores_validos) / len(valores_validos), 2)
    
    # Determinar la clave de edad apropiada
    clave_edad = "<60" if edad < 60 else ">=60"
    
    # Obtener el rango normal para el sexo y edad dados
    rango_normal = drangos[sexo][clave_edad]
    limite_inferior, limite_superior = rango_normal
    
    # Evaluar el riesgo comparando con el rango normal
    if limite_inferior <= promedio <= limite_superior:
        return 1  # Dentro del rango normal
    elif promedio < limite_inferior:
        return 2  # Por debajo del rango normal
    else:
        return 3  # Por encima del rango normal


# Diccionario con los rangos normales de creatinina
dcreatinina_normal = {
    "M": {
        "<60": (0.6, 1.2),
        ">=60": (0.7, 1.3)
    },
    "F": {
        "<60": (0.5, 1.1),
        ">=60": (0.6, 1.2)
    }
}

# Ejemplos de prueba
if __name__ == "__main__":
    # Ejemplo 1: Menos de 5 valores válidos
    resultado1 = evaluar_riesgo_renal(50, 'F', [0.9, -1.0, "x", 1.0, 0.8, 1.0], dcreatinina_normal)
    print(f"Ejemplo 1: {resultado1}")  # Debería ser -3
    
    # Ejemplo 2: Dentro del rango normal
    resultado2 = evaluar_riesgo_renal(63, 'F', [0.9, -1.0, "x", 1.0, 0.8, 1.0, 1.2], dcreatinina_normal)
    print(f"Ejemplo 2: {resultado2}")  # Debería ser 1
    
    # Pruebas adicionales
    
    # Edad inválida
    resultado3 = evaluar_riesgo_renal(-5, 'M', [0.8, 0.9, 1.0, 1.1, 1.2], dcreatinina_normal)
    print(f"Edad inválida: {resultado3}")  # Debería ser -1
    
    # Sexo inválido
    resultado4 = evaluar_riesgo_renal(30, 'X', [0.8, 0.9, 1.0, 1.1, 1.2], dcreatinina_normal)
    print(f"Sexo inválido: {resultado4}")  # Debería ser -2
    
    # Por debajo del rango normal
    resultado5 = evaluar_riesgo_renal(25, 'F', [0.3, 0.4, 0.3, 0.4, 0.4], dcreatinina_normal)
    print(f"Por debajo del rango: {resultado5}")  # Debería ser 2
    
    # Por encima del rango normal
    resultado6 = evaluar_riesgo_renal(40, 'M', [1.5, 1.6, 1.7, 1.8, 1.9], dcreatinina_normal)
    print(f"Por encima del rango: {resultado6}")  # Debería ser 3