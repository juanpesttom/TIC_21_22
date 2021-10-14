def tabla_mul_while():
    n = input("Introduce el numero de la tabla: ")
    i = 0
    while (i <= 10):
        print "%d * %d = %d" % (n, i, n*i)
        i+=1
tabla_mul_while()
