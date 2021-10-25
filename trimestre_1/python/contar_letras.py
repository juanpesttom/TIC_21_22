def contar_letras():
    palabra = raw_input("Introduce una palabra")
    longitud = len(palabra)
    num_vocales = len([c for c in palabra if c.lower() in 'aeiou'])
    num_consonantes = longitud - num_vocales
    print "Longitud: %d" % (longitud)
    print "Numero vocales: %d" % (num_vocales)
    print "Numero consonantes: %d" % (num_consonantes)
    
contar_letras()
