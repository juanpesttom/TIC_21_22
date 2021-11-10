def sumar(n1, n2):
    return n1 + n2
    
def restar(n1, n2):
    return n1 - n2
    
def multiplicar(n1, n2):
    return n1 * n2
    
def dividir(n1, n2):
    return n1 / n2
    
def menu():
    print "*" * 10
    print "*"*3 + "MENU" + "*"*3
    print "*"*10
    print """1. SUMAR
    2. RESTAR
    3. MULTIPLICAR
    4. DIVIDIR
"""
    
def main():
    menu()
    n1 = input("Introduce el primer numero: ")
    n2 = input("Introduce el segundo numero: ")
    op = -1
    
    while op < 1 or op > 4:
        op = input("Introduce la opcion: ")
    if op == 1:
        res = sumar(n1, n2)
    elif op == 2:
        res = restar(n1,n2)
    elif op == 3:
        res = multiplicar(n1, n2)
    else:
        if n2 == 0:
            raise ZeroDivisionError
        res = dividir(float(n1),n2)
    print(res)
main()
        
