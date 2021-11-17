def main():
    num = input("Dame un numero: ")
    suma = 1
    for cont in range(num, -1, -1):
        print cont, suma
        suma *= cont
    
if __name__ == '__main__':
    main()
