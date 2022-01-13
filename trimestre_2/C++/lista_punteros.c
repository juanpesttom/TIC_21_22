#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char buff[BUFSIZ];
    char *lista[3];
    int i;
    
    for (i = 0; i < 3; i++)
    {
        printf("Introduce palabra %d: ", i+1);
        scanf("%s", buff);
        lista[i] = (char *) malloc(strlen(buff)+1);
        strcpy(lista[i], buff);
    }
    for (i = 0; i < 3; i++)
    {
        printf("%s\n", lista[i]);
    }
}
