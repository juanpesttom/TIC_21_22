import random

def dado():
    return random.randint(1, 6)
    
def dados():
    """Introduzca el nombre de los jugadores
    Turno 1
    Jugador 1
    Tirada 1 = 6
    
    Jugador 2
    Tirada 1 = 3
    [...]
    Puntos jugador 1 = 
    Puntos jugador 2 =
    Ha ganado jugador 2
    """
    print "Introduce el nombre de los jugadores"
    j1 = raw_input("Introduce el nombre del jugador 1: ")
    j2 = raw_input("Introduce el nombre del jugador 2: ")
    j3 = raw_input("Introduce el nombre del jugador 3: ")
    n = input("Introduce el numero de turnos")
    p1 = p2 = p3 = 0
    
    for i in range(1,n+1):
        print("%%%% Turno %d %%%%%" % (i))
        print("Jugador 1:", j1)
        print("Tirada %d: " % (i))
            
    
def main():
    print dado()
main()
