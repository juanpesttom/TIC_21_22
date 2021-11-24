"""
111
101
111

11111
10001
10101
10001
11111

1111111
1000001 
1011101 
1010101 
1011101
1000001
1111111
"""

def swap(c1, c2):
    tmp = c1
    c1 = c2
    c2 = tmp
    
def main():
    lenght = 5
    l = [[" " for i in range(lenght)] for i in range(lenght)]
    
    n1 = 0
    n2 = lenght
    c1 = '1'
    c2 = '0'
    
    for i in range(lenght):
        for j in range(lenght):
            if j > n1 or j < n2:
                l[i][j] = c2
            else:
                l[i][j] = c1
        n1 += 1
        n2 -= 1

    for i in l:
        for j in i:
            print j,
        print 
        
    
    
main()
