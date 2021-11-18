def evau():
    asignatura_1 = raw_input("Introduce la primera carrera: ")
    asignatura_2 = raw_input("Introduce la segunda carrera:
    asignatura_3 = raw_input("Introduce la tercera carrera: ")
    
    print "Notas de la fase obligatoria"
    nota_idioma = input("Ingles/Frances: ")
    nota_lengua = input("Lengua: ")
    nota_historia = input("Historia: ")
    nota_mat_lat = input("Matematicas/Latin: ")
    
    fase_obligatoria = sum(nota_idioma + nota_lengua + nota_historia + nota_mat_lab)/4
    if fase_obligatoria < 4:
        return -1
    nota_bachiller = input("Media de bachiller: ")
    nota_acceso = 0.4 * fase_obligatoria + 0.6 * nota_bachiller
    if nota_acceso < 5:
        return -2
    
    
