# Apellidos, Nombre: [Tu nombre aquí]

def calculaPorcentajesGC(nomfich):
    """
    Lee un archivo FASTA y calcula el porcentaje de GC para cada secuencia.
    También crea un archivo de salida con los resultados.
    
    El porcentaje GC es la proporción de nucleótidos G y C en una secuencia de ADN.
    Es una métrica importante porque las regiones con alto contenido GC suelen
    tener propiedades diferentes (más estables, genes más activos, etc.)
    
    Formato FASTA:
    - Las líneas que empiezan con '>' son cabeceras
    - Las siguientes líneas (hasta la próxima cabecera) forman la secuencia
    
    Parámetros:
    - nomfich (str): Nombre del archivo FASTA a procesar
    
    Retorna:
    - list: Lista de porcentajes GC redondeados a 2 decimales
    
    También crea:
    - salida.gc: Archivo con cabeceras y porcentajes GC
    
    Pseudocódigo:
    1. Abrir archivo de entrada y salida
    2. Inicializar variables para almacenar secuencia actual
    3. Para cada línea del archivo:
       - Si es cabecera (empieza con '>'):
         * Procesar secuencia anterior si existe
         * Iniciar nueva secuencia
       - Si no es cabecera:
         * Añadir a la secuencia actual
    4. Procesar la última secuencia
    5. Devolver lista de porcentajes
    """
    
    porcentajes = []  # Lista para almacenar los porcentajes GC
    
    try:
        # Abrir archivos de entrada y salida
        with open(nomfich, 'r') as f_entrada, open('salida.gc', 'w') as f_salida:
            
            cabecera_actual = ""  # Almacena la cabecera actual
            secuencia_actual = ""  # Almacena la secuencia que se está construyendo
            
            # Leer línea por línea
            for linea in f_entrada:
                # No quitamos el \n de la línea para preservar formato en salida
                
                if linea.startswith('>'):
                    # Es una cabecera nueva
                    
                    # Si teníamos una secuencia anterior, procesarla
                    if cabecera_actual and secuencia_actual:
                        # Calcular porcentaje GC
                        porcentaje = calcular_porcentaje_gc(secuencia_actual)
                        porcentajes.append(porcentaje)
                        
                        # Escribir en archivo de salida
                        f_salida.write(cabecera_actual)  # Ya incluye \n
                        f_salida.write(f"{porcentaje}\n")
                    
                    # Guardar nueva cabecera y reiniciar secuencia
                    cabecera_actual = linea
                    secuencia_actual = ""
                    
                else:
                    # Es parte de la secuencia
                    # strip() elimina espacios y saltos de línea
                    secuencia_actual += linea.strip()
            
            # Procesar la última secuencia del archivo
            if cabecera_actual and secuencia_actual:
                porcentaje = calcular_porcentaje_gc(secuencia_actual)
                porcentajes.append(porcentaje)
                f_salida.write(cabecera_actual)
                f_salida.write(f"{porcentaje}\n")
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nomfich}")
        return []
    except Exception as e:
        print(f"Error procesando archivo: {e}")
        return []
    
    return porcentajes


def calcular_porcentaje_gc(secuencia):
    """
    Función auxiliar para calcular el porcentaje de GC en una secuencia.
    
    Parámetros:
    - secuencia (str): Secuencia de ADN
    
    Retorna:
    - float: Porcentaje de GC redondeado a 2 decimales
    """
    if len(secuencia) == 0:
        return 0.0
    
    # Contar G y C (mayúsculas y minúsculas por si acaso)
    num_g = secuencia.upper().count('G')
    num_c = secuencia.upper().count('C')
    
    # Calcular porcentaje
    porcentaje = (num_g + num_c) / len(secuencia)
    
    # Redondear a 2 decimales
    return round(porcentaje, 2)


# Versión alternativa más compacta
def calculaPorcentajesGC_v2(nomfich):
    """
    Versión alternativa usando un enfoque más funcional.
    """
    porcentajes = []
    
    with open(nomfich, 'r') as f_in, open('salida.gc', 'w') as f_out:
        contenido = f_in.read()
        
        # Dividir por cabeceras (cada elemento empieza con >)
        bloques = contenido.split('>')[1:]  # [1:] para saltar el primer elemento vacío
        
        for bloque in bloques:
            lineas = bloque.strip().split('\n')
            cabecera = '>' + lineas[0] + '\n'  # Reconstruir cabecera con >
            secuencia = ''.join(lineas[1:])     # Unir todas las líneas de secuencia
            
            # Calcular porcentaje GC
            gc_count = secuencia.upper().count('G') + secuencia.upper().count('C')
            porcentaje = round(gc_count / len(secuencia), 2) if secuencia else 0.0
            
            porcentajes.append(porcentaje)
            f_out.write(f"{cabecera}{porcentaje}\n")
    
    return porcentajes


if __name__ == "__main__":
    print("=== Prueba de la función calculaPorcentajesGC ===")
    
    # Crear un archivo de prueba
    contenido_prueba = """>chr12_9180206_+:chr12_118582391_+:a1;2 total_counts: 115 Seed: 4 K: 20 length: 79
TTGGTTTCGTGGTTTTGCAAAGTATTGGCCTCCACCGCTATGTCTGGCTGGTTTACGAGC
AGGACAGGCCGCTAAAGTG
>chr12_9180206_+:chr12_118582391_+:a2;2 total_counts: 135 Seed: 4 K: 20 length: 80
CTAACCCGCTACTTCCCAGACAGCTGCTCGTACAGTTTGGGCACATAGTCATCCCACTCG
GCCTGGTAACACGTGCCAGC
>chr1_8969882_-:chr1_568670_-:a1;113 total_counts: 7600 Seed: 225 K: 20 length: 86
CACTCATGAGCTGTCCCCACATTAGGCTTAAAAACAGATGCAATTCCCGGACGTCTAAAC
CAAACCACTTTCACCGCCACACGACC
>chr1_8969882_-:chr1_568670_-:a2;69 total_counts: 6987 Seed: 197 K: 20 length: 120
TGAACCTACGACTACACCGACTACGGCGGACTAATCTTCAACTCCTACATACTTCCCCCA
TTATTCCTAGAACCAGGCGACCTGCGACTCCTTGACGTTGACAATCGAGTAGTACTCCCG"""
    
    # Escribir archivo de prueba
    with open("prueba.fa", "w") as f:
        f.write(contenido_prueba)
    
    # Ejecutar función
    resultado = calculaPorcentajesGC("prueba.fa")
    print(f"Porcentajes GC: {resultado}")
    print("Esperado: [0.52, 0.57, 0.5, 0.51]")
    
    # Mostrar contenido del archivo de salida
    print("\n=== Contenido de salida.gc ===")
    try:
        with open("salida.gc", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No se encontró el archivo salida.gc")
    
    # Verificación adicional
    print("\n=== Verificación de cálculos ===")
    secuencias = [
        "TTGGTTTCGTGGTTTTGCAAAGTATTGGCCTCCACCGCTATGTCTGGCTGGTTTACGAGCAGGACAGGCCGCTAAAGTG",
        "CTAACCCGCTACTTCCCAGACAGCTGCTCGTACAGTTTGGGCACATAGTCATCCCACTCGGCCTGGTAACACGTGCCAGC",
        "CACTCATGAGCTGTCCCCACATTAGGCTTAAAAACAGATGCAATTCCCGGACGTCTAAACCAAACCACTTTCACCGCCACACGACC",
        "TGAACCTACGACTACACCGACTACGGCGGACTAATCTTCAACTCCTACATACTTCCCCCATTATTCCTAGAACCAGGCGACCTGCGACTCCTTGACGTTGACAATCGAGTAGTACTCCCG"
    ]
    
    for i, seq in enumerate(secuencias):
        gc_count = seq.count('G') + seq.count('C')
        total = len(seq)
        porcentaje = round(gc_count / total, 2)
        print(f"Secuencia {i+1}: {gc_count} GC de {total} total = {porcentaje}")