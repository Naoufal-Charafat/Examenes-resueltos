# Apellidos, Nombre: [Tu nombre aquí]

def dameResiduos(molecula):
    """
    Analiza una cadena en formato PDB y cuenta los átomos por residuo.
    
    En el formato PDB:
    - Las líneas que empiezan con "ATOM" representan átomos
    - Las columnas 18-20 contienen el nombre del residuo (3 letras)
    - Un residuo es un aminoácido en la proteína
    
    Parámetros:
    - molecula (str): Cadena multilínea en formato PDB
    
    Retorna:
    - dict: Diccionario {nombre_residuo: número_de_átomos}
    
    Pseudocódigo:
    1. Inicializar diccionario vacío para contar residuos
    2. Dividir la cadena en líneas
    3. Para cada línea que empiece con "ATOM":
       - Extraer el nombre del residuo (columnas 18-20)
       - Incrementar el contador para ese residuo
    4. Devolver el diccionario
    """
    
    # Paso 1: Inicializar diccionario para contar átomos por residuo
    residuos = {}
    
    # Paso 2: Dividir la cadena en líneas individuales
    lineas = molecula.split('\n')
    
    # Paso 3: Procesar cada línea
    for linea in lineas:
        # Verificar si la línea empieza con "ATOM"
        if linea.startswith("ATOM"):
            # En Python, los índices empiezan en 0, pero el formato PDB
            # describe las posiciones empezando en 1
            # Por tanto: columnas 18-20 del PDB = índices 17-19 en Python
            
            # Extraer el nombre del residuo (3 caracteres)
            # strip() elimina espacios en blanco extras
            nombre_residuo = linea[17:20].strip()
            
            # Si es la primera vez que encontramos este residuo
            if nombre_residuo not in residuos:
                residuos[nombre_residuo] = 0
            
            # Incrementar el contador de átomos para este residuo
            residuos[nombre_residuo] += 1
    
    return residuos


# Versión alternativa usando get() para simplificar
def dameResiduos_v2(molecula):
    """
    Versión alternativa usando el método get() del diccionario.
    """
    residuos = {}
    
    for linea in molecula.split('\n'):
        if linea.startswith("ATOM"):
            nombre_residuo = linea[17:20].strip()
            # get() devuelve el valor si existe, o el valor por defecto (0)
            residuos[nombre_residuo] = residuos.get(nombre_residuo, 0) + 1
    
    return residuos


# Versión usando collections.Counter
def dameResiduos_v3(molecula):
    """
    Versión usando Counter de collections (más pythónica).
    """
    from collections import Counter
    
    # Lista comprehension para extraer todos los nombres de residuos
    residuos = [linea[17:20].strip() 
                for linea in molecula.split('\n') 
                if linea.startswith("ATOM")]
    
    # Counter cuenta automáticamente las ocurrencias
    return dict(Counter(residuos))


# Código de prueba proporcionado
molecula = """
ATOM      1  N   HIS A   1      49.668  24.248  10.436  1.00 25.00           N
ATOM      2  CA  HIS A   1      50.197  25.578  10.784  1.00 16.00           C
ATOM      3  C   HIS A   1      49.169  26.701  10.917  1.00 16.00           C
ATOM      4  O   HIS A   1      48.241  26.524  11.749  1.00 16.00           O
ATOM      5  CB  HIS A   1      51.312  26.048   9.843  1.00 16.00           C
ATOM      6  CG  HIS A   1      50.958  26.068   8.340  1.00 16.00           C
ATOM      7  ND1 HIS A   1      49.636  26.144   7.860  1.00 16.00           N
ATOM      8  CD2 HIS A   1      51.797  26.043   7.286  1.00 16.00           C
ATOM      9  CE1 HIS A   1      49.691  26.152   6.454  1.00 17.00           C
ATOM     10  NE2 HIS A   1      51.046  26.090   6.098  1.00 17.00           N
ATOM     11  N   SER A   2      49.788  27.850  10.784  1.00 16.00           N
ATOM     12  CA  SER A   2      49.138  29.147  10.620  1.00 15.00           C
ATOM     13  C   SER A   2      47.713  29.006  10.110  1.00 15.00           C
ATOM     14  O   SER A   2      46.740  29.251  10.864  1.00 15.00           O
ATOM     15  CB  SER A   2      49.875  29.930   9.569  1.00 16.00           C
ATOM     16  OG  SER A   2      49.145  31.057   9.176  1.00 19.00           O
ATOM     17  N   GLN A   3      47.620  28.367   8.973  1.00 15.00           N
ATOM     18  CA  GLN A   3      46.287  28.193   8.308  1.00 14.00           C
ATOM     19  C   GLN A   3      45.406  27.172   8.963  1.00 14.00           C
"""

if __name__ == "__main__":
    print("=== Prueba de la función dameResiduos ===")
    resultado = dameResiduos(molecula)
    print(f"dameResiduos(molecula) = {resultado}")  # Esperado: {'HIS': 10, 'SER': 6, 'GLN': 3}
    
    # Verificar que todas las versiones dan el mismo resultado
    print("\n=== Verificando versiones alternativas ===")
    print(f"dameResiduos_v2(molecula) = {dameResiduos_v2(molecula)}")
    print(f"dameResiduos_v3(molecula) = {dameResiduos_v3(molecula)}")
    
    # Análisis adicional
    print("\n=== Análisis detallado ===")
    print(f"Total de residuos diferentes: {len(resultado)}")
    print(f"Total de átomos: {sum(resultado.values())}")
    for residuo, num_atomos in resultado.items():
        print(f"  {residuo}: {num_atomos} átomos")