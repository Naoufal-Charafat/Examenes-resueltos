def obten_notas_teoria(nom_fich='notasTeoria.txt'):
    dicNotas = {}

    try:
        with open(nom_fich, 'r') as f:
            lineas = f.readlines()

            for l in lineas:
                partes = l.strip().split(';')
                dni = partes[0]
                notas = partes[1:]

                try:
                    # esto lo hacemos pq notas lo sacamos de un documento entonces es str, y hemos de asegurarnos
                    nota = []
                    for c in notas:
                        if c == '':  # en el condicional es cuando se pone ==
                            notitas = 0
                        else:
                            notitas = float(c)  # que es un valor numerico para poder hacer operaciones con el
                        nota.append(notitas)  # hacemos una lista con los numeros con los qu epodemos trabajar
                except ValueError as e:
                    # PROBLEMA 1: Devolver la excepción es incorrecto
                    # - Debería devolver -1 o manejar el error de otra forma
                    # - 'e' es un objeto Exception, no un entero
                    # - Esto rompe el contrato de la función que dice devolver dict o -1
                    return e

                # PROBLEMA 2: Uso innecesario de bucle manual para encontrar máximo
                # - Python tiene max() que es más eficiente y legible
                # - Este código reinventa la rueda
                best = 0
                for n in nota:  # si n = 3 y best = 0, best pasa a ser 3. Ahora, pasamos a la siguiente nota
                    if n > best:  # que es 7. si 7 es mayor que best = 3, se cambia y best pasa a ser 7, sino
                        best = n  # best seguiria siendo 3, pero no es el caso

                # PROBLEMA 3: Si todas las notas son negativas (aunque improbable en este contexto),
                # best quedaría en 0, lo cual sería incorrecto
                
                dicNotas[dni] = best

        return dicNotas

    except FileNotFoundError:
        return -1

 