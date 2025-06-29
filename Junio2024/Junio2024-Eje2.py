import re

# Definir las excepciones personalizadas
class ElementoRepetidoError(Exception):
    """Error cuando un elemento aparece más de una vez en la fórmula"""
    pass

class ElementoNoExisteError(Exception):
    """Error cuando un elemento no existe en el diccionario de masas"""
    pass

class FormMonomeroError(Exception):
    """Error cuando la fórmula tiene caracteres inválidos"""
    pass

# Diccionario de masas atómicas (ejemplo con elementos comunes)
dmasas = {
    'H': 1.008,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'S': 32.065,
    'P': 30.974,
    'Cl': 35.453,
    'F': 18.998,
    'Br': 79.904,
    'I': 126.904
}

def parsea_formula_monomero(formula):
    """
    Parsea una fórmula de monómero y devuelve un diccionario con elementos y cantidades.
    
    Args:
        formula (str): Fórmula del monómero (ej: "C2-H4", "H-C-N")
    
    Returns:
        dict: Diccionario con elementos como claves y cantidades como valores
    
    Raises:
        FormMonomeroError: Si la fórmula contiene caracteres inválidos
        ElementoRepetidoError: Si un elemento aparece más de una vez
        ElementoNoExisteError: Si un elemento no existe en el diccionario de masas
    """
    
    # Validar que la fórmula solo contenga caracteres válidos
    # Permitir letras, números y guiones
    # Usamos una expresión regular para validar que la fórmula solo contenga letras, números y guiones
    # La expresión regular r'^[A-Za-z0-9-]+$' asegura que la fórmula solo contenga letras (mayúsculas y minúsculas),
    # números y guiones. No permite espacios ni otros caracteres especiales.
    if not re.match(r'^[A-Za-z0-9-]+$', formula):
        raise FormMonomeroError("La fórmula contiene caracteres inválidos")
    
    # Dividir por guiones para obtener cada parte del elemento
    # Usamos split para separar la fórmula en partes por el guion '-'
    # Esto nos permite manejar fórmulas como "C2-H4" o "H
    partes = formula.split('-')
    
    # Validar que no haya partes vacías
    # Si alguna parte está vacía, significa que hay un guion al inicio o al final
    # o que hay dos guiones seguidos, lo cual no es válido
    # Usamos any() para verificar si alguna parte es una cadena vacía
    # Si alguna parte es vacía, lanzamos una excepción FormMonomeroError
    # indicando que la fórmula tiene un formato inválido
    if any(parte == '' for parte in partes):
        raise FormMonomeroError("La fórmula tiene formato inválido")
    
    resultado = {}
    
    for parte in partes:
        # Usar expresión regular para separar elemento y número
        # La expresión regular r'^([A-Z][a-z]?)(\d*)$' captura:
        # - Un elemento que comienza con una letra mayúscula, opcionalmente seguido de
        #   una letra minúscula (para elementos como 'H', 'He', 'C', 'Cl', etc.)
        # - Un número opcional que sigue al elemento (puede ser vacío, lo que significa 1)
        # Usamos re.match para aplicar la expresión regular a cada parte
        # Si la parte no coincide con el formato esperado, lanzamos una excepción FormMonomeroError
        # indicando que el formato del elemento es inválido
        # La expresión regular también asegura que el elemento no tenga caracteres especiales
        # como puntos, signos de interrogación, etc.
        match = re.match(r'^([A-Z][a-z]?)(\d*)$', parte)
        
        if not match:
            raise FormMonomeroError("Formato de elemento inválido")
        
        # Extraer el elemento y el número de la coincidencia
        # match.group(1) es el elemento (ej: 'C', 'H', 'N')
        # match.group(2) es el número (ej: '2', '4', o una cadena vacía si no hay número)
        # Si el número es una cadena vacía, asumimos que es 1
        elemento = match.group(1)
        # match.group(2) es el número como cadena, puede ser vacío
        # Si es vacío, asumimos que el número es 1
        # Si hay un número, lo convertimos a entero
        numero_str = match.group(2)
        
        # Si no hay número, asumir 1
        # Si el número es una cadena vacía, lo convertimos a 1
        # Si hay un número, lo convertimos a entero
        numero = 1 if numero_str == '' else int(numero_str)
        
        # Verificar que el elemento existe en el diccionario de masas
        if elemento not in dmasas:
            raise ElementoNoExisteError(f"El elemento {elemento} no existe")
        
        # Verificar que el elemento no se repita
        if elemento in resultado:
            raise ElementoRepetidoError(f"El elemento {elemento} aparece más de una vez")
        
        resultado[elemento] = numero
    
    return resultado

def calcula_masa_polimero(dmon, dmasas, num_mon):
    """
    Calcula la masa de un polímero basado en su monómero.
    
    Args:
        dmon (dict): Diccionario del monómero (elemento: cantidad)
        dmasas (dict): Diccionario con masas atómicas
        num_mon (int): Número de monómeros en el polímero
    
    Returns:
        float: Masa del polímero redondeada a 2 decimales, o -1 si num_mon inválido, o 0 si dmon vacío
    """
    
    # Si dmon está vacío, devolver 0
    if not dmon:
        return 0
    
    # Si num_mon no es entero > 0, devolver -1
    if not isinstance(num_mon, int) or num_mon <= 0:
        return -1
    
    # Calcular la masa del monómero
    masa_monomero = 0
    for elemento, cantidad in dmon.items():
        masa_monomero += dmasas[elemento] * cantidad
    
    # Calcular la masa del polímero
    masa_polimero = masa_monomero * num_mon
    
    # Redondear a 2 decimales
    return round(masa_polimero, 2)

# Ejemplos de uso y pruebas
if __name__ == "__main__":
    try:
        # Ejemplo 1: C2-H4 (etileno)
        print("Ejemplo 1: C2-H4")
        monomero1 = parsea_formula_monomero("C2-H4")
        print(f"Monómero parseado: {monomero1}")
        
        # Ejemplo 2: C-H4
        print("\nEjemplo 2: C-H4")
        monomero2 = parsea_formula_monomero("C-H4")
        print(f"Monómero parseado: {monomero2}")
        
        # Ejemplo 3: H-C-N
        print("\nEjemplo 3: H-C-N")
        monomero3 = parsea_formula_monomero("H-C-N")
        print(f"Monómero parseado: {monomero3}")
        
        # Cálculo de masa del polímero (polietileno)
        print("\nCálculo de masa del polímero:")
        masa = calcula_masa_polimero(monomero1, dmasas, 4000)
        print(f"Masa del polímero C2-H4 con 4000 monómeros: {masa}")
        
        # Pruebas de validación
        print("\n--- Pruebas de validación ---")
        
        # Prueba de monómero vacío
        masa_vacia = calcula_masa_polimero({}, dmasas, 100)
        print(f"Monómero vacío: {masa_vacia}")
        
        # Prueba de número inválido
        masa_invalida = calcula_masa_polimero(monomero1, dmasas, -5)
        print(f"Número de monómeros inválido: {masa_invalida}")
        
        # Prueba de número no entero
        masa_no_entero = calcula_masa_polimero(monomero1, dmasas, 3.5)
        print(f"Número no entero: {masa_no_entero}")
        
    except ElementoRepetidoError as e:
        print(f"Error - Elemento repetido: {e}")
    except ElementoNoExisteError as e:
        print(f"Error - Elemento no existe: {e}")
    except FormMonomeroError as e:
        print(f"Error - Formato inválido: {e}")
    
    # Ejemplos de errores
    print("\n--- Ejemplos de errores ---")
    
    try:
        # Error: Elemento repetido
        parsea_formula_monomero("H3-H2")
    except ElementoRepetidoError:
        print("Error capturado: Elemento repetido (H3-H2)")
    
    try:
        # Error: Elemento no existe
        parsea_formula_monomero("Tz5-H3")
    except ElementoNoExisteError:
        print("Error capturado: Elemento no existe (Tz5-H3)")
    
    try:
        # Error: Formato inválido
        parsea_formula_monomero("H2.O")
    except FormMonomeroError:
        print("Error capturado: Formato inválido (H2.O)")
    
    try:
        # Error: Formato inválido con ?
        parsea_formula_monomero("N?H3")
    except FormMonomeroError:
        print("Error capturado: Formato inválido (N?H3)")