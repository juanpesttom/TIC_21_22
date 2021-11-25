def cuadrado_2():
    lenght = input("Introduce la longitud: ")
    l = [[" " for i in range(lenght)] for i in range(lenght)]
    
    n1 = 0
    n2 = lenght-1
    c = '1'
    
    for i in range(lenght):
        for j in range(n1, n2+1):
            l[n1][j] = c
            l[n2][j] = c
            l[j][n1] = c
            l[j][n2] = c
        if c == '1':
            c = '0'
        else:
            c = '1'
        n1 += 1
        n2 -=1

    for i in l:
        for j in i:
            print j,
        print 
def main():
        
    
    
main()
