#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    // reserva dinamica de memoria
    char buff[BUFSIZ];
    char *palabra;
    printf("Introduce una palabra: ");
    scanf("%s", buff);
    palabra = (char *) malloc(strlen(buff)+1);
    strcpy(palabra, buff);
    printf("%s\n", palabra);
    
    
}
