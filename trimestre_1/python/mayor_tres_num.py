def mayor_tres(n1, n2, n3):
    if (n2 > n1 and n2 > n3):
        return n2
    elif n3 > n1 and n3 > n2:
        return n3
    return n1

def main():
    print mayor_tres(1,5,3)
main()
