def gauss():
    n = input("Introduce un numero: ")
    for i in range(1, n+1):
        print i
     
def suma_gauss():
    n = input("Introduce un numero: ")
    print sum([i for i in range(1, n+1) if i % 2 != 0])

suma_gauss()
