#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void sumar_palabras(char *buf1, char *buf2, char *p)
{
    strcpy(p, buf1);
    strcpy(p+strlen(buf1), buf2);
}
int main(void)
{
    char *p;
    char buf1[BUFSIZ], buf2[BUFSIZ];
    int len;
    
    scanf("%s %s", buf1, buf2);
    len = strlen(buf1) + strlen(buf2);
    p = (char *) malloc(len+1);
    if (strlen(buf1) < strlen(buf2))
        sumar_palabras(buf1, buf2, p);
    else
        sumar_palabras(buf2,  buf1, p);
    p[len] = '\0';
    
    printf("%s\n", p);
}
