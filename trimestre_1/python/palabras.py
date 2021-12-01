def palabra():
    nombre = raw_input("Nombre: ")
    apellido = raw_input("Apellido: ")
    print "Buenos dias %s %s" % (nombre, apellido)
    for i in range(len(nombre)):
        print(nombre[i])
    
def bucles_while():
    n = input("Introduce un numero: ")
    total = 0
    while n != 0:
        total += n
        n = input("Introduce un numero: ")
        
        
palabra()
